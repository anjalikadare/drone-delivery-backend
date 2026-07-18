from fastapi import FastAPI
from app.api.missions import router as missions_router

app = FastAPI(title="Drone Delivery Backend")
app.include_router(missions_router)

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "drone-delivery-backend"}
