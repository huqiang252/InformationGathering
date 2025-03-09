


from datetime import timedelta,date

class DateRangeIterable:
    """An iterable that contains its own iterator object."""

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date

    def __iter__(self):
        return self

    def __next__(self):
        if self._present_day >= self.end_date:
            raise StopIteration()
        today = self._present_day
        self._present_day += timedelta(days=1)
        return today



if __name__ == '__main__':
    for day in DateRangeIterable(date(2025,3,1), date(2025,3,10)):
        print(day)

    r1 = DateRangeIterable(date(2025,3,1), date(2025,3,10))
    print(",".join(map(str, r1)))   #2025-03-01,2025-03-02,2025-03-03,2025-03-04,2025-03-05,2025-03-06,2025-03-07,2025-03-08,2025-03-09

    print(max(r1))   #2025-03-09