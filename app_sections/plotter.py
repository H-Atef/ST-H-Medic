import plotly.express as px

class DiseasePredictionPlotter:
    @staticmethod
    def generate_bar_chart(df):
        # Shorten disease names by removing anything in parentheses
        df['Disease'] = df['Disease'].apply(lambda x: x.split('(')[0].strip() if '(' in x else x)
        df['Probability'] = df['Probability'].str.replace('%', '').astype(float).apply(lambda x:x/100)

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
