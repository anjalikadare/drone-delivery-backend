from pydantic import BaseModel, field_validator
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

    @field_validator("origin_lat", "destination_lat")
    @classmethod
    def validate_lat(cls, v):
        if not -90 <= v <= 90:
            raise ValueError("Latitude must be between -90 and 90")
        return v

    @field_validator("origin_lng", "destination_lng")
    @classmethod
    def validate_lng(cls, v):
        if not -180 <= v <= 180:
            raise ValueError("Longitude must be between -180 and 180")
        return v

    @field_validator("payload_type")
    @classmethod
    def validate_payload(cls, v):
        if not v.strip():
            raise ValueError("payload_type cannot be empty")
        return v.strip().lower()

class Mission(MissionCreate):
    id: int
    status: str = "pending"
