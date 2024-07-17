# src/app/services.py

import uuid
from typing import Dict, List, Optional
from app.database import DBInterface
from app import Tire
from app.exceptions import TireValidationError, TireNotFoundError

class TireService:
    def __init__(self, db: DBInterface):
        self.db = db

    def validate_tire_data(self, tire_data: Dict[str, any]) -> None:
        required_fields = ['brand', 'tire_type', 'ratio', 'construction_type', 'width', 'wheel_diameter', 'speed_rating', 'load_index']
        for field in required_fields:
            if field not in tire_data:
                raise TireValidationError(f"Missing required field: {field}")
        
        # Type validation
        try:
            int(tire_data['width'])
            int(tire_data['wheel_diameter'])
            int(tire_data['load_index'])
        except ValueError:
            raise TireValidationError("Width, wheel_diameter, and load_index must be integers")

        if not isinstance(tire_data['brand'], str) or not isinstance(tire_data['tire_type'], str) or \
           not isinstance(tire_data['ratio'], str) or not isinstance(tire_data['construction_type'], str) or \
           not isinstance(tire_data['speed_rating'], str):
            raise TireValidationError("Brand, tire_type, ratio, construction_type, and speed_rating must be strings")

    def create_tire(self, tire_data: Dict[str, any]) -> Tire:
        self.validate_tire_data(tire_data)
        tire_id = str(uuid.uuid4())
        tire = Tire(id=tire_id, **tire_data)
        self.db.set_tire(tire)
        return tire

    def get_tire(self, tire_id: str) -> Tire:
        tire = self.db.get_tire(tire_id)
        if not tire:
            raise TireNotFoundError(f"Tire with id {tire_id} not found")
        return tire

    def update_tire(self, tire_id: str, tire_data: Dict[str, any]) -> Tire:
        existing_tire = self.db.get_tire(tire_id)
        if not existing_tire:
            raise TireNotFoundError(f"Tire with id {tire_id} not found")
        
        updated_data = {**existing_tire.to_dict(), **tire_data}
        self.validate_tire_data(updated_data)
        
        updated_tire = Tire(id=tire_id, **updated_data)
        self.db.set_tire(updated_tire)
        return updated_tire

    def delete_tire(self, tire_id: str) -> bool:
        if not self.db.get_tire(tire_id):
            raise TireNotFoundError(f"Tire with id {tire_id} not found")
        return self.db.delete_tire(tire_id)

    def get_all_tires(self) -> List[Tire]:
        return self.db.get_all_tires()