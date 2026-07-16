from langgraph.graph import StateGraph
from state import CampaignState

from content_generator import generate_content
from seo_generator import generate_seo
from image_prompt_generator import generate_image_prompt
from campaign_reviewer import review_campaign


#new workflow.
workflow = StateGraph(CampaignState)


#content generation step.
workflow.add_node("content", generate_content)
workflow.add_node("seo", generate_seo)
workflow.add_node("image", generate_image_prompt)
workflow.add_node("review", review_campaign)


# workflow starts.
workflow.set_entry_point("content")

workflow.add_edge("content", "seo")
workflow.add_edge("seo", "image")
workflow.add_edge("image", "review")

# ends here.
workflow.set_finish_point("review")

# Building the workflow.
app = workflow.compile()