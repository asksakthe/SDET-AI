import os
from dotenv import load_dotenv
#import anthropic
#import codes.phase01.day03_lists as day03_lists
from groq import Groq

load_dotenv()

def call_llm(prompt: str) -> str:
    """Call Groq API and return the assistant text."""
    try:
        client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama-3.3-70b-versatile",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return str(e)

# def call_llm(prompt: str) -> str:
#     """Call Anthropic messages API and return the assistant text."""
#     # Use keyword-only argument for api_key (constructor is keyword-only)
#     try:
#         client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
#     #client = anthropic.Client(api_key=os.getenv("ANTHROPIC_API_KEY"))
#     chat_completion = client.chat.completions.create(
#         messages= [
#             {
#                 "role": "user",
#                 "content": prompt,
#             }
#         ],
#         model="llama-3.3-70b-versatile",
#         )
#     # #response = client.messages.create(
#     #     model="claude-3-5-sonnet-20241022",
#     #     max_tokens=256,
#     #     messages=[{"role": "user", "content": prompt}],
#     # )

#     # Extract response text (safe fallback if structure differs)
    
#         return chat_completion.choices[0].message.content
#     except Exception as e:
#         return str(e)


def safe_call_llm(prompt: str) -> str:
    prompt = prompt + "explain in simple terms not more than 10 words"
    try:
        if not isinstance(prompt, str):
            return "Error: Prompt must be a string."
        if prompt.strip() == "":
            return "Error: Prompt cannot be empty."
        return call_llm(prompt)
    except Exception as e:
        # Prefer AnthropicError if available
        err_name = type(e).__name__
        return f"API Error ({err_name}): {e}"


def analyse_with_ai(documents):
    results = []
    for i, doc in enumerate(documents):
        prompt = f"Analyze the following document and provide insights: {doc}"
        ai_response = safe_call_llm(prompt)
        results.append({"text": doc, "AI_Insights": ai_response})
    return results
