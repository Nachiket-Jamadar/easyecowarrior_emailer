import requests
import os
import json
def get_gemini_response(prompt, temp, max_op_tokens):

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": os.getenv('GEMINI_API_KEY')   # Replace with your API key
    }
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ],
        "generationConfig": {
            "maxOutputTokens": max_op_tokens,
            "temperature": temp,
            "topP": 0.9
        }
    }

    return requests.post(url, headers=headers, data=json.dumps(data))