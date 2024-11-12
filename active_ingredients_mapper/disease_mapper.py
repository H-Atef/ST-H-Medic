
from dataset_generator.active_ingredients_list import diseases_cls_to_active_ingredients
import pandas as pd
from typing import List,Tuple,Dict



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

            

        return active_ingredients_output_dict


    def map_diseases_cls(self,disease:str,actv_ing_output:Dict)->Dict:
        if disease in diseases_cls_to_active_ingredients.keys():
            actv_ing_output[disease.split("(")[0].strip()]=diseases_cls_to_active_ingredients[disease]
        
        return actv_ing_output
        
         


    def map_diseases(self,disease:str,actv_ing_output:Dict):

        if disease in list(self.df["Diseases"]) and not disease in diseases_cls_to_active_ingredients.keys():
                row=self.df[self.df["Diseases"]==disease]
                row=row.to_dict(orient="list")
                actv_ing_output[disease]=[x[1][0] for x in list(row.items())[:3]]

        return actv_ing_output
    
    def map_new_disease(self,disease:str,actv_ing_output:Dict):
        pass

    def add_new_disease_to_dataset(self,new_actv_ing_dict:Dict):
        pass



output_example= [[('Gastrointestinal Disorders (Diarrhea, Gastroenteritis, Stomach Ulcer, Peptic Ulcer Disease, GERD)', '53.00%'),
                  ('Respiratory Diseases (Asthma, COPD, Pneumonia, Bronchitis, COVID)', '20.00%'), 
                  ('Skin Disorders (Acne, Psoriasis, Impetigo, Fungal Infections)', '11.00%'),
                  ("Acne","%20")]]

actv_mapper=DiseaseActvIngMapper()

print(actv_mapper.map_pridected_diseases_to_actv(output_example))



# #Extracting diseases Only from the input using list comperhension
# extarcted_diseases_list=[disease[0] for tuple in output_example for disease in tuple]



# #The final output dictionary that includes all mapped diseases
# active_ingredients_output_dict={}

# #A list for including all mapped diseases  
# mapped_diseases=[]


# #A loop for mapping extracted diseases with their active ingredients
# for disease in extarcted_diseases_list:
#     if disease in diseases_cls_to_active_ingredients.keys():
#         active_ingredients_output_dict[disease.split("(")[0].strip()]=diseases_cls_to_active_ingredients[disease]
#         mapped_diseases.append(disease)


# #Removing all mapped diseases and updating the diseases list
# extarcted_diseases_list=[disease for disease in extarcted_diseases_list if not disease in mapped_diseases]


# #The predictors outputs could be disease classes or could be just diseases
# #Assuming there is a mixture of them both, so the diseases if found only should be mapped too

# #Checking if there is any disease left "As disease classes already mapped"
# if not extarcted_diseases_list==[]:
    
#     #A loop for checking and mapping the detected diseases by active_ingredients dataset
#     for disease in extarcted_diseases_list:
#         df=pd.read_csv("./datasets/active_ingredients_diseases.csv")
        
#         if disease in list(df["Diseases"]):
#             row=df[df["Diseases"]==disease]
#             row=row.to_dict(orient="list")
#             mapped_diseases.append(disease)
#             active_ingredients_output_dict[disease]=[x[1][0] for x in list(row.items())[:3]]

        
# #Removing all mapped diseases and updating the diseases list
# extarcted_diseases_list=[x for x in extarcted_diseases_list if not x in mapped_diseases]


# #Assuming that there is a disease or there are some diseases left after updating
# #That means that this disease is not found in the dataset 
# #So, groq active ingredients mapper will be used in order to get map these diseases to their actv_ing
# #In addition, adding them to the dataset
# if not extarcted_diseases_list==[]:
#     pass


# print(active_ingredients_output_dict)