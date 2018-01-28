#! /usr/bin/env python3
import datetime

__version__ = '0.0.1.dev'


def worked():
    print("Mo Tu We Th Fr Sa Su")
    day = datetime.datetime.today().replace(day=1)
    month = day.month
    week_index = day.weekday()
    print("   " * week_index, end='')
    while day.month == month:
        print("{:>2} ".format(day.day), end='')
        day = day + datetime.timedelta(days=1)
        week_index += 1
        if week_index == 7:
            print()
            week_index = 0
    print()
