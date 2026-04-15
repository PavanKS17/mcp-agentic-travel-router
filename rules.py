from typing import List
from models import TravelPackage, PartnerConfig

def filter_by_category(packages: List[TravelPackage], config: PartnerConfig) -> List[TravelPackage]:
    """Removes excluded categories based on partner config."""
    if config.exclude_cruises:
        return [pkg for pkg in packages if pkg.type != "cruise"]
    return packages

def enforce_capacity_limit(packages: List[TravelPackage], config: PartnerConfig) -> List[TravelPackage]:
    """Slices the recommendation list to respect the partner's maximum cap."""
    return packages[:config.max_recommendations]

def apply_partner_rules(packages: List[TravelPackage], config: PartnerConfig) -> List[TravelPackage]:
    """Orchestrates the functional pipeline of business rules."""
    # Step 1: Filter out restricted categories entirely
    filtered = filter_by_category(packages, config)
    
    # Step 2: Enforce UI capacity limits
    final_list = enforce_capacity_limit(filtered, config)
    
    return final_list