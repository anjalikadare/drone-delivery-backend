from fastapi import FastAPI

app = FastAPI(title="Drone Delivery Backend")

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "drone-delivery-backend"}
    