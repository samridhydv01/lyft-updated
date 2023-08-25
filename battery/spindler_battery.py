from datetime import datetime
from abc import ABC

class SpindlerBattery(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def battery_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date():
            return True
        else:
            return False
