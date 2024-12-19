import streamlit as st
import pandas as pd
import medicine_mapper.active_ingredient_scraper as actv_med_scraper

import importlib

path='app_sections.'

pro=importlib.import_module(f'{path}outputs_processor')






def search_med_section_content():
    # Title of the app
    st.title("ST/H-Medic: Search Medicines")

    
    input_text = st.text_area("Enter Medicines Or Active Ingredients", 
                              placeholder="Please Enter Medicines or Active Ingredients Here")
    
    st.markdown("<p style='font-size: 14px; color: gray;'>"
                            "<strong>Note: </strong>If you want to enter multiple Medicines or Active Ingredients,"
                            " separate them with a '/' (e.g., 'medicine1/medicine2').</p>",
                              unsafe_allow_html=True)

    
    search_type = st.radio(
        "Choose The Search Type",
        ('BY Medicine Name','By Active Ingredient')
    )


    # Create a DataFrame for displaying the entered information
    input_data = {
        "Entered Input": [input_text.strip().strip(' ').split('/')],
        "Input Type":[search_type]
    }

    # Convert the dictionary to a DataFrame
    input_df = pd.DataFrame(input_data)

    # Display the table
    st.write(input_df)

    # Button to trigger prediction or active mapping
    if st.button("Search"):

        df_converter = pro.DiseaseOutputProcessor()
        
        try:       

            # Scrape medicines data
            med_scraper = actv_med_scraper.DrugEyeActvIngScraper()

            with st.spinner('Please Wait...'):
                med_res = med_scraper.search_medicines(inputs_list=input_data["Entered Input"][0],
                                                    input_type=input_data["Input Type"][0]
                                                    
                                                    )
                
            df_converter.med_data=med_res
            med_df=df_converter.med_to_df()          
            st.write(med_df)

            del med_scraper
            df_converter.med_data=None

        except Exception as e:
            st.error(f"Error during prediction or mapping: {e}")