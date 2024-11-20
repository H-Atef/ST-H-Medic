import pandas as pd

class DiseaseOutputProcessor:
    def __init__(self, predicted_diseases=None, actv_res=None, diseases_dict=None):
        self.predicted_diseases = predicted_diseases
        self.actv_res = actv_res
        self.diseases_dict = diseases_dict
    
    def predicted_diseases_to_df(self) -> pd.DataFrame:
        """Convert predicted diseases to a DataFrame"""
        try:
            # Check if input is None or empty
            if not self.predicted_diseases or not isinstance(self.predicted_diseases, list) or len(self.predicted_diseases) == 0:
                return pd.DataFrame(columns=["Disease", "Probability", "Case"])  # Empty DataFrame with headers

            flat_diseases = []
            case_number = 1
            for sublist in self.predicted_diseases:
                for item in sublist:
                    flat_diseases.append([item[0], item[1], f"Case {case_number}"])
                case_number += 1
            
            # Create DataFrame
            df = pd.DataFrame(flat_diseases, columns=["Disease", "Probability", "Case"])
            return df
        except Exception as e:
            #print(f"Error in predicted_diseases_to_df: {e}")
            return pd.DataFrame(columns=["Disease", "Probability", "Case"])  # Empty DataFrame with headers
    
    def diseases_to_actv_df(self) -> pd.DataFrame:
        """Convert diseases' active ingredients to a DataFrame"""
        try:
            # Check if input is None or empty
            if not self.actv_res or not isinstance(self.actv_res, dict) or len(self.actv_res) == 0:
                return pd.DataFrame(columns=["Disease", "Active Ingredient", "Line"])  # Empty DataFrame with headers

            actv_data = []
            for disease, ingredients in self.actv_res.items():
                if not ingredients:  # Handle empty ingredients list
                    continue
                for i, ingredient in enumerate(ingredients[:3]):  # Limit to 3 ingredients
                    actv_data.append([disease, ingredient, f"{['primary', 'alternative1', 'alternative2'][i]}"])
            
            # Create DataFrame
            df = pd.DataFrame(actv_data, columns=["Disease", "Active Ingredient", "Line"])
            return df
        except Exception as e:
            #print(f"Error in diseases_to_actv_df: {e}")
            return pd.DataFrame(columns=["Disease", "Active Ingredient", "Line"])  # Empty DataFrame with headers
    
    def diseases_to_med_df(self) -> pd.DataFrame:
        """Convert diseases' medicines to a DataFrame"""
        try:
            # Check if input is None or empty
            if not self.diseases_dict or not isinstance(self.diseases_dict, dict) or len(self.diseases_dict) == 0:
                return pd.DataFrame(columns=["Disease", "Active Ingredient", "Drug Name", "Generic Name", "Drug Class", "Similars", "Alternatives"])  # Empty DataFrame with headers

            data = []
            
            for disease, details in self.diseases_dict.items():
                # Skip empty or None disease data
                if not details:
                    continue
                
                for ingredient, ingredient_details in details.items():
                    # Ensure all lists have the same length (fill missing entries with '-')
                    drug_names = ingredient_details.get("drug_name", ["-"] * max(len(ingredient_details.get("drug_name", [])), 1))
                    generic_names = ingredient_details.get("generic_name", ["-"] * max(len(ingredient_details.get("generic_name", [])), 1))
                    drug_classes = ingredient_details.get("drug_class", ["-"] * max(len(ingredient_details.get("drug_class", [])), 1))
                    
                    # Find the maximum length of all lists for this ingredient
                    max_len = max(len(drug_names), len(generic_names), len(drug_classes))
                    
                    # Ensure all lists are of equal length by extending with '-'
                    drug_names.extend(["-"] * (max_len - len(drug_names)))
                    generic_names.extend(["-"] * (max_len - len(generic_names)))
                    drug_classes.extend(["-"] * (max_len - len(drug_classes)))
                    
                    # Add rows for each combination of drug and other attributes
                    for i in range(max_len):
                        data.append([
                            disease,
                            ingredient,
                            drug_names[i],    
                            generic_names[i],
                            drug_classes[i]
                        ])
            
            # Convert the list of rows to a DataFrame
            df = pd.DataFrame(data, columns=["Disease", "Active Ingredient", "Drug Name", "Generic Name", "Drug Class"])
            return df
        except Exception as e:
            #print(f"Error in diseases_to_med_df: {e}")
            return pd.DataFrame(columns=["Disease", "Active Ingredient", "Drug Name", "Generic Name", "Drug Class"])  # Empty DataFrame with headers
