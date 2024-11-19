import pandas as pd
from sklearn.utils import resample
from itertools import combinations
import disease_predictors.common_diseases_list as cd

class OriginalDatasetPre:

    def __init__(self, df: pd.DataFrame):
        self.df = df

        # Define the mapping of diseases to their classes
        self.disease_classes = cd.disease_classes

    def map_disease_to_class(self):
        # Create a reverse mapping from disease to class for faster lookup
        disease_to_class = {disease.lower().strip(): cls for cls, diseases in self.disease_classes.items() for disease in diseases}

        # Map each disease in the 'Disease' column to its corresponding class
        self.df['Disease_Class'] = self.df['Disease'].map(lambda x: disease_to_class.get(x.strip().lower(), 'Unknown'))

        return self.df

    def add_new_diseases(self, new_diseases_list) -> pd.DataFrame:
        try:
            # Generate all unique symptom combinations for each new disease
            all_combinations = []
            for disease in new_diseases_list:
                disease_name = disease['Disease']
                symptoms = [disease[f'Symptom_{i + 1}'] for i in range(8) if f'Symptom_{i + 1}' in disease and pd.notna(disease[f'Symptom_{i + 1}'])]

                # Create combinations of symptoms
                for r in range(3, len(symptoms) + 1):
                    for combo in combinations(symptoms, r):
                        # Prepare each row as a dictionary
                        row = {'Disease': disease_name}
                        for i, symptom in enumerate(combo):
                            row[f'Symptom_{i + 1}'] = symptom
                        all_combinations.append(row)

            # Convert the combinations to a DataFrame
            combinations_df = pd.DataFrame(all_combinations)
            # Append the new data to the original dataset
            updated_data = pd.concat([self.df, combinations_df], ignore_index=True)

            # Assign disease classes to the new rows
            updated_data = self.map_disease_to_class()

            self.df = updated_data.copy()

            # Save the updated dataset
            updated_data.to_csv('./datasets/updated_disease_symptom_dataset.csv', index=False)

            return self.df

        except Exception as e:
            print(e)
            return pd.DataFrame({})

    def fill_and_group_symptoms(self) -> pd.DataFrame:
        try:
            # Fill NaN values with empty string
            self.df = self.df.fillna("")

            # Dynamically select symptom columns (assuming symptom columns have a consistent naming convention)
            symptom_columns = [col for col in self.df.columns if col.startswith('Symptom_')]

            # Remove extra spaces in between (in case some symptom columns are empty)
            self.df["Symptoms"] = self.df[symptom_columns].apply(lambda row: " ".join(filter(bool, row)), axis=1)

            # Drop the individual symptom columns
            self.df.drop(symptom_columns, axis=1, inplace=True)

            return self.df

        except Exception as e:
            print(e)
            return pd.DataFrame({})

    def balance_dataset(self) -> pd.DataFrame:
        try:
            # Get the value counts of the Disease_Class column
            class_counts = self.df['Disease_Class'].value_counts()

            # Find the maximum class size (to balance all other classes)
            max_class_size = class_counts.max()

            # Create lists of classes that need to be oversampled (those with fewer rows than the maximum)
            oversample_classes = [cls for cls, count in class_counts.items() if count < max_class_size]
            undersample_classes = [cls for cls, count in class_counts.items() if count > max_class_size]

            # Perform Oversampling for underrepresented classes
            oversampled_data = []
            for cls in oversample_classes:
                class_data = self.df[self.df['Disease_Class'] == cls]
                oversampled_data.append(resample(class_data, 
                                                 replace=True,  # With replacement
                                                 n_samples=max_class_size - len(class_data),  # Number of samples to add
                                                 random_state=42))  # For reproducibility

            # Perform Undersampling for overrepresented classes
            undersampled_data = []
            for cls in undersample_classes:
                class_data = self.df[self.df['Disease_Class'] == cls]
                undersampled_data.append(resample(class_data, 
                                                  replace=False,  # Without replacement
                                                  n_samples=max_class_size,  # Limit to the maximum size
                                                  random_state=42))  # For reproducibility

            # Concatenate all resampled datasets
            balanced_data = pd.concat([self.df] + oversampled_data + undersampled_data)

            # Shuffle the dataset after resampling (optional but recommended)
            balanced_data = balanced_data.sample(frac=1, random_state=42).reset_index(drop=True)

            self.df = balanced_data.copy()

            return self.df

        except Exception as e:
            print(e)
            return pd.DataFrame({})

    def process_dataset(self, new_diseases_list=None) -> pd.DataFrame:
        try:
            if new_diseases_list is None:
                self.fill_and_group_symptoms()
                self.map_disease_to_class()  # Ensure Disease_Class is assigned
                self.balance_dataset()
            else:
                self.add_new_diseases(new_diseases_list=new_diseases_list)
                self.fill_and_group_symptoms()
                self.map_disease_to_class()  # Ensure Disease_Class is assigned after new diseases
                self.balance_dataset()

            # Save the processed dataset
            self.df.to_csv("./datasets/processed_dataset.csv", index=False)

            return self.df

        except Exception as e:
            print(e)
            return pd.DataFrame({})


# Example usage:

# # Load the initial dataset
# df = pd.read_csv('./datasets/disease_symptom_dataset.csv')

# # Create an instance of the OriginalDatasetPre class
# pre = OriginalDatasetPre(df)

# # Add new diseases (if any)
# new_diseases_list = cd.common_diseases_to_add  # Replace with your actual list of new diseases
# df = pre.process_dataset()

# # Output the balanced dataset
# print(df['Disease_Class'].value_counts())
