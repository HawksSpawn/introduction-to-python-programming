def readable_timedelta(days):
    """Return a string of the number of weeks and days included in days."""

    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s).".format(weeks, remainder)

if __name__ == '__main__':
    print(readable_timedelta(10))
    print(readable_timedelta(1))
    print(readable_timedelta(6))
    print(readable_timedelta(7))
    print(readable_timedelta(9))
    print(readable_timedelta(4663))
