import pandas as pd
import active_ingredients_list as ac


class ActiveIngredientsDatasetGenerator:


    @classmethod
    def generate_csv_file(cls)->pd.DataFrame:

        try:

            # Create a list to store the final structured data
            final_data = []

            # Process each active ingredient and disease list
            for entry in ac.active_ingredients_list:
                ingredient = entry[0]
                diseases = entry[1:]

                treat_1 = ingredient
                treat_2 = None
                treat_3 = None

                # Find alternative treatments for the first disease
                if diseases:
                    disease = diseases[0]
                    alt_list = ac.alternatives.get(disease, [None])

                    if len(alt_list) > 0 and alt_list[0] != treat_1:
                        treat_2 = alt_list[0]  # First alternative, ensure it's not the same as Treat 1
                    if len(alt_list) > 1 and alt_list[1] != treat_1 and alt_list[1] != treat_2:
                        treat_3 = alt_list[1]  # Second alternative, ensure it's not the same as Treat 1 or Treat 2

                # If we don't have enough alternatives, fill with None
                final_data.append([treat_1, treat_2 if treat_2 else '-', treat_3 if treat_3 else '-', ', '.join(diseases)])

            # Create DataFrame from the final data
            df = pd.DataFrame(final_data, columns=['Treat 1', 'Treat 2', 'Treat 3', 'Disease'])

            # Save the DataFrame to a CSV file
            df.to_csv('active_ingredients_diseases.csv', index=False)

            return df
        
        except Exception as e:
            return pd.DataFrame({})
            print(e)


ActiveIngredientsDatasetGenerator.generate_csv_file()