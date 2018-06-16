import unittest
from datesFromLogs_d2 import datetime, timedelta
from datesFromLogs_d2 import loglines, convert_to_datetime, time_between_shutdowns


class TestDatesFromLogs(unittest.TestCase):

    def test_convert_to_datetime(self):
        line1 = 'ERROR 2014-07-03T23:24:31 supybot Invalid user dictionary file'
        line2 = 'INFO 2015-10-03T10:12:51 supybot Shutdown initiated.'
        line3 = 'INFO 2016-09-03T02:11:22 supybot Shutdown complete.'
        self.assertEqual(convert_to_datetime(line1), datetime(2014, 7, 3, 23, 24, 31))
        self.assertEqual(convert_to_datetime(line2), datetime(2015, 10, 3, 10, 12, 51))
        self.assertEqual(convert_to_datetime(line3), datetime(2016, 9, 3, 2, 11, 22))


    def test_time_between_events(self):
        diff = time_between_shutdowns(loglines)
        self.assertEqual(type(diff), timedelta)
        self.assertEqual(str(diff), '0:03:31')


if __name__ == '__main__':
    unittest.main()
