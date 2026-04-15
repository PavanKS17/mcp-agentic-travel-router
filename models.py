from pydantic import BaseModel

class RecommendationRequest(BaseModel):
    member_id: str
    partner_id: str

class TravelPackage(BaseModel):
    id: str
    destination: str
    type: str  # e.g., "flight", "hotel", "cruise"
    price: float

class PartnerConfig(BaseModel):
    max_recommendations: int
    exclude_cruises: bool