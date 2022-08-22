import unittest

from tests.test_double.mock_time_sink import MockTimeSink
from tests.test_double.mock_time_source import MockTimeSource


class TestClockDriver(unittest.TestCase):
    def test_time_change(self):
        source = MockTimeSource()
        sink = MockTimeSink()
        source.set_observer(sink)
        source.set_time(3, 4, 5)
        self.assertEqual(3, sink.get_hours())
        self.assertEqual(4, sink.get_minutes())
        self.assertEqual(5, sink.get_seconds())

        source.set_time(7, 8, 9)
        self.assertEqual(7, sink.get_hours())
        self.assertEqual(8, sink.get_minutes())
        self.assertEqual(9, sink.get_seconds())


if __name__ == '__main__':
    unittest.main()
