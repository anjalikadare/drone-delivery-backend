from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.mission import Mission, MissionCreate
from app.models.mission import MissionDB
from app.core.database import get_db

router = APIRouter(prefix="/missions", tags=["missions"])

@router.post("/", response_model=Mission)
def create_mission(mission: MissionCreate, db: Session = Depends(get_db)):
    db_mission = MissionDB(**mission.model_dump())
    db.add(db_mission)
    db.commit()
    db.refresh(db_mission)
    return db_mission

@router.get("/", response_model=list[Mission])
def list_missions(db: Session = Depends(get_db)):
    return db.query(MissionDB).all()

@router.get("/{mission_id}", response_model=Mission)
def get_mission(mission_id: int, db: Session = Depends(get_db)):
    mission = db.query(MissionDB).filter(MissionDB.id == mission_id).first()
    if not mission:
        raise HTTPException(status_code=404, detail="Mission not found")
    return mission
