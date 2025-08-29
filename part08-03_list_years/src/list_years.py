from datetime import date

def list_years(dates: list):
    years = []
    [years.append(date.year) for date in dates]
    years.sort()
    return years
