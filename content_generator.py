from LLM import generate_response

def generate_content(state):

    # Get user details
    product = state["product"]
    audience = state["audience"]
    tone = state["tone"]

    # Create prompt
    prompt = f"""
You are an experienced digital marketing expert.

Create a professional LinkedIn post using the following details.

Product: {product}
Target Audience: {audience}
Tone: {tone}

Instructions:
- Start with an attention-grabbing opening.
- Explain the product benefits clearly.
- Use a natural and human-like writing style.
- Keep the post between 120 and 180 words.
- End with a strong call-to-action.
- Make it suitable for LinkedIn.
"""

    try:
        content = generate_response(prompt)
        state["content"] = content

    except Exception as e:
        state["content"] = f"Content generation failed: {str(e)}"

    return state