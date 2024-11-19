

import disease_predictors.disease_predictor_main as disease_predictor
import active_ingredients_mapper.disease_mapper as disease_actv_mapper
import medicine_mapper.active_ingredient_scraper as actv_med_scraper
import outputs_processor as pro




symptoms = [
    "Case 1: A 35-year-old male presenting with a persistent dry cough shortness of breath chest tightness and fever for the past 4 days."
]

predictor = disease_predictor.DiseasePredictionContext()



predictor.set_predictor('custom')

predicted_diseases = predictor.predict(symptoms)

actv_mapper=disease_actv_mapper.DiseaseActvIngMapper()
actv_res=actv_mapper.map_pridected_diseases_to_actv(['common cold','COVID-19'])


med_scraper=actv_med_scraper.DrugEyeActvIngScraper()
med_res=med_scraper.scrape_multiple_data(actv_res)

df_converter=pro.DiseaseOutputProcessor(predicted_diseases,actv_res,med_res)

print(df_converter.predicted_diseases_to_df())
print(df_converter.diseases_to_actv_df())
print(df_converter.diseases_to_med_df())