from sklearn.base import ClassifierMixin
from typing import Tuple,List,Type
from groq import Groq
import importlib
import os
from dotenv import load_dotenv

load_dotenv()

module1='disease_predictors.base_disease_predictor'



class GroqDiseasePredictor(importlib.import_module(module1).DiseasePredictor):
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
        self.client = Groq(api_key=os.getenv("API_KEY"))

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
                    {"role": "assistant","content":"return ``` {*output*} ```" },
                    {   
                        

                        "role": "user",
                        "content": """ 
                                ```
                                Return the output like the following example for each case in this format:

                                ```  
                                {
                                'case1' : [('diseases', probabilities)]
                                }
                                ```
                                """+f"""
                                Given the following input:

                                ```
                                {symptoms_list}
                                ```

                                Return the top 3 related diseases for each string/case 
                                (each string could contain multiple symptoms the string fall between two ''), 
                                with the disease names and their corresponding probabilities in a dictionary 
                                and rename the keys of dict case1,case2,... etc 
                                and so on depend on the order of the string was in the list.

                                just the output only without any explainations or even notes.

                                     """
                        
                    }
                ],
                model="llama3-8b-8192",  # Assuming Groq uses Llama3 model
            )

            # Parse the result from the API (assuming it's a string representation of a list of tuples)
            predictions = chat_completion.choices[0].message.content

            print(predictions)


            # Using eval to convert the string into a list of tuples

            if "```" in predictions:
                results=eval(predictions.strip().split("```")[1].split("```")[0])
            else:
                results=eval(predictions.strip().split("```python")[1].split("```")[0])


            return self.convert_and_transfrom_result_dict(results)
        
        except Exception as e:
            print(e)
            return []
    
    def convert_and_transfrom_result_dict(self,data):
        
        #Convert Dict to List[List[Tuple[str, str]]]
        data=[data[key] for key in data.keys()]
      
        # transform probas to percentages
        return [
            [(disease, f"{str(round(float(percentage),1)*100)}%") for disease, percentage in case]
            for case in data
        ]



# predictor = GroqDiseasePredictor()
# symptoms = [
#     "Patient 1: A 35-year-old male presenting with a persistent dry cough, shortness of breath, chest tightness, and fever for the past 4 days. No prior history of asthma or allergies.",
#     "Patient 2: A 28-year-old female with a sudden onset of headache, fever, body aches, chills, and nausea. She reports fatigue and feeling extremely weak. No cough or respiratory symptoms.",
#     "Patient 3: A 45-year-old male complaining of fatigue, dry cough, and shortness of breath. He has a history of hypertension but no history of chronic respiratory illness.",
#     "Patient 4: A 60-year-old female with a runny nose, sore throat, mild cough, and low-grade fever for the past 2 days. She also reports feeling a little light-headed but has no chest pain.",
#     "Patient 5: A 50-year-old male who is experiencing a stuffy nose, sore throat, persistent cough, mild fever, and difficulty sleeping due to nasal congestion. He has a history of seasonal allergies.",
#     "Patient 6: A 30-year-old female with a persistent cough, sore throat, fever, chills, and body aches. She also reports difficulty swallowing and feeling nauseous.",
#     "Patient 7: A 25-year-old male presenting with symptoms of congestion, sore throat, mild fever, and a dry cough. He’s feeling fatigued but reports no difficulty breathing.",
#     "Patient 8: A 40-year-old female who has been experiencing a headache, fever, and chills along with muscle aches. She feels fatigued and reports a dry, unproductive cough."
# ]


# # Make a prediction
# predictions = predictor.predict(symptoms_list=symptoms)
# print(predictions)