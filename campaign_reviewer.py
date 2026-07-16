from LLM import llm

def review_campaign(state):

    content = state["content"]
    seo = state["keywords"]
    image = state["image_prompt"]

    prompt = f"""
    You are a senior digital marketing manager.

    Review the following campaign.

    Content:
    {content}

    SEO:
    {seo}

    Image Prompt:
    {image}

    Improve the campaign if needed and give the final version.
    """

    result = llm.invoke(prompt)

    state["final_content"] = result.content

    return state