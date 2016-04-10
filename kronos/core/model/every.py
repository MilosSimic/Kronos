from schedule import Schedule
from datetime import datetime, timedelta, date
from ..exception import ArgsException
from ..util import decide_timedelta, get_times_from_every_item
from time import sleep

class Every(Schedule):
	"""docstring for Continius"""
	def __init__(self, time, unit, when=None):
		super(Every, self).__init__(when)

		self.time = time
		self.unit = unit
		self.nap_time = decide_timedelta(self.time, self.unit)
		self.run_times = self._process_time()
		self.used = []

	def _process_time(self):
		dt1, dt2 = get_times_from_every_item(self.when)

		#put only time, because we need to run this task every dan/month/year between the same time
		times = []
		while dt1 < dt2:
			time_tuple = dt1.time().hour, dt1.time().minute
			times.append(time_tuple)
			dt1 = dt1 + self.nap_time

		return times

	def execute(self, security, target, url):
		print 'hello', self.__class__.__name__
		sleep(30)

	def is_time_for_job(self):
		tt = datetime.now().time()
		cur_time = (tt.hour, tt.minute)

		print tt, self.run_times

		if len(self.run_times) == 0:
			self.run_times.extend(self.used)

		if cur_time in self.run_times:
			self.used.append(cur_time)
			self.run_times.remove(cur_time)

			return True

		return False

	def sleep_time(self):
		tt = datetime.now().time()
		nap_time = None

		try:
			#get next colsest time to run code -> (hour, minutes)
			next_time = [p for p in self.run_times if p > (tt.hour, tt.minute)][0]
			next_time = (next_time[0]-tt.hour, next_time[1]-tt.minute)
			nap_time = timedelta(hours=next_time[0], minutes=next_time[1])

			print nap_time
		except IndexError, e:
			#if there is no more in front to run, then sleep until next day
			#because tasks of class Every tun every day form specific time to specific time
			first_time = self.run_times[0]
			#next_time = (first_time[0]-tt.hour, first_time[1]-tt.minute)
			future = timedelta(days=1, hours=first_time[0], minutes=first_time[1])
			present = timedelta(hours=tt.hour, minutes=tt.minute)
			nap_time = future - present

			print nap_time

		return nap_time.seconds #self.nap_time.seconds

	def __str__(self):
		return repr("Time {}, Unit {}, When {}".format(self.time, self.unit, self.when))
		