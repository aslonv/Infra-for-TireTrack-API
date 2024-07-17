# src/tests/test_application.py

import json

def test_create_tire(client):
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
    response = client.post("http://0.0.0.0:8080/tires", json=tire_data)
    assert response.status_code == 201
    created_tire = response.json()
    assert "id" in created_tire
    assert created_tire["brand"] == "Michelin"

def test_get_tire(client):
    # First, create a tire
    tire_data = {
        "brand": "Goodyear",
        "tire_type": "Winter",
        "ratio": "55",
        "construction_type": "R",
        "width": 225,
        "wheel_diameter": 17,
        "speed_rating": "T",
        "load_index": 97
    }
    create_response = client.post("http://0.0.0.0:8080/tires", json=tire_data)
    created_tire = create_response.json()
    
    # Now, get the tire
    response = client.get(f"http://0.0.0.0:8080/tires/{created_tire['id']}")
    assert response.status_code == 200
    assert response.json() == created_tire

def test_update_tire(client):
    # First, create a tire
    tire_data = {
        "brand": "Continental",
        "tire_type": "Summer",
        "ratio": "45",
        "construction_type": "R",
        "width": 245,
        "wheel_diameter": 18,
        "speed_rating": "Y",
        "load_index": 99
    }
    create_response = client.post("http://0.0.0.0:8080/tires", json=tire_data)
    created_tire = create_response.json()
    
    # Update the tire
    update_data = {"brand": "Pirelli"}
    response = client.put(f"http://0.0.0.0:8080/tires/{created_tire['id']}", json=update_data)
    assert response.status_code == 200
    updated_tire = response.json()
    assert updated_tire["brand"] == "Pirelli"
    assert updated_tire["tire_type"] == "Summer"  # Other fields should remain unchanged

def test_delete_tire(client):
    # First, create a tire
    tire_data = {
        "brand": "Bridgestone",
        "tire_type": "All-Terrain",
        "ratio": "70",
        "construction_type": "R",
        "width": 265,
        "wheel_diameter": 16,
        "speed_rating": "S",
        "load_index": 112
    }
    create_response = client.post("http://0.0.0.0:8080/tires", json=tire_data)
    created_tire = create_response.json()
    
    # Delete the tire
    response = client.delete(f"http://0.0.0.0:8080/tires/{created_tire['id']}")
    assert response.status_code == 204
    
    # Try to get the deleted tire
    get_response = client.get(f"http://0.0.0.0:8080/tires/{created_tire['id']}")
    assert get_response.status_code == 404

def test_get_all_tires(client):
    # Create a few tires
    tire_data_list = [
        {
            "brand": "Michelin",
            "tire_type": "All-Season",
            "ratio": "65",
            "construction_type": "R",
            "width": 205,
            "wheel_diameter": 16,
            "speed_rating": "H",
            "load_index": 95
        },
        {
            "brand": "Goodyear",
            "tire_type": "Winter",
            "ratio": "55",
            "construction_type": "R",
            "width": 225,
            "wheel_diameter": 17,
            "speed_rating": "T",
            "load_index": 97
        }
    ]
    
    for tire_data in tire_data_list:
        client.post("http://0.0.0.0:8080/tires", json=tire_data)
    
    # Get all tires
    response = client.get("http://0.0.0.0:8080/tires")
    assert response.status_code == 200
    tires = response.json()
    assert len(tires) >= 2  # There should be at least the two tires we just created
    assert any(tire["brand"] == "Michelin" for tire in tires)
    assert any(tire["brand"] == "Goodyear" for tire in tires)