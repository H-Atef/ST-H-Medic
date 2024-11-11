import os
from typing import Type, Dict, Any,Tuple,List
from base_disease_predictor import DiseasePredictor
from custom_disease_predictor import CustomDiseasePredictor
from groq_disease_predictor import GroqDiseasePredictor
from roberta_disease_predictor import RobertaDiseasePredictor

class DiseasePredictionContext:
    """
    Context class to manage different disease prediction strategies (predictors).
    """

    def __init__(self):
        """
        Initializes the context with a dictionary that maps each predictor to a string identifier.
        
        Args:
            model_dir: Directory where models will be saved or loaded from.
        """
        # Dictionary to map predictor names to their corresponding predictor classes
        self.predictor_map: Dict[str, Type[DiseasePredictor]] = {
            'custom': CustomDiseasePredictor,
            'groq': GroqDiseasePredictor,
            'roberta': RobertaDiseasePredictor,
        }
        self.current_predictor: DiseasePredictor = None

        

    def set_predictor(self, predictor_name: str, **kwargs: Any) -> None:
        """
        Set the current predictor strategy based on the name provided.
        
        Args:
            predictor_name: The name of the predictor strategy (e.g., 'custom', 'groq', 'roberta').
            kwargs: Additional parameters required to initialize the predictor.
        """
        if predictor_name in self.predictor_map:
            # Instantiate the chosen predictor with the provided arguments
            predictor_class = self.predictor_map[predictor_name]
            self.current_predictor = predictor_class(**kwargs)
            print(f"Switched to {predictor_name} predictor.")
        else:
            raise ValueError(f"Predictor {predictor_name} not found in the available strategies.")


    def predict(self, symptoms_list: list, **kwargs: Any) ->  List[List[Tuple[str, str]]]:
        """
        Makes predictions using the current selected predictor.
        
        Args:
            symptoms_list: A list of symptoms (strings) for which predictions are needed.
            top_n: The number of top predictions to return (default is 3).
        
        Returns:
            The predictions made by the current predictor.
        """
        if self.current_predictor:
            return self.current_predictor.predict(symptoms_list, **kwargs)
        else:
            raise RuntimeError("No predictor has been selected. Use set_predictor first.")




# Initialize the context
context = DiseasePredictionContext()


pred=context.set_predictor('custom')


# Use the loaded model to make predictions
symptoms = [
    "Patient 1: A 35-year-old male presenting with a persistent dry cough, shortness of breath, chest tightness, and fever for the past 4 days."
]
predictions = context.predict(symptoms)
print("Top 3 Predictions:", predictions)
