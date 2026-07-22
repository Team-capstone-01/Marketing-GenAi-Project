from LLM import generate_response

def review_campaign(state):

    # Read outputs from previous agents
    content = state["content"]
    keywords = state["keywords"]
    hashtags = state["hashtags"]
    image_prompt = state["image_prompt"]

    # Review prompt
    prompt = f"""
You are a Senior Digital Marketing Manager.

Review the complete marketing campaign below.

LinkedIn Content:
{content}

SEO Keywords:
{keywords}

Hashtags:
{hashtags}

Image Prompt:
{image_prompt}

Review the campaign and improve it if necessary.

Check for:
- Grammar and spelling
- Professional tone
- Marketing effectiveness
- Call-to-action (CTA)
- SEO optimization
- Brand consistency
- Readability
- Audience engagement

Return the final improved campaign in a clear and professional format.
"""

    try:
        # Generate reviewed campaign
        final_campaign = generate_response(prompt)

        # Save final output
        state["final_content"] = final_campaign

    except Exception as e:
        state["final_content"] = f"Campaign Review Failed: {str(e)}"

    return state