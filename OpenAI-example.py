import openai
import os
from dotenv import load_dotenv
import json

# Read API KEY from .env file
load_dotenv()

# Get API_KEY
api_key = os.getenv('OPENAI_API_KEY')

# Set up OpenAI API
openai.api_key = api_key

# Create a function to get the response in JSON format
def get_openai_response(prompt):
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=300
    )
    return completion.choices[0].message

# Example usage
user_prompt = "Give me two reasons to learn OpenAI API with Python"
response = get_openai_response(user_prompt)
print(json.dumps(json.loads(response.model_dump_json()), indent=4))

