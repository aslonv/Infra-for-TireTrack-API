# Tire Management API

RESTful API for managing tire data, built using Falcon and Redis. The API provides endpoints to create, read, update, and delete tire information.

Implemented data validation in the service layer (validate_tire_data method) to ensure that only valid data is processed and stored, preventing errors and maintaining data integrity.

- Use of Redis for fast in-memory data operations.
- Falcon framework for high performance and low overhead.
- Containerization for easy and quick deployment.

- Concise exception handling (exceptions.py).
- Comprehensive data validation and error handling in the service layer.
- Modular design promoting code readability and maintainability.

### Prerequisites

- Docker
- Docker Compose
- Python 3.8+

Create a virtual environment and activate it:

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

### Testing

1. Install the test dependencies:

    ```sh
    pip install -r requirements-test.txt
    ```

2. Run the tests using `pytest`:

    ```sh
    pytest
    ```


## API Endpoints

### Get All Tires

 ```sh
    GET/tires
 ```

### Get a Tire by ID

```sh
    GET /tires/{tire_id}
```

### Create a Tire

```sh
    POST/tires
```

### Update a Tire

```sh
    PUT /tires/{tire_id}
```

### Delete a Tire

```sh
    DELETE /tires/{tire_id}
```
