from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from core.database import get_db
from schemas.simulation_schema import SimulationCreate, SimulationResponse
from services.simulation_service import SimulationService

router = APIRouter(prefix="/simulations", tags=["Simulations"])

@router.post("/", response_model=SimulationResponse, status_code=status.HTTP_201_CREATED)
def create_simulation(simulation: SimulationCreate, db: Session = Depends(get_db)):
    return SimulationService.create_simulation(db, simulation)

@router.get("/", response_model=list[SimulationResponse])
def list_simulations(db: Session = Depends(get_db)):
    return SimulationService.get_all_simulations(db)
