import os

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import tensorflow as tf
tf.get_logger().setLevel('ERROR')

from transformers import logging
logging.set_verbosity_error()


from transformers import pipeline
from typing import List,Any,Tuple
from base_disease_predicator import DiseasePredictor






class RobertaDiseasePredictor(DiseasePredictor):
    """
    A concrete subclass implementing the methods for disease prediction using Facebook's RoBERTa model.
    """

    def __init__(self, df: Any = None, model_name: str = "facebookai/roberta-large-mnli", candidate_labels: List[str] = None, model_dir: str = './roberta_model'):
        """
        Initializes the RoBERTa-based disease predictor.
        Args:
            df: Input DataFrame (optional) – not required for this class as RoBERTa uses zero-shot learning.
            model_name: The model name for the RoBERTa model (default: 'facebookai/roberta-large-mnli').
            candidate_labels: List of disease labels to classify symptoms against.
            model_dir: Directory where the model is saved or will be saved (default: './roberta_model').
        """
        super().__init__(df, model=None)  # We override the model initialization

        self.model_name = model_name
        self.candidate_labels = candidate_labels if candidate_labels else [
            '(vertigo) Paroymsal  Positional Vertigo', 'AIDS', 'Acne', 'Alcoholic hepatitis', 'Allergic Rhinitis', 'Allergy', 
            'Arthritis', 'Bronchial Asthma', 'Cervical spondylosis', 'Chicken pox', 'Chronic cholestasis', 'Common Cold', 'Dengue',
            'Diabetes ', 'Diabetic Neuropathy', 'Diarrhea', 'Dimorphic hemmorhoids(piles)', 'Drug Reaction', 'Fungal infection', 
            'GERD', 'Gastroenteritis', 'Headache', 'Heart attack', 'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E', 
            'Hypertension ', 'Hyperthyroidism', 'Hypoglycemia', 'Hypothyroidism', 'Impetigo', 'Jaundice', 'Malaria', 'Migraine',
            'Osteoarthristis', 'Paralysis (brain hemorrhage)', 'Peptic ulcer diseae', 'Pneumonia', 'Psoriasis', 'Stomach Ulcer', 
            'Tuberculosis', 'Typhoid', 'Urinary tract infection', 'Varicose veins', 'hepatitis A'
        ]

        self.model_dir = model_dir  # Directory to store the model

        # Initialize the pipeline for zero-shot classification
        self.nlp = None  # We will initialize the model and tokenizer here when needed
        self._load_or_initialize_model()

    def _load_or_initialize_model(self):
        """
        Loads the model if it's already saved, otherwise initializes the model and saves it for future use.
        """
        if os.path.exists(self.model_dir):
            print(f"Loading model from {self.model_dir}")
            self.nlp = pipeline("zero-shot-classification", model=self.model_dir, tokenizer=self.model_dir)
        else:
            print("Model not found, loading from Hugging Face and saving it.")
            self.nlp = pipeline("zero-shot-classification", model=self.model_name, tokenizer=self.model_name)
            self.save_model(self.model_dir)

    def save_model(self, model_path: str) -> None:
        """
        Saves the model and tokenizer to the specified directory.
        """
        try:
            print(f"Saving model and tokenizer to {model_path}")
            self.nlp.model.save_pretrained(model_path)
            self.nlp.tokenizer.save_pretrained(model_path)
        except Exception as e:
            print(f"An error occurred while saving the model: {e}")

    def load_model(self, model_path: str, vectorizer_path: str, encoder_path: str) -> None:
        """
        Loads a pre-trained model from HuggingFace and tokenizer if saved.
        This method is overridden for consistency but not used as RoBERTa uses Hugging Face pipeline directly.
        """
        print("Model is pre-trained and loaded directly from HuggingFace model hub.")
        # This method is left for interface consistency with the abstract class, though it’s not used here.

    def initialize_model(self) -> dict:
        """
        Initializes the model (RoBERTa in this case). Since RoBERTa is pre-trained and doesn't need to be trained on the dataset,
        this method will simply set up the necessary components.
        """
        try:
            # No model training required, as it's a zero-shot classifier
            return {"message": "Model is pre-trained and ready to use."}
        except Exception as e:
            print(f"An error occurred during model initialization: {e}")
            return {"error": str(e)}

    def predict(self, symptoms_list: List[str], top_n: int = 5) -> List[List[Tuple[str, str]]]:
        """
        Predicts the top N diseases for each symptom string in the input list using zero-shot classification,
        with probabilities as percentages.
        Args:
            symptoms_list: A list of strings, each containing a list of symptoms to classify.
            top_n: The number of top predictions to return for each symptom string (default is 5).
        Returns:
            A list of lists, where each inner list contains tuples of predicted diseases and their probabilities 
            in percentage form for a corresponding symptom string.
        """
        try:
            result = self.nlp(symptoms_list, candidate_labels=self.candidate_labels, truncation=True, max_length=128)

            # Process predictions
            all_predictions = []
            for res in result:
                sorted_results = sorted(zip(res['labels'], res['scores']), key=lambda x: x[1], reverse=True)
                top_n_predictions = sorted_results[:top_n]  # Select top N predictions

                # Convert the scores to percentages and format the output
                top_n_with_percentages = [(disease, f"{score * 100:.2f}%") for disease, score in top_n_predictions]
                all_predictions.append(top_n_with_percentages)

            return all_predictions

        except Exception as e:
            print(f"An error occurred during prediction: {e}")
            return {"error": str(e)}

# Initialize the predictor
predictor = RobertaDiseasePredictor()

# Example symptom input
input_list = ["Sneezing", "Runny nose", "Sore throat", "Cough"]

# Join the list of symptoms into a single string (space-separated)
input_string = " ".join(input_list)

# Predict the top 5 diseases
top_5_predictions = predictor.predict([input_string])

# Display the top 5 predicted diseases
print("Top 5 Predicted Diseases:", top_5_predictions)
