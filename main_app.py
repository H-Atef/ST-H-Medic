import streamlit as st
import app_sections.main_section as main_section
import app_sections.how_to_use_section  as how_to_use_section
import app_sections.data_stats_section as data_stats_section
import app_sections.search_med_section as search_med_section




page = st.sidebar.radio("Choose a page", ["ST/H-Medic Main", 
                                          "Medicine Data Stats.",
                                          "Search Medicine",
                                          "How To Use The App",
                                          "About"])


if page == "ST/H-Medic Main":
    main_section.main_section_content()

elif page == "Medicine Data Stats.":
    data_stats_section.data_stats_section_content()

elif page == "Search Medicine":
    search_med_section.search_med_section_content()

elif page == "How To Use The App":
    how_to_use_section.how_to_use_app_section_content()
   
