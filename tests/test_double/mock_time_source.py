from base.time_source import TimeSource


class MockTimeSource(TimeSource):
    def set_time(self, hours, minutes, seconds):
        self.notify(hours, minutes, seconds)
