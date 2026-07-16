from LLM import llm

def generate_seo(state):

    # Reading the content
    content = state["content"]

    # Prompt for Gemini
    prompt = f"""
    You are an SEO expert.

    Read the following marketing content and generate:

    1. Five SEO keywords
    2. Five suitable hashtags

    Content:
    {content}

    Give the output in this format:

    Keywords:
    keyword1, keyword2, keyword3...

    Hashtags:
    #tag1 #tag2 #tag3...
    """

    #response from Gemini
    result = llm.invoke(prompt)

    # Saving SEO response
    state["keywords"] = result.content

    return state