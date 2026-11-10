import re
from typing import Dict, Any, Optional

# Jurisdiction & Police Routing Database for Bharat
DISTRICT_ROUTING_TABLE = {
    "hyderabad": {
        "state": "Telangana",
        "cyber_thana": "Cyber Crime Police Station, CCPS Detective Department, Basheerbagh, Hyderabad",
        "sho_contact": "+91 40 2785 2412",
        "nodal_bank": "State Bank of India (SBI) Cyber Nodal Desk, Gunfoundry, Hyderabad",
        "emergency_dispatch_code": "TG-HYD-CYBER-01",
        "legal_aid_authority": "Telangana State Legal Services Authority (TSSLSA)"
    },
    "warangal": {
        "state": "Telangana",
        "cyber_thana": "Warangal Urban Police Commissionerate Cyber Cell, Subedari",
        "sho_contact": "+91 870 242 4100",
        "nodal_bank": "Andhra Bank / Union Bank Regional Nodal Center, Hanamkonda",
        "emergency_dispatch_code": "TG-WGL-RURAL-04",
        "legal_aid_authority": "Warangal District Legal Services Authority (DLSA)"
    },
    "delhi": {
        "state": "Delhi NCR",
        "cyber_thana": "Special Cell / IFSO Cyber Police Station, Dwarka Sector 19, New Delhi",
        "sho_contact": "+91 11 2089 2611",
        "nodal_bank": "Reserve Bank of India (RBI) Central Banking Fraud Oversight Desk, Sansad Marg",
        "emergency_dispatch_code": "DL-IFSO-CENTRAL-09",
        "legal_aid_authority": "Delhi State Legal Services Authority (DSLSA)"
    },
    "mumbai": {
        "state": "Maharashtra",
        "cyber_thana": "Cyber Police Station, Crime Branch CID, Bandra Kurla Complex (BKC), Mumbai",
        "sho_contact": "+91 22 2650 4008",
        "nodal_bank": "Bank of Baroda / ICICI Corporate Cyber Nodal Desk, BKC",
        "emergency_dispatch_code": "MH-MUM-BKC-02",
        "legal_aid_authority": "Maharashtra State Legal Services Authority"
    },
    "bengaluru": {
        "state": "Karnataka",
        "cyber_thana": "CID Cyber Crime Police Station, Carlton House, Palace Road, Bengaluru",
        "sho_contact": "+91 80 2209 4500",
        "nodal_bank": "Canara Bank / HDFC Regional Nodal Hub, MG Road, Bengaluru",
        "emergency_dispatch_code": "KA-BLR-CID-03",
        "legal_aid_authority": "Karnataka State Legal Services Authority (KSLSA)"
    }
}

class JurisdictionRouter:
    """Intelligent jurisdictional router for law enforcement and bank nodal dispatch."""
    
    def resolve_jurisdiction(self, query: str = "", pin_code: Optional[str] = None) -> Dict[str, Any]:
        query_l = query.lower()
        
        # Check by district keyword
        for dist, info in DISTRICT_ROUTING_TABLE.items():
            if dist in query_l:
                return {"matched_district": dist.capitalize(), **info}
                
        # Check PIN code prefixes (e.g., 500xxx -> Hyderabad, 506xxx -> Warangal, 110xxx -> Delhi, 400xxx -> Mumbai, 560xxx -> Bengaluru)
        if pin_code:
            clean_pin = re.sub(r'\D', '', pin_code)
            if clean_pin.startswith("500"):
                return {"matched_district": "Hyderabad", **DISTRICT_ROUTING_TABLE["hyderabad"]}
            elif clean_pin.startswith("506"):
                return {"matched_district": "Warangal", **DISTRICT_ROUTING_TABLE["warangal"]}
            elif clean_pin.startswith("110"):
                return {"matched_district": "Delhi", **DISTRICT_ROUTING_TABLE["delhi"]}
            elif clean_pin.startswith("400"):
                return {"matched_district": "Mumbai", **DISTRICT_ROUTING_TABLE["mumbai"]}
            elif clean_pin.startswith("560"):
                return {"matched_district": "Bengaluru", **DISTRICT_ROUTING_TABLE["bengaluru"]}
                
        # Default fallback to national central dispatch
        return {
            "matched_district": "National Central Dispatch",
            "state": "India",
            "cyber_thana": "National Cyber Crime Reporting Portal (1930 / I4C MHA)",
            "sho_contact": "Toll-Free 1930 / 112",
            "nodal_bank": "RBI Centralized Banking Ombudsman Nodal System",
            "emergency_dispatch_code": "IN-CENTRAL-1930",
            "legal_aid_authority": "National Legal Services Authority (NALSA)"
        }

jurisdiction_router = JurisdictionRouter()
