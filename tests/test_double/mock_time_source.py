from base.clock_observer import ClockObserver
from base.time_source import TimeSource


class MockTimeSource(TimeSource):
    def __init__(self):
        self.__its_observer = None

    def set_observer(self, observer: ClockObserver):
        self.__its_observer = observer

    def set_time(self, hours: int, minutes: int, seconds: int):
        self.__its_observer.update(hours, minutes, seconds)
