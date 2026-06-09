import google.generativeai as genai

genai.configure(api_key="AQ.Ab8RN6Kc86S-Aq-huIISs7MxzZ13GfDOp0WUx1ip7PBKRwV56g")

model = genai.GenerativeModel("gemini-2.5-flash")

def get_response(question):

    prompt = f"""
    You are a professional customer support assistant.

    Rules:
    - Be polite
    - Give short answers
    - Help customers

    Customer:
    {question}
    """

    response = model.generate_content(prompt)

    return response.text