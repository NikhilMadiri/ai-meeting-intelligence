from models.groq_client import generate_response

def summarize_text(text):
    text = text[:2000]  # limit for speed

    prompt = f"""
    Summarize the following meeting clearly in 4-5 sentences:

    {text}
    """

    return generate_response(prompt)