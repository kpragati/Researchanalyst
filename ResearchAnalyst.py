from openai import OpenAI
import pandas as pd

OpenAI.api_key = "API_KEY"

df = "/Users/pragati-devhub/Downloads/machine-readable-business-employment-data-dec-2024-quarter.csv"


def anlyseDate():
    response = OpenAI.chat.completion.create(
          

    )