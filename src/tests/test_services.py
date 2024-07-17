# src/tests/test_services.py

import pytest
from unittest.mock import Mock
from app.services import TireService
from app.models import Tire

@pytest.fixture
def mock_db():
    return Mock()

@pytest.fixture
def tire_service(mock_db):
    return TireService(mock_db)

def test_create_tire(tire_service, mock_db):
    tire_data = {
        "brand": "Michelin",
        "tire_type": "All-Season",
        "ratio": "65",
        "construction_type": "R",
        "width": 205,
        "wheel_diameter": 16,
        "speed_rating": "H",
        "load_index": 95
    }
    
    created_tire = tire_service.create_tire(tire_data)
    
    assert isinstance(created_tire, Tire)
    assert created_tire.brand == "Michelin"
    assert created_tire.tire_type == "All-Season"
    assert created_tire.ratio == "65"
    assert created_tire.construction_type == "R"
    assert created_tire.width == 205
    assert created_tire.wheel_diameter == 16
    assert created_tire.speed_rating == "H"
    assert created_tire.load_index == 95
    
    mock_db.set_tire.assert_called_once()

def test_get_tire(tire_service, mock_db):
    mock_tire = Tire(id="123", brand="Goodyear", tire_type="Winter", ratio="55", 
                     construction_type="R", width=225, wheel_diameter=17, 
                     speed_rating="T", load_index=97)
    mock_db.get_tire.return_value = mock_tire
    
    retrieved_tire = tire_service.get_tire("123")
    
    assert retrieved_tire == mock_tire
    mock_db.get_tire.assert_called_once_with("123")

def test_update_tire(tire_service, mock_db):
    existing_tire = Tire(id="123", brand="Goodyear", tire_type="Winter", ratio="55", 
                         construction_type="R", width=225, wheel_diameter=17, 
                         speed_rating="T", load_index=97)
    mock_db.get_tire.return_value = existing_tire
    
    update_data = {"brand": "Pirelli", "tire_type": "Summer"}
    updated_tire = tire_service.update_tire("123", update_data)
    
    assert updated_tire.id == "123"
    assert updated_tire.brand == "Pirelli"
    assert updated_tire.tire_type == "Summer"
    assert updated_tire.ratio == "55"  # Unchanged
    mock_db.set_tire.assert_called_once()

def test_delete_tire(tire_service, mock_db):
    mock_db.delete_tire.return_value = True
    
    result = tire_service.delete_tire("123")
    
    assert result is True
    mock_db.delete_tire.assert_called_once_with("123")

def test_get_all_tires(tire_service, mock_db):
    mock_tires = [
        Tire(id="1", brand="Michelin", tire_type="All-Season", ratio="65", 
             construction_type="R", width=205, wheel_diameter=16, 
             speed_rating="H", load_index=95),
        Tire(id="2", brand="Goodyear", tire_type="Winter", ratio="55", 
             construction_type="R", width=225, wheel_diameter=17, 
             speed_rating="T", load_index=97)
    ]
    mock_db.get_all_tires.return_value = mock_tires
    
    retrieved_tires = tire_service.get_all_tires()
    
    assert retrieved_tires == mock_tires
    mock_db.get_all_tires.assert_called_once()