#! /usr/bin/env python3
import datetime
import subprocess
import termcolor

__version__ = '0.0.1.dev'


def worked():
    git = subprocess.Popen(['git', 'reflog', "--format=format:%ad",  '--date=short', '--author=tikitu'], stdout=subprocess.PIPE)
    uniq = subprocess.Popen(['sort',  '-u'], stdin=git.stdout, stdout=subprocess.PIPE)
    git.stdout.close()
    output, err = uniq.communicate()
    output = output.decode('utf-8')

    day = datetime.datetime.today()
    if day.day < 15:
        day = (day.replace(day=1) + datetime.timedelta(days=-1)).replace(day=1)
    else:
        day = day.replace(day=1)
    prefix = '{}-{:0>2}-'.format(day.year, day.month)

    days_worked = { int(d[-2:]) for d in output.split('\n') if d.startswith(prefix) }

    print(day.strftime("%B"))
    print("Mo Tu We Th Fr Sa Su")
    month = day.month
    week_index = day.weekday()
    print("   " * week_index, end='')
    while day.month == month:
        if week_index in {5, 6}:
            # weekend
            color = 'red' if day.day in days_worked else 'grey'
        else:
            color = 'green' if day.day in days_worked else 'red'
        day_string = termcolor.colored("{:>2} ".format(day.day), color)
        print(day_string, end='')
        day = day + datetime.timedelta(days=1)
        week_index += 1
        if week_index == 7:
            print()
            week_index = 0
    print()
    print()
    print('total days: {}'.format(len(days_worked)))
    print()
