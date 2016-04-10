from schedule import Schedule
from datetime import datetime, timedelta, date
from ..util import calculate_today_data, day_of_week, decide_timedelta
from ..util import get_times_from_every_item
from ..exception import ArgsException

class Selective(Schedule):
	"""docstring for Ordinal"""
	def __init__(self, ordinal_list, days_list, when=None, apendix=None, month_list=None):
		super(Selective, self).__init__(when)

		self.ordinal_list = ordinal_list
		self.days_list = days_list
		self.month_list = month_list
		self.apendix = apendix
		self.run_times = []

		self._process_ordinal()

	def _process_time(self):
		td = decide_timedelta(self.apendix[0], self.apendix[1])
		dt1, dt2 = get_times_from_every_item(self.when)

		times = []

		#put only time, because we need to run this task every dan/month/year between the same time
		while dt1 < dt2:
			times.append(dt1.time())
			dt1 = dt1 + td

		return times

	def _process_ordinal(self):
		if len(self.when.time) == 1:
			dt1 = datetime.combine(date.today(), self.when.time[0])
			self.run_times.append(dt1.time())
		elif len(self.when.time) == 2:
			if self.apendix:
				self.run_times = self._process_time()
			else:
				raise ArgsException("Args error, someting whent wrong with apendix")
		else:
			raise ArgsException("Args error, not valid amount of time arguments")

	def execute(self, security, target, url):
		print self.__class__

	def is_time_for_job(self):
		week_num, day, month, today = calculate_today_data() #week num, day, month, today tuple
		return week_num in self.ordinal_list and day in self.days_list and today in self.run_times

	def sleep_time(self):
		# add some algorithm to calculate nap time for this kind of schedule tasks
		return 1

	def __str__(self):
		if self.month_list:
			return repr("Ordinal {}, Days {}, When {}, Months {}".format(self.ordinal_list, self.days_list, self.when, self.month_list))
		return repr("Ordinal {}, Days {}, When {}".format(self.ordinal_list, self.days_list, self.when))
		