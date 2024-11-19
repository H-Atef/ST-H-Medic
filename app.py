import streamlit as st
import pandas as pd
import disease_predictors.disease_predictor_main as disease_predictor
import active_ingredients_mapper.disease_mapper as disease_actv_mapper
import medicine_mapper.active_ingredient_scraper as actv_med_scraper

# Title of the app
st.title("H-Medic: Disease Prediction & Medicine Recommendation")

# 1. Input Field to Get Symptoms or Disease
input_text = st.text_area("Enter Symptoms or Disease",placeholder="Please Enter Symptoms or Diseases Here")

# 2. Fancy Radio Button or Button to Specify If it's Symptoms or Disease
input_type = st.radio(
    "Is the input text about Symptoms or a Disease?",
    ('Symptoms', 'Disease')
)

if input_type=='Symptoms':
    # 3. Dropdown Menu to Select the Disease Prediction Model
    model_option = st.selectbox(
    "Select Disease Prediction Model",
    ('custom', 'groq', 'roberta'),
    )






# Create a DataFrame for displaying the entered information
input_data = {
    "Entered Input": [input_text.strip().strip(' ').split('/')],
    "Input Type": [input_type],
    "Prediction Model": [model_option] if input_type == 'Symptoms' else ["-"]
}

# Convert the dictionary to a DataFrame
input_df = pd.DataFrame(input_data)

# Display the table
st.write(input_df)

# Button to trigger prediction or active mapping
if st.button("Process Input"):
    try:
     
     if input_type=='Disease':
        pass
     
     if input_type=='Symptoms':
        pass
     

    except Exception as e:
        st.error(f"Error during prediction or mapping: {e}")
