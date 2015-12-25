import time

def cmp_time_string(str_time1, str_time2, format="%H:%M"):
	t1 = time.strptime(str_time1,format)
	t2 = time.strptime(str_time2,format)

	return t1 < t2
	