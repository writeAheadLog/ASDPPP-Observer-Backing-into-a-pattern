class ClockDriver:
    def __init__(self, source, sink):
        source.set_driver(self)
        self.__its_sink = sink

    def update(self, hours, minutes, seconds):
        self.__its_sink.set_time(hours, minutes, seconds)
