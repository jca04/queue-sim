from sqlalchemy import Column, Integer, String, Float
from core.database import Base

class SimulationConfig(Base):
    __tablename__ = "simulation_configs"

    simulation_config_id = Column(Integer, primary_key=True, index=True)
    arrival_rate = Column(Float, nullable=False)   # λ
    service_rate = Column(Float, nullable=False)   # μ
    servers = Column(Integer, nullable=False, default=1)
    queue_capacity = Column(Integer, nullable=False, default=10)
    description = Column(String, nullable=True)