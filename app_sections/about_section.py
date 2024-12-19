import streamlit as st

def about_section_content():

    st.title("ST/H-Medic: Health Predictor and Medicine Advisor")

    # Section 1: Project Overview with Expander
    with st.expander("Project Overview"):
        st.markdown("""
        ST/H-Medic is an interactive Streamlit app designed to provide disease prediction, medicine recommendations, and a comprehensive medicine search feature. 
        The app uses machine learning and AI models to predict potential diseases based on user-reported symptoms, suggest related medicines, and provide real-time data analysis and visualization. 
        The app also allows users to search for medicines either by active ingredients or by medicine names, providing an all-in-one solution for users seeking health information.
        """)

    # Section 2: Project Aim with Expander
    with st.expander("Project Aim"):
        st.markdown("""
        The aim of the ST/H-Medic project is to build an accessible tool for disease prediction and medicine recommendation that can be used by the general public. 
        By using AI/machine learning models trained on various datasets, the app predicts diseases based on symptoms and suggests relevant medicines. 
        It also provides data analysis features, visualizations, and filtering tools to help users better understand health-related data. 
        The application serves as an educational tool and a starting point for exploring medical data.
        """)

    # Section 3: Technologies and Tools with Expander
    with st.expander("Technologies and Tools"):
        st.markdown("""
        The project utilizes a range of tools and technologies to provide an interactive and efficient solution:
        - **Streamlit**: The framework used to build the interactive user interface for the app.
        - **Machine Learning Models**: 
        - **Sklearn**: A popular machine learning library.
        - **Transformers (RoBERTa)**: A state-of-the-art NLP model for disease classification.
        - **Groq AI**: A large-scale language model used for advanced predictions.
        - **Data Processing**: 
        - **Pandas** for data manipulation.
        - **Selenium** for web scraping.
        - **Data Analysis**: Descriptive statistics and visualizations using libraries like Pandas and Plotly.
        - **OOP**: Following Object-Oriented Programming principles for scalable and maintainable code.
        """)

    # Section 4: Future Work with Expander
    with st.expander("Future Work"):
        st.markdown("""
        ST/H-Medic is part of a larger project that will be expanded in the future with new features like:
        - **Data Saving**: More robust back-end integration for saving and managing user data.
        - **Additional Sections**: Including personalized medication advice and disease prevention tips.
        - **Advanced Search Features**: Improved search capabilities with more advanced filters.
        """)

    # Important Disclaimer with Expander
    with st.expander("Important Disclaimer"):
        st.markdown("""
        **Please note that this app is for learning and informational purposes only.**  
        It should not be used as a replacement for professional medical advice. Always consult with a medical expert or doctor for accurate diagnosis and treatment recommendations.
        """)

