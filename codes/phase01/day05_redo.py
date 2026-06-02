import anthropic as anth
from groq import Groq
import os

def call_llm(prompt : str) -> str:  
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    #client = Groq..Client(api_key=api_key))
    response = client.chat.completions.create(
        messages = [{"role": "user","content":prompt}], 
        model = "llama-3.3-70b-versatile", 
        max_completion_tokens=8192)
    return response.choices[0].message.content

def safe_call_llm(prompt):
    try:
        if not isinstance(prompt, str):
            return "Error: Prompt must be a string."
        if prompt.strip() == "":
            return "Error: Prompt cannot be empty."
        return call_llm(prompt)
    except Exception as e:
        err_name = type(e).__name__
        return f"API Error ({err_name}): {e}"
    
def analyse_with_ai(documents):
    results = []
    for index, doc in enumerate(documents):
        prompt = f"Summarise this in exactly 5 words: {doc}"
        ai_response = safe_call_llm(prompt)
        results.append({"text": doc, "AI_insights": ai_response})
    return results
    

if __name__ == "__main__":
    documents_in = [
    "AI is transforming the software industry",
    "LangChain helps build LLM applications",
    "RAG stands for Retrieval Augmented Generation",
    "Agents can use tools to complete tasks",
    "Python is the primary language for AI engineering"
]
    answer = analyse_with_ai(documents_in)
    for i, res in enumerate(answer):
        print(f"Document {i+1}:\n\t Original_input: {res['text']}\n\t Summary: {res['AI_insights']}\n\n")

    #print(answer)