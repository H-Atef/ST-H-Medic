
from dataset_generator.active_ingredients_list import disease_classes,active_ingredients,top_diseases_classes
import pandas as pd

output_example= [[('Gastrointestinal Disorders (Diarrhea, Gastroenteritis, Stomach Ulcer, Peptic Ulcer Disease, GERD)', '53.00%'), ('Respiratory Diseases (Asthma, COPD, Pneumonia, Bronchitis, COVID)', '20.00%'), ('Skin Disorders (Acne, Psoriasis, Impetigo, Fungal Infections)', '11.00%'),("Acne","%20")]]

extarcted_diseases_list=[disease[0] for tuple in output_example for disease in tuple]


#print(extarcted_diseases_list)


ready_to_be_mapped_dict={}
classes_to_delete=[]

for i,disease in enumerate(extarcted_diseases_list):
    if disease in top_diseases_classes.keys():
        ready_to_be_mapped_dict[disease.split("(")[0].strip()]=active_ingredients[disease]
        classes_to_delete.append(disease)


extarcted_diseases_list=[x for x in extarcted_diseases_list if not x in classes_to_delete]

classes_to_delete=[]
ready_to_map_diseases_list=[]
if not extarcted_diseases_list==[]:
    
    for disease in extarcted_diseases_list:
        df=pd.read_csv("./datasets/active_ingredients_diseases.csv")
        
        if disease in list(df["Diseases"]):
            row=df[df["Diseases"]==disease]
            row=row.to_dict(orient="list")
            classes_to_delete.append(disease)
            ready_to_be_mapped_dict[disease]=[x[1][0] for x in list(row.items())[:3]]

extarcted_diseases_list=[x for x in extarcted_diseases_list if not x in classes_to_delete]

print(extarcted_diseases_list)



print(ready_to_be_mapped_dict)