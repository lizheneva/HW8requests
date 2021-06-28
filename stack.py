import requests
from datetime import datetime
from pprint import pprint


URL = 'https://api.stackexchange.com/2.2/questions'


def date_seconds(date):
    d = (date - datetime(1970, 1, 1))
    return int(d.total_seconds())


def params(date):
    to_date = date_seconds(date)
    from_date = to_date - 48 * 3600

    result = {
        'order': 'desc',
        'sort': 'activity',
        'tagged': 'Python',
        'site': 'stackoverflow',
        'to_date': to_date,
        'from_date': from_date,
    }

    return result

date = datetime.now()
response = requests.get(URL, params=params(date))
pprint(response.json())

