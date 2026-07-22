from LLM import generate_response

def generate_image_prompt(state):

    # Read the generated LinkedIn content
    content = state["content"]

    # Create image prompt
    prompt = f"""
You are an expert AI Image Prompt Engineer.

Based on the following marketing content, generate a realistic and detailed image prompt for an AI image generation model.

Marketing Content:
{content}

The image prompt should include:

- Main subject
- Product placement
- Background
- Lighting
- Camera angle
- Style
- Color palette
- Mood
- Target audience

The image should look realistic, professional, and suitable for a marketing campaign.

Do not include any text, logos, captions, or watermarks in the image.
"""

    try:
        # Generate image prompt
        image_prompt = generate_response(prompt)

        # Save image prompt
        state["image_prompt"] = image_prompt

    except Exception as e:
        state["image_prompt"] = f"Image Prompt Generation Failed: {str(e)}"

    return state