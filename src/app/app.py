# src/app/app.py

import falcon
from .gateways import TireResource
from .services import TireService
from .database import DBInterface

def create_app() -> falcon.App:
    db_interface = DBInterface()
    tire_service = TireService(db_interface)
    tire_resource = TireResource(tire_service)

    application = falcon.App()
    application.add_route('/tires', tire_resource)
    application.add_route('/tires/{tire_id}', tire_resource)

    return application