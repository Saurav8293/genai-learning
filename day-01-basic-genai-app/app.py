import os
from dotenv import load_dotenv
from google import genai

load_dotenv(dotenv_path="../.env")

api_key = os.getenv("GOOGLE_API_KEY")
print("API KEY =", api_key) 

client = genai.Client(api_key=api_key)

response1 = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain Generative AI in one sentence."
)

response2 = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Give me a simple one example of Generative AI."
)

print(response1.text)
print("\n-----------------------\n")
print(response2.text)

