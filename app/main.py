from fastapi import FastAPI, status
from api.v1.simulation_router import router as simulation_router
from core.database import Base, engine
from core.config import settings

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Queue and Server Performance Simulator (M/M/1, M/M/c)"
)

app.include_router(simulation_router, prefix="/api/v1")

@app.get("/", tags=["Health"], status_code=status.HTTP_200_OK)
def health_check():
    return {"status": "Running 👌"}