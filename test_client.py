import requests
import json

API_URL = "http://127.0.0.1:8000/mcp/get_recommendations"

def test_api():
    print("--- Testing Partner A (Strict Rules: Max 2, No Cruises Allowed) ---")
    req_a = {"member_id": "member_123", "partner_id": "partner_A"}
    res_a = requests.post(API_URL, json=req_a)
    print(json.dumps(res_a.json(), indent=2))

    print("\n--- Testing Partner B (Relaxed Rules: Max 5, Cruises Allowed) ---")
    req_b = {"member_id": "member_123", "partner_id": "partner_B"}
    res_b = requests.post(API_URL, json=req_b)
    print(json.dumps(res_b.json(), indent=2))

if __name__ == "__main__":
    test_api()