import streamlit as st
import pandas as pd

def filter_data_section_content():
    st.title("Filter Retrieved Medicines Data")

    # Check if the medicine DataFrame exists in session state
    if 'med_df' in st.session_state and st.session_state.med_df is not None:
        med_df = st.session_state.med_df

        # Check if 'Active Ingredient' and 'Disease' columns exist
        if 'Active Ingredient' in med_df.columns and 'Disease' in med_df.columns:
            # Display a summary of the DataFrame
            st.write("### Summary of Retrieved Medicines Data:")
            st.write(f"Total number of records: {len(med_df)}")
            st.write(f"Total number of unique diseases: {med_df['Disease'].nunique()}")
            st.write(f"Total number of unique active ingredients: {med_df['Active Ingredient'].nunique()}")
            st.write(f"Total number of unique drug classes: {med_df['Drug Class'].nunique()}")
            
            # Display a few rows of the dataset as a preview
            st.write("### Preview of Data:")
            st.write(med_df.head())

            # Display statistics 
            st.write("### Statistics:")
            disease_count = med_df['Disease'].value_counts()
            actv_ing_count = med_df['Active Ingredient'].value_counts()
            drug_class_count = med_df['Drug Class'].value_counts()

            # medicines count for each disease
            st.write("Medicines Count For Each Disease:")
            st.write(disease_count.head())

            # Show top active ingredients
            st.write("Top Active Ingredients:")
            st.write(actv_ing_count.head())

            # Show top drug classes
            st.write("Top  Drug Classes:")
            st.write(drug_class_count.head())

            # Create a multiselect for active ingredients
            actv_ing_options = med_df['Active Ingredient'].unique()
            selected_actv_ing = st.multiselect(
                "Select Active Ingredients", 
                options=actv_ing_options,
                default=actv_ing_options.tolist()[:4]  # Set default to first 4 options
            )

            # Determine if there is more than one unique disease
            disease_options = med_df['Disease'].unique()

            # Conditionally show the Disease multiselect only if there are multiple diseases
            if len(disease_options) > 1:
                selected_diseases = st.multiselect(
                    "Select Diseases", 
                    options=disease_options,
                    default=disease_options.tolist() # Set default to all options
                )
            else:
                # If there's only one disease, show the disease as text (non-selectable)
                selected_diseases = disease_options.tolist()
                st.write(f"Only one disease available: {selected_diseases[0]}")

            # Filter the DataFrame based on selections
            filtered_df = med_df

            if selected_actv_ing:
                filtered_df = filtered_df[filtered_df['Active Ingredient'].isin(selected_actv_ing)]

            if selected_diseases:
                filtered_df = filtered_df[filtered_df['Disease'].isin(selected_diseases)]

            # Display the filtered DataFrame
            if not filtered_df.empty:
                st.write("### Filtered Medicines Data:")
                st.write(filtered_df)
            else:
                st.write("No data available for the selected filters.")
        else:
            st.write("The necessary columns ('Active Ingredient' and 'Disease') are not found in the data.")
    else:
        st.write("No data available. Please process the input on the Disease Prediction page first.")
