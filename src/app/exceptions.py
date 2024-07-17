# src/app/exceptions.py

class TireValidationError(ValueError):
    pass

class TireNotFoundError(Exception):
    pass