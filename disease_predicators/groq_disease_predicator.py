from sklearn.base import ClassifierMixin
from typing import Tuple,List,Type
from base_disease_predicator import DiseasePredictor
from ai_model_auth import API_KEY
from groq import Groq



class GroqDiseasePredictor(DiseasePredictor):
    """
    A subclass of DiseasePredictor that uses the Groq API to predict diseases based on symptoms.
    """

    def __init__(self, model: Type[ClassifierMixin] = None, model_params: dict = None):
        """
        Initializes the GroqDiseasePredictor with an API key for the Groq API.
        Args:
            api_key: The API key to authenticate with the Groq API.
            model: The machine learning model class (default is None).
            model_params: A dictionary of hyperparameters for the model (default is None).
        """
        super().__init__(df=None, model=model, model_params=model_params)  # df is not needed here as we're using Groq API
        self.client = Groq(api_key=API_KEY)

    def initialize_model(self) -> dict:
        """
        This method is not applicable for Groq API integration as the model is external.
        We can leave this method empty or raise an exception to indicate it's not needed.
        """
        raise NotImplementedError("Groq API does not require model initialization.")

    def save_model(self, model_path: str, vectorizer_path: str, encoder_path: str) -> None:
        """
        This method is not applicable for Groq API as it doesn't use a local machine learning model.
        """
        raise NotImplementedError("Groq API does not require model saving.")

    def load_model(self, model_path: str, vectorizer_path: str, encoder_path: str) -> None:
        """
        This method is not applicable for Groq API as it doesn't use a local machine learning model.
        """
        raise NotImplementedError("Groq API does not require model loading.")

    def predict(self, symptoms_list: List[str]) -> List[List[Tuple[str, str]]]:
        """
        This method uses the Groq API to predict the disease based on input symptoms.
        It sends the symptoms as input to the Groq API and returns the predictions.
        Args:
            input_list: A list of strings representing symptoms.
        Returns:
            A list of lists of tuples representing the top disease predictions for each case.
        """

        try:
        # Join the list of symptoms into a single string (space-separated)
        
            # Make API request for predictions
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content":  f"I want a list of top 3 diseases with their probabilities (as numbers without the '%' sign) for the following "
                                    f"list of symptoms: {symptoms_list}. For each symptom string, treat it as a separate case. For each case, "
                                    f"please return the top 3 diseases that related to these symptoms and their probabilities as numbers (no '%' sign). "
                                    f"Return the result as a list of lists of tuples, where each inner list corresponds to a case and contains "
                                    f"tuples in the format (disease_name, probability_as_string) without the '%' sign. "
                                    f"The result should look like this: "
                                    f"[ [('Disease1', '20'), ('Disease2', '30'), ('Disease3', '15')], "
                                    f"  [('Disease6', '80'), ('Disease7', '10'), ('Disease8', '4')], "
                                    f"  [('Disease11', '20'), ('Disease12', '18')], "
                                    f"  [('Disease16', '60'), ('Disease17', '20')] ]."
                                    f"Do not provide any explanations, just return the list in the requested format."

                        
                    }
                ],
                model="llama3-8b-8192",  # Assuming Groq uses Llama3 model
            )

            # Parse the result from the API (assuming it's a string representation of a list of tuples)
            predictions = chat_completion.choices[0].message.content
            
            if "```" in predictions:
                results=eval(predictions.strip().split("```")[1])
            else:
                results=eval(predictions.strip().split(":")[1])# Using eval to convert the string into a list of tuples

            return self.convert_to_percentage_format(results)
        
        except Exception as e:
            #print(e)
            return []
    
    def convert_to_percentage_format(self,data):
        return [
            [(disease, f"{percentage}%") for disease, percentage in case]
            for case in data
        ]



predictor = GroqDiseasePredictor()
symptoms = [
    "Patient 1: A 35-year-old male presenting with a persistent dry cough, shortness of breath, chest tightness, and fever for the past 4 days. No prior history of asthma or allergies.",
    "Patient 2: A 28-year-old female with a sudden onset of headache, fever, body aches, chills, and nausea. She reports fatigue and feeling extremely weak. No cough or respiratory symptoms.",
    "Patient 3: A 45-year-old male complaining of fatigue, dry cough, and shortness of breath. He has a history of hypertension but no history of chronic respiratory illness.",
    "Patient 4: A 60-year-old female with a runny nose, sore throat, mild cough, and low-grade fever for the past 2 days. She also reports feeling a little light-headed but has no chest pain.",
    "Patient 5: A 50-year-old male who is experiencing a stuffy nose, sore throat, persistent cough, mild fever, and difficulty sleeping due to nasal congestion. He has a history of seasonal allergies.",
    "Patient 6: A 30-year-old female with a persistent cough, sore throat, fever, chills, and body aches. She also reports difficulty swallowing and feeling nauseous.",
    "Patient 7: A 25-year-old male presenting with symptoms of congestion, sore throat, mild fever, and a dry cough. He’s feeling fatigued but reports no difficulty breathing.",
    "Patient 8: A 40-year-old female who has been experiencing a headache, fever, and chills along with muscle aches. She feels fatigued and reports a dry, unproductive cough."
]


# Make a prediction
predictions = predictor.predict(symptoms_list=symptoms)
print(predictions)