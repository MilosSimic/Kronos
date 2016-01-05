from schedule import Schedule
from datetime import datetime, timedelta, date
from ..util.utils import calculate_today_data
from ..exception.params import ArgsException

class Selective(Schedule):
	"""docstring for Ordinal"""
	def __init__(self, ordinal_list, days_list, when=None, apendix=None, month_list=None):
		super(Selective, self).__init__(when)

		self.ordinal_list = ordinal_list
		self.days_list = days_list
		self.month_list = month_list

	def _process_time(self):
		td = timedelta(self.time)

		if len(self.when.time) == 2:
			#because i can get only time, put some date just to can do timedelta
			dt1 = datetime.combine(date.today(), self.when.time[0])
			dt2 = datetime.combine(date.today(), self.when.time[1])
		else:
			raise ArgsException('Args error!No start/end time!')

		times = []

		#put only time, because we need to run this task every dan/month/year between the same time
		while dt1 <= dt2:
			dt1 = dt1 + td
			times.append(dt1.time())

		return times

	def _process_ordinal(self):
		week_num, day, month, hour, mins = calculate_today_data() #week num, day, month, hour, mins tuple

		run_times = []

		if len(self.when.times) == 1:
			run_times.append(self.when.times[0])
		elif len(self.when.times) < 0 or len(self.when.times) > 2:
			raise ArgsException("Args error, not valid amount of time arguments")

	def execute(self, security, target, url):
		pass

	def is_time_for_job(self):
		pass

	def __str__(self):
		if self.month_list:
			return repr("Ordinal {}, Days {}, When {}, Months {}".format(self.ordinal_list, self.days_list, self.when, self.month_list))
		return repr("Ordinal {}, Days {}, When {}".format(self.ordinal_list, self.days_list, self.when))
		