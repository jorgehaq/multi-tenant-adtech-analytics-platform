from fastapi import FastAPI
from api.dependencies import init_dependencies
from api.config import settings


app = FastAPI(
    title="AdTech Analytics API",
    version="1.0.0"
)

init_dependencies(app)

@app.get("/health")
def health_check():
    return {"status": "ok", "environment": settings.ENVIRONMENT}