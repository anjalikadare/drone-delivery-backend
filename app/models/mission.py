from sqlalchemy import Column, Integer, String, Float
from app.core.database import Base

class MissionDB(Base):
    __tablename__ = "missions"

    id = Column(Integer, primary_key=True, index=True)
    payload_type = Column(String, nullable=False)
    origin_lat = Column(Float, nullable=False)
    origin_lng = Column(Float, nullable=False)
    destination_lat = Column(Float, nullable=False)
    destination_lng = Column(Float, nullable=False)
    priority = Column(String, nullable=False)
    status = Column(String, default="pending")
