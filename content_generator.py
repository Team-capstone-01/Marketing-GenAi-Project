from LLM import generate_response

def generate_content(state):

    product = state["product"]
    brand_name = state["brand_name"]
    brand_target = state["brand_target"]
    audience = state["audience"]
    tone = state["tone"]

    # Create prompt
    prompt = f"""
You are a social media marketing expert.

Create an engaging LinkedIn campaign.

Brand Name: {brand_name}
Brand Target: {brand_target}
Product: {product}
Target Audience: {audience}
Tone: {tone}

Keep the content engaging, professional, and aligned with the brand's target market.
"""

    try:
        content = generate_response(prompt)
        state["content"] = content

    except Exception as e:
        state["content"] = f"Content generation failed: {str(e)}"

    return state