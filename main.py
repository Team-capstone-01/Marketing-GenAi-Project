from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from graph import app as graph_app

# Create FastAPI application
app = FastAPI()


# Request Model
class CampaignRequest(BaseModel):
    product: str = Field(..., min_length=1)
    brand_name: str = Field(..., min_length=1)
    brand_target: str = Field(..., min_length=1)
    audience: str = Field(..., min_length=1)
    tone: str = Field(..., min_length=1)


# API Endpoint
@app.post("/generate")
def generate_campaign(data: CampaignRequest):

    try:

        campaign = {
    "product": data.product,
    "brand_name": data.brand_name,
    "brand_target": data.brand_target,
    "audience": data.audience,
    "tone": data.tone,
    "content": "",
    "keywords": "",
    "hashtags": "",
    "image_prompt": "",
    "final_content": ""
}
        # Run LangGraph Workflow
        result = graph_app.invoke(campaign)

        return {
            "content": result["content"],
            "keywords": result["keywords"],
            "hashtags": result["hashtags"],
            "imagePrompt": result["image_prompt"],
            "review": result["final_content"],
            "status": "success"
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except TimeoutError:
        raise HTTPException(
            status_code=408,
            detail="Request timed out while generating campaign."
        )

    except PermissionError:
        raise HTTPException(
            status_code=401,
            detail="Invalid API Key."
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal Server Error: {str(e)}"
        )