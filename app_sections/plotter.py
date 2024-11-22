import plotly.express as px

class MedDataPlotter:
    @staticmethod
    def generate_bar_chart(df):
        # Shorten disease names by removing anything in parentheses
        df['Disease'] = df['Disease'].apply(lambda x: x.split('(')[0].strip() if '(' in x else x)
        df['Probability'] = df['Probability'].str.replace('%', '').astype(float).apply(lambda x: x / 100)

        # Choose a color palette for different cases
        color_palette = ['#E03C31', '#1f77b4', '#2ca02c', '#ff7f0e', '#9467bd']  # Streamlit red + others

        fig = px.bar(
            df,
            x='Probability',
            y='Disease',
            color='Case',  # Color bars by 'Case' column
            orientation='h',  # Horizontal bar chart
            title='Disease Probability Visualization by Case',
            labels={'Probability': 'Probability (%)', 'Disease': 'Disease'},
            height=400,
            color_discrete_sequence=color_palette  # Use the custom color palette
        )

        # Update layout for better presentation
        fig.update_layout(
            xaxis=dict(
                autorange=True,
                tickformat=".1%",
                tickfont=dict(size=12, family='Arial', weight='bold'),  # Increase font size and make it bold
                title=dict(text="Probability (%)", font=dict(size=14, family='Arial', weight='bold'))  # Bold x-axis title
            ),
            yaxis=dict(
                tickfont=dict(size=12, family='Arial', weight='bold'),  # Increase font size and make it bold
                title=dict(text="Disease", font=dict(size=16, family='Arial', weight='bold'))  # Bold y-axis title
            ),
            title=dict(
                font=dict(weight='bold'),  # Make the title bold
                x=0.5  # Center title
            ),
            barmode='group',  # Group bars by 'Case'
            template='plotly_white',  # Clean white background
            hovermode='closest',  # Display details when hovering over bars
            showlegend=True,
            coloraxis_showscale=False,  # Disable the color scale legend
            legend=dict(
                font=dict(size=13, family='Arial', weight='bold')  # Bold legend labels
            )
        )

        return fig
    
    @staticmethod
    def plot_disease_count(df, color_palette=None):
        # Count medicines for each disease
        disease_count = df['Disease'].value_counts()
        shortened_disease_labels = MedDataPlotter.shorten_labels(disease_count.index)
        
        # Use the passed color palette or a default one
        color_palette = color_palette or [
                        "#E03C31", "#1f77b4", "#2ca02c", "#ff7f0e", "#9467bd", 
                        "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf",  
                        "#d62728", "#ff9896", "#98df8a", "#c5b0d5", "#c49c94"
                    ]
        
        # Plot pie chart for disease counts
        fig_disease = px.pie(
            names=shortened_disease_labels, 
            values=disease_count.values,
            color=disease_count.index,
            color_discrete_map={d: color_palette[i] for i, d in enumerate(disease_count.index)},
            labels={'value': 'Count', 'names': 'Disease'}
        )

        fig_disease.update_layout(
            font=dict(size=12, family='Arial', weight='bold'),
            margin=dict(t=40, b=40, l=40, r=40),
            width=350,  # Shrink the pie chart size
            height=350
        )
        return fig_disease

    @staticmethod
    def plot_active_ingredient_count(df, color_palette=None):
        # Count active ingredients
        actv_ing_count = df['Active Ingredient'].value_counts()
        shortened_actv_ing_labels = MedDataPlotter.shorten_labels(actv_ing_count.index)

        # Use the passed color palette or a default one
        color_palette = color_palette or [
                            "#E03C31", "#1f77b4", "#2ca02c", "#ff7f0e", "#9467bd", 
                            "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf",  
                            "#d62728", "#ff9896", "#98df8a", "#c5b0d5", "#c49c94"
                        ]

        # Plot bar chart for active ingredient counts
        fig_actv_ing = px.bar(
            x=shortened_actv_ing_labels[:10], 
            y=actv_ing_count.values[:10],
            labels={'x': 'Active Ingredient', 'y': 'Count'},
            color=shortened_actv_ing_labels[:10],
            color_discrete_map={shortened_actv_ing_labels[i]: color_palette[i] for i in range(len(shortened_actv_ing_labels[:10]))}
        )

        fig_actv_ing.update_layout(
            font=dict(size=16, family='Arial', weight='bold'),
            xaxis={'title': 'Active Ingredient', 'tickangle': 45},
            yaxis={'title': 'Count'},
            margin=dict(t=40, b=40, l=40, r=40),
            showlegend=False  # Hide legend for clarity
        )

        return fig_actv_ing

    @staticmethod
    def plot_drug_class_count(df, color_palette=None):
        # Count drug classes
        drug_class_count = df['Drug Class'].value_counts()
        shortened_drug_class_labels = MedDataPlotter.shorten_labels(drug_class_count.index)

        # Use the passed color palette or a default one
        color_palette = color_palette or [
                "#E03C31", "#1f77b4", "#2ca02c", "#ff7f0e", "#9467bd", 
                "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf",  
                "#d62728", "#ff9896", "#98df8a", "#c5b0d5", "#c49c94"
            ]

        # Plot bar chart for drug class counts
        fig_drug_class = px.bar(
            x=shortened_drug_class_labels[:10], 
            y=drug_class_count.values[:10],
            labels={'x': 'Drug Class', 'y': 'Count'},
            color=shortened_drug_class_labels[:10],
            color_discrete_map={shortened_drug_class_labels[i]: color_palette[i] for i in range(len(shortened_drug_class_labels[:10]))}
        )

        fig_drug_class.update_layout(
            font=dict(size=16, family='Arial', weight='bold'),
            xaxis={'title': 'Drug Class', 'tickangle': 45},
            yaxis={'title': 'Count'},
            margin=dict(t=40, b=40, l=40, r=40),
            showlegend=False  # Hide legend for clarity
        )

        return fig_drug_class
    
    @staticmethod
    def shorten_labels(labels, max_length=20):
        return [label if len(label) <= max_length else label[:max_length] + '...' for label in labels]
