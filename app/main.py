from fastapi import FastAPI
from app.api.missions import router as missions_router
from app.api.auth import router as auth_router
from app.core.database import Base, engine
from app.models import mission, user

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Drone Delivery Backend")
app.include_router(missions_router)
app.include_router(auth_router)

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "drone-delivery-backend"}
