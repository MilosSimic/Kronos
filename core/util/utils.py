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
	return datetime.now().strftime(code)

def end_values(year, month):
	return calendar.monthrange(year, month)

def get_weekday_number():
	return datetime.datetime.today().weekday()

def week_of_month():
	testdate = datetime.datetime.now()
	return (testdate.day+7-1)/7

def day_of_week():
	return datetime.now().strftime("%a")

def month_of_year():
	return datetime.now().strftime("%b")

def calculate_today_data():
	testdate = datetime.now()

	week_num = (testdate.day+7-1)/7
	day = testdate.strftime("%a")
	month = testdate.strftime("%b")
	#hour = testdate.strftime("%H")
	#mins = testdate.strftime("%M")

	return (week_num, day, month, testdate.today())

def decide_timedelta(amount, value):
	if value in 'minutes':
		return timedelta(minutes=amount)
	else:
		return timedelta(hours=amount)

def calendar_detail(year, month):
	return calendar.monthcalendar(year, month)

def week_count(year, month):
	detail = calendar_detail(year, month)

	return len(detail)

	