from abc import ABC

class WilloughbyEngine(ABC):
    def __init__(self, current_mileage, last_service_mileage):
        # super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def engine_service(self):
        return self.current_mileage - self.last_service_mileage > 60000
