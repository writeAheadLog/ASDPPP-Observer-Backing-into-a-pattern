from base.clock_observer import ClockObserver


class Subject:
    def __init__(self):
        self.__its_observer = list()

    def register_observer(self, observer: ClockObserver):
        self.__its_observer.append(observer)

    def notify_observers(self):
        for observer in self.__its_observer:
            observer.update()
