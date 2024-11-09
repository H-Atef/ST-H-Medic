from ai_model_auth import API_KEY

import os

from groq import Groq

client = Groq(
    api_key=API_KEY,
)

# Example symptom input
input_list = ["Sneezing", "Runny nose", "Sore throat", "Cough"]

# Join the list of symptoms into a single string (space-separated)
input_string = " ".join(input_list)

symptoms=[
    "Dry cough Shortness of breath",     
    "Headache Fever Nausea",             
    "Fatigue Dry cough Shortness of breath"  ,
    input_string
]

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "I want a list of top 5 disease with percentage for the following " +
            f"list of symptoms: {symptoms} for each string of the list represent a case so do that "+
            "for each case and just return the list only and I WANT THE OUTPUT IN A LIST OF LISTS OF Tuples"+
            "don't give brief explaination just code",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)