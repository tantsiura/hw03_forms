import datetime


def year(request):
    today = datetime.date.today()
    year = str(today.year)
    return {
        'year': year,
    }
