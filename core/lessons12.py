import requests
import datetime
import sys
sys.path.append('..')

my_date = datetime.date(2023, 11, 1)
while my_date.month == 11:
    date_str = my_date.strftime('%Y/%m/%d')
    my_date += datetime.timedelta(days=1)
    url =f'https://www.cbr-xml-daily.ru/archive/{date_str}/daily_json.js'
    r = requests.get(url)
    try:
        lst.append([date_str, r.json()['Valute']['USD']['Value'], r.json()['Valute']['EUR']['Value']])
    except:
        lst.append([date_str, lst[-1][1], lst[-1][2]])


print(lst)
