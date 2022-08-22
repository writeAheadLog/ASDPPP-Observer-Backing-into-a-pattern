from base.clock_observer import ClockObserver
from base.time_source import TimeSource


class MockTimeSink(ClockObserver):
    def __init__(self, source: TimeSource):
        self.__its_source = source
        self.__its_hours = None
        self.__its_minutes = None
        self.__its_seconds = None

    def get_hours(self) -> int:
        return self.__its_hours

    def get_minutes(self) -> int:
        return self.__its_minutes

    def get_seconds(self) -> int:
        return self.__its_seconds

    def update(self):
        self.__its_hours = self.__its_source.get_hours()
        self.__its_minutes = self.__its_source.get_minutes()
        self.__its_seconds = self.__its_source.get_seconds()
