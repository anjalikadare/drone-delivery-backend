from pydantic import BaseModel
from enum import Enum

class MissionPriority(str, Enum):
    critical = "critical"
    high = "high"
    normal = "normal"

class MissionCreate(BaseModel):
    payload_type: str
    origin_lat: float
    origin_lng: float
    destination_lat: float
    destination_lng: float
    priority: MissionPriority

class Mission(MissionCreate):
    id: int
    status: str = "pending"
