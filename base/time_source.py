from base.clock_observer import ClockObserver


class TimeSource:
    def __init__(self):
        self.__its_observer = []

    def register_observer(self, observer: ClockObserver):
        self.__its_observer.append(observer)

    def notify(self, hours: int, minutes: int, seconds: int):
        for observer in self.__its_observer:
            observer.update(hours, minutes, seconds)