from fastapi import FastAPI
from app.api.missions import router as missions_router
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Drone Delivery Backend")
app.include_router(missions_router)

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "drone-delivery-backend"}
