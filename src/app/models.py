# src/app/models.py

from dataclasses import dataclass

@dataclass
class Tire:
    id: str
    brand: str
    tire_type: str
    ratio: str
    construction_type: str
    width: int
    wheel_diameter: int
    speed_rating: str
    load_index: int

    def to_dict(self):
        return {
            "id": self.id,
            "brand": self.brand,
            "tire_type": self.tire_type,
            "ratio": self.ratio,
            "construction_type": self.construction_type,
            "width": self.width,
            "wheel_diameter": self.wheel_diameter,
            "speed_rating": self.speed_rating,
            "load_index": self.load_index
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)