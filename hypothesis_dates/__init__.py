import datetime

from hypothesis.strategies import defines_strategy
from hypothesis.searchstrategy.strategies import SearchStrategy

class DateStrategy(SearchStrategy):
    def do_draw(self, data):
        return datetime.date(2010, 8, 1)

@defines_strategy
def dates():
    return DateStrategy()
