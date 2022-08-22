from base.clock_observer import ClockObserver


class MockTimeSink(ClockObserver):
    def __init__(self):
        self.__its_hours = None
        self.__its_minutes = None
        self.__its_seconds = None

    def get_hours(self) -> int:
        return self.__its_hours

    def get_minutes(self) -> int:
        return self.__its_minutes

    def get_seconds(self) -> int:
        return self.__its_seconds

    def update(self, hours: int, minutes: int, seconds: int):
        self.__its_hours = hours
        self.__its_minutes = minutes
        self.__its_seconds = seconds
