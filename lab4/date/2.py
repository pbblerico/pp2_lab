import datetime

yesterday = (datetime.datetime.now() - datetime.timedelta(1)).strftime('%d-%m-%Y')
today = datetime.datetime.now().strftime('%d-%m-%Y')
tomorrow = (datetime.datetime.now() + datetime.timedelta(1)).strftime('%d-%m-%Y')

print('yesterday: {}\ntoday: {}\ntomorrow: {}'.format(yesterday, today, tomorrow))

