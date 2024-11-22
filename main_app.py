import streamlit as st
import app_sections.main_section as main_section
import app_sections.how_to_use_section  as how_to_use_section
import app_sections.filter_data_section as filter_data_section




page = st.sidebar.radio("Choose a page", ["ST/H-Medic Main", "How To Use The App","Filter Data"])


if page == "ST/H-Medic Main":
    main_section.main_section_content()
  
elif page == "How To Use The App":
    how_to_use_section.how_to_use_app_section_content()
   
elif page == "Filter Data":
    filter_data_section.filter_data_section_content()