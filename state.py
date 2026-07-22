from typing import TypedDict

class CampaignState(TypedDict):
    # User Input
    product: str
    audience: str
    tone: str

    # AI Generated Output
    content: str
    keywords: str
    hashtags: str
    image_prompt: str
    final_content: str