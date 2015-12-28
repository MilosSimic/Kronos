import time
from datetime import date, datetime, timedelta
import calendar

'''
	for result in perdelta(date(2011, 10, 10), date(2011, 12, 12), timedelta(days=4)):
	    print result
'''
def perdelta(start, end, delta):
	curr = start
	while curr < end:
		yield curr
		curr += delta

def cmp_time_string(str_time1, str_time2, format="%H:%M"):
	t1 = time.strptime(str_time1,format)
	t2 = time.strptime(str_time2,format)

	return t1 < t2

def get_datetime_value(code):
	return datetime.datetime.now().strftime(code)

def end_values(year, month):
	return calendar.monthrange(year, month)
	