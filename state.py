from typing import TypedDict

class CampaignState(TypedDict):
    product: str
    brand_name: str
    brand_target: str
    audience: str
    tone: str

    content: str
    keywords: str
    hashtags: str
    image_prompt: str
    final_content: str