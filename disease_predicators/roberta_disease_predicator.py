import os

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import tensorflow as tf
tf.get_logger().setLevel('ERROR')

from transformers import logging
logging.set_verbosity_error()

from transformers import pipeline
from typing import List, Any, Tuple
from base_disease_predicator import DiseasePredictor


NLP_MODEL=pipeline("zero-shot-classification", model="facebookai/roberta-large-mnli")

class RobertaDiseasePredictor(DiseasePredictor):
    """
    A concrete subclass implementing the methods for disease prediction using Facebook's RoBERTa model.
    """

    def __init__(self, df: Any = None, model_name: str = "facebookai/roberta-large-mnli", candidate_labels: List[str] = None):
        """
        Initializes the RoBERTa-based disease predictor.
        Args:
            df: Input DataFrame (optional) not required for this class as RoBERTa uses zero-shot learning.
            model_name: The model name for the RoBERTa model (default: 'facebookai/roberta-large-mnli').
            candidate_labels: List of disease labels to classify symptoms against.
        """
        super().__init__(df, model=None)  # override the model initialization

        self.model_name = model_name
        self.candidate_labels = candidate_labels if candidate_labels else  [
            'Liver Diseases (Hepatitis B, Hepatitis C, Alcoholic Hepatitis, Chronic Hepatitis)',  # Antiviral treatment
            'Cardiovascular Diseases (Heart Disease, Stroke, Heart Attack)',  # Statins, antihypertensives
            'Diabetes & Metabolic Disorders (Type 2 Diabetes, Hypertension, Obesity, Hyperthyroidism, Hypothyroidism)',  # Insulin, antihypertensives, weight-loss drugs
            'Headache & Migraines',  # Pain relievers, triptans, prevention
            'Respiratory Diseases (Asthma, COPD, Pneumonia, Bronchitis, COVID)',  # Bronchodilators, corticosteroids, antibiotics
            'Gastrointestinal Disorders (Diarrhea, Gastroenteritis, Stomach Ulcer, Peptic Ulcer Disease, GERD)',  # Antidiarrheals, antibiotics, acid-reducing meds
            'Infectious Diseases (Tuberculosis, Dengue, Typhoid, Malaria)',  # Anti-TB drugs, antimalarials, antibiotics
            'Skin Disorders (Acne, Psoriasis, Impetigo, Fungal Infections)',  # Corticosteroids, antifungals, acne meds
            'Depression & Mental Health Disorders (Depression, Anxiety, Bipolar Disorder, PTSD)',  # Antidepressants, therapy
            'Common Cold (Upper Respiratory Tract Infection)',  # Decongestants, pain relievers, symptomatic treatment
        ]

        # Initialize the pipeline for zero-shot classification
        self.nlp = NLP_MODEL

    def save_model(self, model_path: str) -> None:
        pass

    def load_model(self, model_path: str, vectorizer_path: str, encoder_path: str) -> None:
        pass

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

    def predict(self, symptoms_list: List[str], top_n: int = 3) -> List[List[Tuple[str, str]]]:
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
            all_predictions = []  # To store results for all symptoms

            # Use batch processing to process multiple symptoms at once
            result = self.nlp(symptoms_list, candidate_labels=self.candidate_labels)

            # Loop through each symptom's prediction result and process
            for symptoms_idx, symptoms in enumerate(symptoms_list):
                # Process predictions and sort them by score (in descending order)
                sorted_results = sorted(zip(result[symptoms_idx]['labels'], result[symptoms_idx]['scores']), key=lambda x: x[1], reverse=True)
                top_n_predictions = sorted_results[:top_n]  # Select top N predictions

                # Convert the scores to percentages and format the output
                top_n_with_percentages = [(disease, f"{score * 100:.2f}%") for disease, score in top_n_predictions]

                # Append the predictions for this symptom to the results list
                all_predictions.append(top_n_with_percentages)

            return all_predictions

        except Exception as e:
            print(f"An error occurred during prediction: {e}")
            return {"error": str(e)}


# Initialize the predictor
predictor = RobertaDiseasePredictor()

symptoms = ["Patient 1: A 35-year-old male presenting with a persistent dry cough, shortness of breath, chest tightness, and fever for the past 4 days. No prior history of asthma or allergies."]

# Predict the top 3 diseases
top_3_predictions = predictor.predict(symptoms_list=symptoms)

# Display the top 3 predicted diseases
print("Top 3 Predicted Diseases:", top_3_predictions)

