from LLM import llm

def generate_image_prompt(state):

    # Read generated content
    content = state["content"]

    prompt = f"""
    You are an AI image prompt expert.

    Based on the following marketing content, create a realistic image generation prompt.

    Content:
    {content}

    The prompt should describe:
    - Background
    - Product
    - Lighting
    - Style
    - Target audience
    """

    result = llm.invoke(prompt)

    state["image_prompt"] = result.content

    return state