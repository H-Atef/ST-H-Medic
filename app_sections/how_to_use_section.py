import streamlit as st


def how_to_use_app_section_content():
    st.title("How to Use ST/H-Medic")

    st.markdown("""
    ### Welcome to ST/H-Medic!
    This app helps in predicting diseases based on symptoms, recommending treatments, and finding/scraping for medicines related to active ingredients. 

    ### How It Works:
    - **Step 1**: Enter symptoms or a disease name.
    - **Step 2**: Choose the input type (Symptoms or Disease).
    - **Step 3**: Select a disease prediction model (if symptoms are provided).
    - **Step 4**: Click "Process Input" to get predictions, active ingredient mapping, and recommended medicines.

    ### Disease Prediction Models:
    #### 1. **Custom Model**:
    - A basic machine learning model with lower accuracy. It may work well for fast general predictions but is not ideal for precise medical advice.

    #### 2. **RoBERTa Model**:
    - This is a pre-trained model from Hugging Face, providing better accuracy than the custom model. RoBERTa is a transformer-based model that has been trained on vast amounts of data, improving its prediction capabilities for disease detection.

    #### 3. **Groq AI Model (Llama3-8B-8192)**:
    - This is the most advanced model available, based on Groq AI's Llama3-8B-8192 architecture. It uses an 8-billion parameter transformer and provides high accuracy in predicting diseases. It's the best option for obtaining reliable and precise predictions based on symptoms.

    ### Notes:
    - **Medical Disclaimer**: The predictions provided by this app are for informational purposes only and should not replace professional medical advice. Always consult a healthcare provider for accurate diagnosis and treatment.
    """)
