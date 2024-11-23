import streamlit as st
import importlib

path='app_sections.'
pl=importlib.import_module(f'{path}plotter')

def data_stats_section_content():
    st.title("ST/H-Medic: Medicine Data Stats.")

    # Check if the medicine DataFrame exists in session state
    if 'med_df' in st.session_state and st.session_state.med_df is not None:
        med_df = st.session_state.med_df

        # Check if 'Active Ingredient' and 'Disease' columns exist
        if 'Active Ingredient' in med_df.columns and 'Disease' in med_df.columns:

            # Collapsible Summary Section
            with st.expander("Summary"):
                st.write("### Summary of Retrieved Medicines Data:")
                st.write(f"Total number of records: {len(med_df)}")
                st.write(f"Total number of unique diseases: {med_df['Disease'].nunique()}")
                st.write(f"Total number of unique active ingredients: {med_df['Active Ingredient'].nunique()}")
                st.write(f"Total number of unique drug classes: {med_df['Drug Class'].nunique()}")
                
                # Display a few rows of the dataset as a preview
                st.write("### Preview of Data:")
                st.write(med_df.head())

            # Collapsible Visualizations Section
            with st.expander("Visualizations"):
                st.write("### Visualizations:")

                st.write('#### Medicines Count For Each Disease')
                # Medicines count for each disease (Pie chart using Plotly)
                fig_disease = pl.MedDataPlotter.plot_disease_count(med_df)
                st.plotly_chart(fig_disease)

                st.write('#### Active Ingredients Count')
                # Active ingredient count plot (Bar chart using Plotly)
                fig_actv_ing = pl.MedDataPlotter.plot_active_ingredient_count(med_df)
                st.plotly_chart(fig_actv_ing)

                st.write('#### Drug Classes Count')
                # Drug class count plot (Bar chart using Plotly)
                fig_drug_class = pl.MedDataPlotter.plot_drug_class_count(med_df)
                st.plotly_chart(fig_drug_class)

            # Collapsible Filter Data Section
            with st.expander("Filter Data"):
                st.write("### Filter Medicines Data:")

                # Create a multiselect for active ingredients
                actv_ing_options = med_df['Active Ingredient'].unique()
                selected_actv_ing = st.multiselect(
                    "Select Active Ingredients", 
                    options=actv_ing_options,
                    default=actv_ing_options.tolist()[:4]  # Set default to first 4 options
                )

                # Conditionally show the Disease multiselect only if there are multiple diseases
                disease_options = med_df['Disease'].unique()

                if len(disease_options) > 1:
                    selected_diseases = st.multiselect(
                        "Select Diseases", 
                        options=disease_options,
                        default=disease_options.tolist()  # Set default to all options
                    )
                else:
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
