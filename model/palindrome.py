from abc import ABC
from car import Car
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery

class Palindrome(SternmanEngine,SpindlerBattery,Car,ABC):
    def __init__(self, last_service_date, warning_light_is_on):
        Car.__init__()
        SternmanEngine.__init__(warning_light_is_on)
        SpindlerBattery.__init__(last_service_date)
    def needs_service(self):
        if self.battery_service() or self.engine_service():
            return True
        else:
            return False
