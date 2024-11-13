
from dataset_generator.active_ingredients_list import diseases_cls_to_active_ingredients
import pandas as pd
from typing import List,Tuple,Dict
from ai_mapper import GroqActvIngMapper



class DiseaseActvIngMapper:

    def __init__(self,
                 df:pd.DataFrame=pd.read_csv("./datasets/active_ingredients_diseases.csv"),
                 predicted_diseases:List[List[Tuple[str,str]]]=None
                 ):
        self.df=df
        self.predicted_diseases=predicted_diseases
        

    
    def extract_diseases_only(self,predicted_diseases:List[List[Tuple[str,str]]]=None)->List:
        
        #Extracting diseases Only from the input using list comperhension
        extarcted_diseases_list=[disease[0] for tuple in predicted_diseases for disease in tuple]

        return extarcted_diseases_list
    

    def check_and_filter_new_diseases(self,diseases_list:List=None)->List:
        filtered_list=[disease for disease in diseases_list if
                        not disease in diseases_cls_to_active_ingredients and
                        not disease in list(self.df["Diseases"])
                        ]
        
        return filtered_list


    def map_pridected_diseases_to_actv(self,predicted_diseases:List[List[Tuple[str,str]]]=None)->Dict:

        if predicted_diseases is None:
            if not self.predicted_diseases is None:
                predicted_diseases=self.predicted_diseases
            
            else:
                return {}
            
        
        extarcted_diseases_list=self.extract_diseases_only(predicted_diseases)

       
                
        #The final output dictionary that includes all mapped diseases
        active_ingredients_output_dict={}



        #A loop for mapping extracted diseases with their active ingredients
        for disease in extarcted_diseases_list:
            
            self.map_diseases_cls(disease,active_ingredients_output_dict)

            self.map_diseases(disease,active_ingredients_output_dict)


        filtered_list=self.check_and_filter_new_diseases(extarcted_diseases_list)

        if not filtered_list ==[]:
            new_diseses_dict=self.ai_map_disease_to_actv_ing(filtered_list)

            if not new_diseses_dict=={}:
                active_ingredients_output_dict.update(new_diseses_dict)
                self.save_new_disease_records(new_diseses_dict)
            

        return active_ingredients_output_dict


    def map_diseases_cls(self,disease:str,actv_ing_output:Dict)->Dict:
        if disease in diseases_cls_to_active_ingredients.keys():
            actv_ing_output[disease.split("(")[0].strip()]=diseases_cls_to_active_ingredients[disease]
        
        return actv_ing_output
        
         


    def map_diseases(self,disease:str,actv_ing_output:Dict)->Dict:

        if disease in list(self.df["Diseases"]) and not disease in diseases_cls_to_active_ingredients.keys():
                row=self.df[self.df["Diseases"]==disease]
                row=row.to_dict(orient="list")
                actv_ing_output[disease]=[x[1][0] for x in list(row.items())[:3]]

        return actv_ing_output
    
    def save_new_disease_records(self,data_dict:Dict=None)->pd.DataFrame:

        try:

            new_df = pd.DataFrame.from_dict(
                            {disease: {
                                'Primary Active Ingredient': ingredients[0] if len(ingredients) > 0 else None,
                                'Alternative Treatment 1': ingredients[1] if len(ingredients) > 1 else None,
                                'Alternative Treatment 2': ingredients[2] if len(ingredients) > 2 else None,
                                'Diseases': disease
                            } for disease, ingredients in data_dict.items()},
                            orient='index'
                        ).reset_index(drop=False)

            try:
                ai_df = pd.read_csv("./datasets/ai_active_ingredients_diseases.csv")
            except FileNotFoundError:
                # If file is not found, create an empty DataFrame with the specified columns
                ai_df = pd.DataFrame(columns=[
                    'Primary Active Ingredient','Alternative Treatment 1', 
                    'Alternative Treatment 2', 'Diseases'])

            # Append the new data to the existing DataFrame
            self.df = pd.concat([self.df, new_df], ignore_index=True)
            ai_df = pd.concat([ai_df, new_df], ignore_index=True)

            self.df.drop('index',axis=1,inplace=True)
            ai_df.drop('index',axis=1,inplace=True)

            self.df.to_csv("./datasets/active_ingredients_diseases.csv",index=False)
            ai_df.to_csv("./datasets/ai_active_ingredients_diseases.csv",index=False)

        except Exception as e:
            print(e)


    def ai_map_disease_to_actv_ing(self,diseases:List)->Dict:
        groq_mapper=GroqActvIngMapper()
        result=groq_mapper.map_diseases(diseases_list=diseases)
        return result



output_example= [[('Gastrointestinal Disorders (Diarrhea, Gastroenteritis, Stomach Ulcer, Peptic Ulcer Disease, GERD)', '53.00%'),
                  ('Respiratory Diseases (Asthma, COPD, Pneumonia, Bronchitis, COVID)', '20.00%'), 
                  ('Skin Disorders (Acne, Psoriasis, Impetigo, Fungal Infections)', '11.00%'),
                  ("Common Cold","%10")
                  ]]

actv_mapper=DiseaseActvIngMapper()

print(actv_mapper.map_pridected_diseases_to_actv(output_example))



