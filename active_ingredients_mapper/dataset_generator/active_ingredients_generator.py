import pandas as pd
import os
import active_ingredients_list as ac  # Assuming active_ingredients_list contains `active_ing_list`

class ActiveIngredientsDatasetGenerator:

    @classmethod
    def generate_csv_file(cls) -> pd.DataFrame:
        try:
            # Create a list to store the final structured data
            final_data = []

            # Process each entry in the active ingredients list
            for entry in ac.active_ingredients_list:
                option_one_treatment = entry[0]
                option_two_treatment = entry[1] if len(entry) > 1 else None
                option_three_treatment = entry[2] if len(entry) > 2 else None
                diseases = entry[3:]

                # If we don't have enough options, fill with '-'
                option_two_treatment = option_two_treatment if option_two_treatment else '-'
                option_three_treatment = option_three_treatment if option_three_treatment else '-'

                # Append the structured data
                final_data.append([option_one_treatment, option_two_treatment, option_three_treatment, ', '.join(diseases)])

            # Create DataFrame from the final data with descriptive column names
            df = pd.DataFrame(final_data, columns=['Option 1 Treatment', 
                                                   'Option 2 Treatment', 
                                                   'Option 3 Treatment', 
                                                   'Diseases'])
            

            if not os.path.exists("../datasets/"):
                os.makedirs("../datasets/") 

            # Save the DataFrame to a CSV file
            df.to_csv('../datasets/active_ingredients_diseases.csv', index=False)

            return df
        
        except Exception as e:
            print(e)
            return pd.DataFrame({})

# Generate the CSV file
ActiveIngredientsDatasetGenerator.generate_csv_file()
