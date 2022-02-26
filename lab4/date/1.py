import datetime

five_days_ago = datetime.datetime.now() - datetime.timedelta(5)
print('five days ago was:', five_days_ago.strftime('%d-%m-%Y'))
