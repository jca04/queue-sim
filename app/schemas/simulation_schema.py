from pydantic import BaseModel, Field

class SimulationCreate(BaseModel):
    arrival_rate: float = Field(..., gt=0)
    service_rate: float = Field(..., gt=0)
    servers: int = Field(..., gt=0)
    queue_capacity: int = Field(..., ge=0)
    description: str | None = None

class SimulationResponse(SimulationCreate):
    simulation_config_id: int

    class Config:
        orm_mode = True
