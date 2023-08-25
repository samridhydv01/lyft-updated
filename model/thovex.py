from abc import ABC
from car import Car
from engine.capulet_engine import CapuletEngine 
from battery.nubbin_battery import NubbinBattery

class Thovex(CapuletEngine,NubbinBattery,Car,ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        Car.__init__()
        CapuletEngine.__init__(current_mileage, last_service_mileage)
        NubbinBattery.__init__(last_service_date)
    def needs_service(self):
        if self.battery_service() or self.engine_service():
            return True
        else:
            return False
