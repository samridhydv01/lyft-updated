from abc import ABC
from car import Car
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery

class Glissade(WilloughbyEngine,SpindlerBattery,Car,ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        Car.__init__()
        WilloughbyEngine.__init__(current_mileage, last_service_mileage)
        SpindlerBattery.__init__(last_service_date)
    def needs_service(self):
        if self.battery_service() or self.engine_service():
            return True
        else:
            return False
