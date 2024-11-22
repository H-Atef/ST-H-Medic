# ST/H-Medic: Health Predictor and Medicine Advisor

## Project Overview

ST/H-Medic is an interactive Streamlit app designed to provide disease prediction, medicine recommendations, and a comprehensive medicine search feature. The app uses machine learning and AI models to predict potential diseases based on user-reported symptoms, suggest related medicines, and provide real-time data analysis and visualization. The app also allows users to search for medicines either by active ingredients or by medicine names, providing an all-in-one solution for users seeking health information.

The app is built using modern technologies like Streamlit, Sklearn, Transformers, Groq AI, and Selenium for web scraping. It is part of a larger project and is intended to be expanded with more advanced features and datasets in the future.

## Project Aim

The aim of the ST/H-Medic project is to build an accessible tool for disease prediction and medicine recommendation that can be used by the general public. By using AI/machine learning models trained on various datasets, the app predicts diseases based on symptoms and suggests relevant medicines. It also provides data analysis features, visualizations, and filtering tools to help users better understand health-related data. The application serves as an educational tool and a starting point for exploring medical data.

### Important Disclaimer

**Please note that this app is for learning and informational purposes only. It should not be used as a replacement for professional medical advice. Always consult with a medical expert or doctor for accurate diagnosis and treatment recommendations.**

## Project Sections

ST/H-Medic consists of three main sections:

### 1. Disease Prediction and Medicine Recommendation

- **Disease Prediction**: Users input their symptoms, and the app predicts potential diseases based on those symptoms. The predictions are powered by AI models.
- **Medicine Recommendation**: Once a disease is predicted, the app maps the disease to its most related active ingredients, providing users with medicine suggestions based on these ingredients.
- **Data Scraping**: The app scrapes relevant medicine data using web scraping techniques to fetch the information about active ingredients and associated medicines.

### 2. Data Stats and Visualization Section

- After retrieving the data, this section offers a summary of the information with descriptive statistics, visualizations, and filters that allow users to explore the data in-depth.
- Users can apply filters to view specific subsets of the data, helping them understand medicines and active ingredients relations better.

### 3. Medicine Search Section

- **Search by Active Ingredients**: This search option allows users to find medicines based on their active ingredients.
- **Search by Medicine Name**: Users can search directly for a specific medicine by name to find relevant information.

## Technologies and Tools

The project utilizes a range of tools and technologies to provide an interactive and efficient solution:

- **Streamlit**: The framework used to build the interactive user interface for the app.
- **Machine Learning Models**:
  - **Sklearn**: A popular machine learning library used to train the custom model on disease-symptom data.
  - **Transformers (RoBERTa)**: A state-of-the-art natural language processing (NLP) model used for disease classification. RoBERTa has been fine-tuned on a multi-class classification task, making it more robust and accurate for disease predictions.
  - **Groq AI**: The Llama3-8B-8192 model, which is a large-scale language model used for more advanced predictions and data processing. This model enhances prediction capabilities and provides more reliable results.
- **Data Processing**:
  - **Pandas**: For data manipulation and transformation.
  - **Selenium**: Used for web scraping to gather relevant data about medicines, active ingredients, and diseases.
  - **Threading**: Employed to speed up data retrieval and web scraping processes, ensuring quicker response times for the user.
- **Data Analysis**:
  - Descriptive statistics and visualizations are generated using libraries like Pandas and Plotly to help users better understand the health-related data.
- **OOP (Object-Oriented Programming)**: The project follows OOP principles to ensure clean, maintainable, and scalable code.
- **AI & ML Concepts**: The project applies various machine learning concepts such as classification, and model training on real-world datasets to enhance the accuracy of disease predictions.

### Kaggle Dataset

The custom model has been trained on the Kaggle dataset [Disease-Symptom-Description Dataset](https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset/data?select=dataset.csv). This dataset was preprocessed by clustering diseases into main classes to address the challenges posed by similar symptoms across diseases. Although the model provides fast results, it is not the most accurate in terms of prediction reliability due to the inherent complexity of the symptoms.

### Models Details

- **RoBERTa Model**: A robust transformer model that is suitable for the disease classification task. It offers a significant improvement in prediction accuracy.
- **Groq AI (Llama3-8B-8192)**: A highly sophisticated AI model that leverages cutting-edge language processing capabilities to provide more precise results for disease prediction and medicine recommendations.

## Future Work

ST/H-Medic is part of a larger project that will be expanded in the future, with several new features and improvements:

- **Data Saving**: In the future, better data-saving processes will be implemented with a more robust back-end built in Django. This will allow for saving and managing user data and predictions more effectively.
- **Additional Sections**: The app may include additional sections like personalized medication advice, disease prevention tips, and more detailed medical statistics.

- **Improved Data Collection**: Data gathering will be expanded, with more comprehensive information on medicines, active ingredients, diseases, and treatment options.

- **Advanced Search Features**: Search capabilities will be extended to include more advanced filters, such as searching by disease categories or patient demographics.

---

**Important Reminder**: This project is for educational purposes only. It is not intended to replace professional medical advice. Always consult with healthcare professionals for diagnosis and treatment options.
