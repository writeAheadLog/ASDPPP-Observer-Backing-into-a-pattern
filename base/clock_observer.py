from abc import ABCMeta, abstractmethod


class ClockObserver(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass
