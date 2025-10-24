from sqlalchemy.orm import Session
from models.simulation_config import SimulationConfig
from schemas.simulation_schema import SimulationCreate

class SimulationService:

    @staticmethod
    def create_simulation(db: Session, simulation_data: SimulationCreate):
        new_simulation = SimulationConfig(**simulation_data.model_dump())
        db.add(new_simulation)
        db.commit()
        db.refresh(new_simulation)
        return new_simulation

    @staticmethod
    def get_all_simulations(db: Session):
        return db.query(SimulationConfig).all()