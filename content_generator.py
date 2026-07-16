from LLM import llm

def generate_content(state):

    # Get user details
    product = state["product"]
    audience = state["audience"]
    tone = state["tone"]

    # Create a prompt for Gemini
    prompt = f"""
    You are a social media marketing expert.

    Write an attractive LinkedIn post for the following product.

    Product: {product}
    Target Audience: {audience}
    Tone: {tone}

    Keep the content simple, engaging and professional.
    """

    # Ask Gemini to generate the content
    result = llm.invoke(prompt)

    # Save the generated content
    state["content"] = result.content

    # Return the updated state so the nxt agent could use it
    return state