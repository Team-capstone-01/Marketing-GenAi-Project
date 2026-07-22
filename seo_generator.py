from LLM import generate_response

def generate_seo(state):

    # Read the generated LinkedIn content
    content = state["content"]

    # SEO Prompt
    prompt = f"""
You are an SEO and Digital Marketing Expert.

Analyze the following LinkedIn marketing content and generate:

1. Exactly 5 SEO keywords.
2. Exactly 5 relevant hashtags.

Return the output in the following format only.

Keywords:
keyword1, keyword2, keyword3, keyword4, keyword5

Hashtags:
#tag1 #tag2 #tag3 #tag4 #tag5

Content:
{content}
"""

    try:
        # Generate SEO response
        response = generate_response(prompt)

        # Separate keywords and hashtags
        parts = response.split("Hashtags:")

        state["keywords"] = parts[0].replace("Keywords:", "").strip()

        if len(parts) > 1:
            state["hashtags"] = parts[1].strip()
        else:
            state["hashtags"] = ""

    except Exception as e:
        state["keywords"] = ""
        state["hashtags"] = ""
        print(f"SEO Generation Error: {e}")

    return state