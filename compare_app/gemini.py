# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from google import genai
from google.genai import types 
from dotenv import load_dotenv
load_dotenv()


def generate(address1, address2):
    client = genai.Client(
        api_key=os.environ.get("API_KEY"),
    )
    address_prompt =  """Can you compare these two addresses {address1} and {address2}"""
    model = "gemini-2.5-pro-preview-03-25"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=address_prompt),
            ],
        )
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config = types.ThinkingConfig(
            thinking_budget=0,
        ),
        response_mime_type="text/plain",
    )
    result = ""
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        result += chunk.text
    
    return result


