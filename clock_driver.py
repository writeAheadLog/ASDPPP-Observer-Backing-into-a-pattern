from base.clock_observer import ClockObserver
from base.time_sink import TimeSink
from base.time_source import TimeSource


class ClockDriver(ClockObserver):
    def __init__(self, source: TimeSource, sink: TimeSink):
        source.set_observer(self)
        self.__its_sink = sink

    def update(self, hours: int, minutes: int, seconds: int):
        self.__its_sink.set_time(hours, minutes, seconds)
