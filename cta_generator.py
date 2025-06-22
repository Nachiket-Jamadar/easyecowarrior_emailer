from gemini_call import get_gemini_response
from ctas_list import CTAs

def cta_prompt(company_name):
    return f'''
You are an AI assistant specializing in sustainability and business operations. You will receive a company name and a list of actionable "Easy Eco Warrior" Call-To-Actions (CTAs).

**Crucially, BEFORE making any decisions, perform a thorough web search on the provided [COMPANY NAME] to understand its industry, operations, primary activities, and any relevant details about its office spaces (if applicable). Use this information to make informed decisions.**

Your task is to select the 3 MOST RELEVANT CTAs from the provided list for the given company, based on its industry, operations, and potential for environmental impact.

First, categorize the company into one of the following categories:

1. Others
2. Business to Customer Manufacturer
3. Parcel/Delivery Services
4. Restaurant/Lodging/Resort (Excluding Food Delivery)
5. Malls/Office Spaces/Stores/Shops
6. Educational Institution

If the company falls under category '1. Others' and operates office spaces, prioritize the first two CTAs that are most relevant to office housekeeping/maintenance activities. The third CTA should be chosen based on overall relevance to the company's operations and ability to reduce its environmental footprint.

For companies in categories 2-5, select the three most relevant CTAs based on their potential for significant impact on the company's operations.

**Crucially, the selected CTAs MUST be actionable by the company ITSELF. Do NOT include any CTAs that primarily rely on customer or employee participation or behavior change.**

Output ONLY the three selected CTAs in a numbered list format (1, 2, 3). Do NOT include any explanations, justifications, or additional text.

**Input Format:**

*   Company Name: [COMPANY NAME. The tool MUST perform a detailed and comprehensive web search on this name before proceeding.]
*   CTA List:
    *   [CTA 1]
    *   [CTA 2]
    *   [CTA 3]
    *   ... (all CTAs from the list)

**Example Input:**

*   Company Name: Acme Corp [The tool MUST perform a web search on "Acme Corp" before proceeding.]
*   CTA List:
    *   Use Bio Enzyme Cleaners Instead of Chemical Based Cleaners & Reuse the Water
    *   Use Natural Handwash Tablet/Powder instead of Liquid Handwash
    *   Use Natural Detergent Pods/Papers/Powder instead of Liquid Detergent & Reuse Water
    *   Switch to Paper Based Packaging Instead of Plastic Based Packaging
    *   Prefer digital notes over paper based notes
    *   ... (rest of the CTA list)

**Expected Output:**

1.  Use Bio Enzyme Cleaners Instead of Chemical Based Cleaners & Reuse the Water
2.  Use Natural Handwash Tablet/Powder instead of Liquid Handwash
3.  Prefer digital notes over paper based notes

*** Company Name: {company_name}***
*** CTAs: {CTAs}

'''

def generate_ctas(company_name):

    response = get_gemini_response(cta_prompt(company_name),1.3, 20000)


    if response.status_code == 200:
        print(response.text)
        response_json = response.json()
        cta_list = response_json['candidates'][0]['content']['parts'][0]['text']

    else:
        cta_list = response.status_code

    return cta_list