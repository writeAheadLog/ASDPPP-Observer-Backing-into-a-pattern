from base.clock_observer import ClockObserver
from base.time_source import TimeSource
from time_source_implementation import TimeSourceImplementation


class MockTimeSource(TimeSource):
    def __init__(self):
        self.__ts_imp = TimeSourceImplementation()

    def set_time(self, hours, minutes, seconds):
        self.__ts_imp.notify(hours, minutes, seconds)

    def register_observer(self, observer: ClockObserver):
        self.__ts_imp.register_observer(observer)

