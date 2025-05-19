import openai 
import os
import pandas as pd

openai.api_key = os.environ.get("OPENAI_API_KEY") #Using direct openai module
df = pd.read_csv("/Users/pragati-devhub/Downloads/machine-readable-business-employment-data-dec-2024-quarter.csv") 


def anlyseData(df):
    response = openai.Completion.create(
          model = "gpt-4o",
          message = [{"role": "user", "content":f"You are research assistent. Provide key insight from {df} in point form"}],
          temperature = 0.2,
          max_tokens = 300
    )

    return response.choices[0].message.content

print(anlyseData(df))