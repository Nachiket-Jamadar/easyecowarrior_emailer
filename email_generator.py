from prompt_generator import generate_prompt
from gemini_call import get_gemini_response

def generate_email(company_name):

    response = get_gemini_response(generate_prompt(company_name), 1, 10000)

    if response.status_code == 200:
        response_json = response.json()
        email = {}
        email_string = str(response_json['candidates'][0]['content']['parts'][0]['text'])
        email['subject'] =  email_string.split('&&')[0].strip()
        email['body'] =  email_string.split('&&')[1].strip()

        return email
    else:
        print(f"Error: {response.status_code} - {response.text}")

