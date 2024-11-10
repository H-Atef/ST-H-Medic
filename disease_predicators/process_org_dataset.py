import pandas as pd
from itertools import combinations
import common_diseases_list as cd





class OriginalDatasetPre:

    def __init__(self,df:pd.DataFrame):
        self.df=df


    def add_new_diseases(self,new_diseases_list)->pd.DataFrame:

        try:

            # Generate all unique symptom combinations for each new disease
            all_combinations = []
            for disease in new_diseases_list:
                disease_name = disease['Disease']
                symptoms = [disease[f'Symptom_{i+1}'] for i in range(8) if f'Symptom_{i+1}' in disease and pd.notna(disease[f'Symptom_{i+1}'])]

                # Create combinations of symptoms
                for r in range(3, len(symptoms) + 1):
                    for combo in combinations(symptoms, r):
                        # Prepare each row as a dictionary
                        row = {'Disease': disease_name}
                        for i, symptom in enumerate(combo):
                            row[f'Symptom_{i+1}'] = symptom
                        all_combinations.append(row)

            # Convert the combinations to a DataFrame
            combinations_df = pd.DataFrame(all_combinations)
            # Append the new data to the original dataset
            updated_data = pd.concat([self.df, combinations_df], ignore_index=True)

            # # Sort the data alphabetically by disease
            # updated_data = updated_data.sort_values(by='Disease').reset_index(drop=True)

            # Save the updated dataset
            updated_data.to_csv('./datasets/updated_disease_symptom_dataset.csv', index=False)


            self.df=updated_data.copy()


            return self.df
        
        except Exception as e:
            print(e)
            return pd.DataFrame({})
    
    def fill_and_group_symptoms(self)->pd.DataFrame:

        try:
        
            # Fill NaN values with empty string
            self.df = self.df.fillna("")

            # Dynamically select symptom columns (assuming symptom columns have a consistent naming convention)
            symptom_columns = [col for col in self.df.columns if col.startswith('Symptom_')]

            # remove extra spaces in between (in case some symptom columns are empty)
            self.df["Symptoms"] = self.df[symptom_columns].apply(lambda row: " ".join(filter(bool, row)), axis=1)

            self.df.drop(symptom_columns,axis=1,inplace=True)

            return self.df

        except Exception as e:
            print(e)
            return pd.DataFrame({})
        

    def balance_dataset(self)->pd.DataFrame:

        try:

            # Step 1: Get the value counts of the Disease column
            disease_counts = self.df['Disease'].value_counts()

            # Step 2: Filter out diseases with counts less than 120
            diseases_to_keep = disease_counts[disease_counts >= 120].index

            # Step 3: Filter the DataFrame to only include rows with diseases that have count >= 120
            filtered_df = self.df[self.df['Disease'].isin(diseases_to_keep)]

            # Step 4: Ensure that diseases with counts > 120 have only 120 rows
            balanced_df = pd.DataFrame()

            for disease in diseases_to_keep:
                disease_rows = filtered_df[filtered_df['Disease'] == disease]
                # If disease has more than 120 occurrences, limit it to 120 rows
                if len(disease_rows) > 120:
                    disease_rows = disease_rows.sample(n=120, random_state=42)  # Randomly sample 120 rows
                balanced_df = pd.concat([balanced_df, disease_rows])

            # Reset index of the final DataFrame
            balanced_df = balanced_df.reset_index(drop=True)

            # # Sort the data alphabetically by disease
            # balanced_df= balanced_df.sort_values(by='Disease').reset_index(drop=True)

            self.df=balanced_df.copy()

            return self.df
        
        except Exception as e:
            print(e)
            return pd.DataFrame({})
    

    def process_dataset(self,new_diseases_list=None)->pd.DataFrame:

        try:

         if new_diseases_list is None:
            self.fill_and_group_symptoms()
            self.balance_dataset()

         else:
            self.add_new_diseases(new_diseases_list=new_diseases_list)
            self.fill_and_group_symptoms()
            self.balance_dataset()

         self.df.to_csv("./datasets/processed_dataset.csv",index=False)

         return self.df
             
        except Exception as e:
            print(e)
            return pd.DataFrame({})





    

        
            

df = pd.read_csv('./datasets/disease_symptom_dataset.csv')
pre=OriginalDatasetPre(df)
new_diseases_list=cd.common_diseases_to_add
df=pre.process_dataset()
print(df['Disease'].value_counts())














