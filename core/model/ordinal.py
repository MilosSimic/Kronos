from schedule import Schedule
from datetime import datetime, timedelta, date
from ..util.utils import calculate_today_data, day_of_week
from ..exception.params import ArgsException

class Selective(Schedule):
	"""docstring for Ordinal"""
	def __init__(self, ordinal_list, days_list, when=None, apendix=None, month_list=None):
		super(Selective, self).__init__(when)

		self.ordinal_list = ordinal_list
		self.days_list = days_list
		self.month_list = month_list
		self.apendix = apendix
		self.run_times = []
			

	def _process_time(self):
		td = decide_timedelta(self.apendix[0], self.apendix[1])

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
		if len(self.when.times) == 1:
			d1 = datetime.combine(date.today(), self.when.time[0])
			self.run_times.append(dt1.time())
		elif len(self.when.times) == 2:
			if apendix:
				self.run_times = self._process_time()
			else:
				raise ArgsException("Args error, someting whent wrong with apendix")
		else:
			raise ArgsException("Args error, not valid amount of time arguments")

	def execute(self, security, target, url):
		week_num, day, month, hour, mins = calculate_today_data() #week num, day, month, hour, mins tuple

	def is_time_for_job(self):
		pass

	def __str__(self):
		if self.month_list:
			return repr("Ordinal {}, Days {}, When {}, Months {}".format(self.ordinal_list, self.days_list, self.when, self.month_list))
		return repr("Ordinal {}, Days {}, When {}".format(self.ordinal_list, self.days_list, self.when))
		