import os
import anthropic
import day03_lists


def call_llm(prompt: str) -> str:
    """Call Anthropic messages API and return the assistant text."""
    # Use keyword-only argument for api_key (constructor is keyword-only)
    client = anthropic.Client(api_key=os.getenv("ANTHROPIC_API_KEY"))

    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=256,
        messages=[{"role": "user", "content": prompt}],
    )

    # Extract response text (safe fallback if structure differs)
    try:
        return response.content[0].text
    except Exception:
        return str(response)


def safe_call_llm(prompt: str) -> str:
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


if __name__ == "__main__":
    documents = [
        "cloud computing software industry",
        "LangChain helps build LLM applications",
    ]
    ai_analysis_results = analyse_with_ai(documents)
    for i, res in enumerate(ai_analysis_results):
        print(f"Document {i+1}:\n\t Text: {res['text']}\n\t AI Insights: {res['AI_Insights']}\n")
