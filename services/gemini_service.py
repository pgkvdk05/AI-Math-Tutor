import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-3.1-pro-preview")


def solve_equation_with_gemini(equation):

    prompt = f"""
You are an AI Math Tutor.

Solve the algebra equation step-by-step.

Equation:
{equation}

Instructions:
- Explain each step clearly
- Show intermediate steps
- Provide final answer

Return format:

Step 1:
Step 2:
Step 3:

Final Answer:
"""

    response = model.generate_content(prompt)

    return response.text