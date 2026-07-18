from fastapi import APIRouter, HTTPException
from app.schemas.mission import Mission, MissionCreate

router = APIRouter(prefix="/missions", tags=["missions"])

_missions: list[Mission] = []
_next_id = 1

@router.post("/", response_model=Mission)
def create_mission(mission: MissionCreate):
    global _next_id
    new_mission = Mission(id=_next_id, **mission.model_dump())
    _missions.append(new_mission)
    _next_id += 1
    return new_mission

@router.get("/", response_model=list[Mission])
def list_missions():
    return _missions

@router.get("/{mission_id}", response_model=Mission)
def get_mission(mission_id: int):
    for m in _missions:
        if m.id == mission_id:
            return m
    raise HTTPException(status_code=404, detail="Mission not found")
