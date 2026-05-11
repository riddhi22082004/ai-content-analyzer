from fastapi import APIRouter
from pydantic import BaseModel, HttpUrl

from app.services.website_service import (
    process_website
)

router = APIRouter()


class WebsiteRequest(BaseModel):

    url: HttpUrl


@router.post("/analyze")
def analyze_website(
    request: WebsiteRequest
):

    try:

        result = process_website(
            str(request.url)
        )

        return result

    except Exception as e:

        return {

            "success": False,

            "error":
            "Internal server error"
        }