from fastapi import FastAPI, HTTPException
from models import RecommendationRequest
from mocks import INVENTORY, MOCK_PARTNERS, MOCK_MEMBERS
from rules import apply_partner_rules

app = FastAPI(title="Agentic Travel Recommendations API")

@app.post("/mcp/get_recommendations")
async def get_recommendations(req: RecommendationRequest):
    # Fetch data from upstream services (simulated)
    if req.partner_id not in MOCK_PARTNERS:
        raise HTTPException(status_code=404, detail="Partner not found")
    if req.member_id not in MOCK_MEMBERS:
        raise HTTPException(status_code=404, detail="Member not found")

    partner_config = MOCK_PARTNERS[req.partner_id]
    
    # Execute deterministic rule engine
    safe_recommendations = apply_partner_rules(INVENTORY, partner_config)

    # Return payload to the AI Agent
    return {
        "member_id": req.member_id,
        "partner_id": req.partner_id,
        "applied_constraints": {
            "max_shown": partner_config.max_recommendations,
            "cruises_excluded": partner_config.exclude_cruises
        },
        "recommendations": safe_recommendations
    }