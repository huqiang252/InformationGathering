from datetime import date, timedelta

class DateRangeContainerIterable:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def __iter__(self):
        current_day = self.start_date
        while current_day < self.end_date:
            yield current_day
            current_day += timedelta(days=1)



if __name__ == '__main__':
    r1 = DateRangeContainerIterable(date(2025, 3, 1), date(2025, 3, 10))
    print(",".join(map(str,r1)))  # 2025-03-01,2025-03-02,2025-03-03,2025-03-04,2025-03-05,2025-03-06,2025-03-07,2025-03-08,2025-03-09

    print(max(r1))  # ValueError: max() arg is an empty sequence