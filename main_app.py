import streamlit as st
import app_sections.main_section as main_section
import app_sections.how_to_use_section  as how_to_use_section
import app_sections.data_stats_section as data_stats_section
import app_sections.search_med_section as search_med_section
import app_sections.about_section as about_section



page_dict = {
    "ST/H-Medic Main": main_section.main_section_content,
    "Medicine Data Stats.": data_stats_section.data_stats_section_content,
    "Search Medicine": search_med_section.search_med_section_content,
    "How To Use The App": how_to_use_section.how_to_use_app_section_content,
    "About": about_section.about_section_content
}

# Sidebar to select the page
page = st.sidebar.radio("Choose a page", list(page_dict.keys()))

# Call the function corresponding to the selected page
page_dict[page]()
