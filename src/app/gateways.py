# src/app/gateways.py

import falcon
import json
from app import TireService
from app.exceptions import TireValidationError, TireNotFoundError

class TireResource:
    def __init__(self, service: TireService):
        self.service = service

    def on_get(self, req, resp, tire_id=None):
        try:
            if tire_id:
                tire = self.service.get_tire(tire_id)
                resp.media = tire.to_dict()
            else:
                tires = self.service.get_all_tires()
                resp.media = [tire.to_dict() for tire in tires]
        except TireNotFoundError as e:
            resp.status = falcon.HTTP_404
            resp.media = {"error": str(e)}
        except Exception as e:
            resp.status = falcon.HTTP_500
            resp.media = {"error": "An unexpected error occurred."}

    def on_post(self, req, resp):
        try:
            tire_data = json.loads(req.stream.read())
            tire = self.service.create_tire(tire_data)
            resp.status = falcon.HTTP_201
            resp.media = tire.to_dict()
        except TireValidationError as e:
            resp.status = falcon.HTTP_400
            resp.media = {"error": str(e)}
        except json.JSONDecodeError:
            resp.status = falcon.HTTP_400
            resp.media = {"error": "Invalid JSON in request body"}
        except Exception as e:
            resp.status = falcon.HTTP_500
            resp.media = {"error": "An unexpected error occurred."}

    def on_put(self, req, resp, tire_id):
        try:
            tire_data = json.loads(req.stream.read())
            updated_tire = self.service.update_tire(tire_id, tire_data)
            resp.media = updated_tire.to_dict()
        except TireValidationError as e:
            resp.status = falcon.HTTP_400
            resp.media = {"error": str(e)}
        except TireNotFoundError as e:
            resp.status = falcon.HTTP_404
            resp.media = {"error": str(e)}
        except json.JSONDecodeError:
            resp.status = falcon.HTTP_400
            resp.media = {"error": "Invalid JSON in request body"}
        except Exception as e:
            resp.status = falcon.HTTP_500
            resp.media = {"error": "An unexpected error occurred."}

    def on_delete(self, req, resp, tire_id):
        try:
            self.service.delete_tire(tire_id)
            resp.status = falcon.HTTP_204
        except TireNotFoundError as e:
            resp.status = falcon.HTTP_404
            resp.media = {"error": str(e)}
        except Exception as e:
            resp.status = falcon.HTTP_500
            resp.media = {"error": "An unexpected error occurred."}
