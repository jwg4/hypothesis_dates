from hypothesis import given
from hypothesis_dates import dates

import datetime
import unittest

def iso_to_gregorian(iso_year, iso_week, iso_day):
    "Gregorian calendar date for the given ISO year, week and day"
    fifth_jan = datetime.date(iso_year, 1, 5)
    _, fifth_jan_week, fifth_jan_day = fifth_jan.isocalendar()
    return fifth_jan + datetime.timedelta(days=iso_day-fifth_jan_day, weeks=iso_week-fifth_jan_week)

class TestDateConversion(unittest.TestCase):
    @given(dates())
    def test_date_conversion(d):
        assert iso_to_gregorian(datetime.isocalendar(d)) == d
