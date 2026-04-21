from typing import List
from models import TravelPackage, PartnerConfig

def filter_by_category(packages: List[TravelPackage], config: PartnerConfig) -> List[TravelPackage]:
    if config.exclude_cruises:
        return [pkg for pkg in packages if pkg.type != "cruise"]
    return packages

def enforce_capacity_limit(packages: List[TravelPackage], config: PartnerConfig) -> List[TravelPackage]:
    return packages[:config.max_recommendations]

def apply_partner_rules(packages: List[TravelPackage], config: PartnerConfig) -> List[TravelPackage]:
    # Filter out restricted categories entirely
    filtered = filter_by_category(packages, config)
    
    # Enforce UI capacity limits
    final_list = enforce_capacity_limit(filtered, config)
    
    return final_list