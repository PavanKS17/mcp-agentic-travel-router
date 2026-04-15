from models import TravelPackage, PartnerConfig

# Mock Database of Travel Inventory
INVENTORY = [
    TravelPackage(id="pkg_1", destination="Miami", type="flight", price=300.00),
    TravelPackage(id="pkg_2", destination="Caribbean", type="cruise", price=1200.00),
    TravelPackage(id="pkg_3", destination="Cancun", type="hotel", price=800.00),
    TravelPackage(id="pkg_4", destination="Alaska", type="cruise", price=1500.00),
    TravelPackage(id="pkg_5", destination="New York", type="flight", price=250.00),
]

# Mock Partner Configuration Service
MOCK_PARTNERS = {
    # Partner A is strict: no cruises, maximum 2 recommendations per prompt
    "partner_A": PartnerConfig(max_recommendations=2, exclude_cruises=True), 
    # Partner B is relaxed: allows cruises, shows up to 5 recommendations
    "partner_B": PartnerConfig(max_recommendations=5, exclude_cruises=False), 
}

# Mock Member Data Service
MOCK_MEMBERS = {
    "member_123": {"tier": "Gold", "history": ["Miami", "New York"]},
}