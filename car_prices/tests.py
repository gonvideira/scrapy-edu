import datetime
import pytz

created_s = '2023-08-09 10:51:38'
created = datetime.datetime.strptime(created_s, '%Y-%m-%d %H:%M:%S').astimezone(pytz.timezone('Europe/Lisbon'))
modified = datetime.datetime.now(pytz.timezone('Europe/Lisbon'))

days = (modified - created).days

print(days)