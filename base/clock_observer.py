from abc import ABCMeta, abstractmethod


class ClockObserver(metaclass=ABCMeta):
    @abstractmethod
    def update(self, hours: int, minutes: int, seconds: int):
        pass
