from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def needs_service(self):
        pass
