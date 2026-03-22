"""Portfolio tracker — partnerships and integrations."""
from dataclasses import dataclass
from enum import Enum

class PartnerStatus(Enum):
    PROSPECT = "prospect"
    ACTIVE = "active"
    INTEGRATED = "integrated"

@dataclass
class Partner:
    name: str
    category: str
    status: PartnerStatus
    integration_type: str = ""
    notes: str = ""

PARTNERS = [
    Partner("Stripe", "payments", PartnerStatus.INTEGRATED, "API", "Card processing — only external dep"),
    Partner("GoDaddy", "domains", PartnerStatus.ACTIVE, "registrar", "Domain registrar"),
    Partner("Cloudflare", "cdn", PartnerStatus.INTEGRATED, "DNS/CDN", "DNS + Pages + Workers"),
    Partner("DigitalOcean", "compute", PartnerStatus.ACTIVE, "IaaS", "2 droplets"),
]
