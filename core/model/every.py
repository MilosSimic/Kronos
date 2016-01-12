from schedule import Schedule
from datetime import datetime, timedelta, date
from ..exception import ArgsException
from ..util import decide_timedelta

class Every(Schedule):
	"""docstring for Continius"""
	def __init__(self, time, unit, when=None):
		super(Every, self).__init__(when)

		self.time = time
		self.unit = unit
		self.run_times = self._process_time()

	def _process_time(self):
		td = decide_timedelta(self.time, self.unit)

		if len(self.when.time) == 2:
			#because i can get only time, put some date just to can do timedelta
			dt1 = datetime.combine(date.today(), self.when.time[0])
			dt2 = datetime.combine(date.today(), self.when.time[1])
		else:
			raise ArgsException('Args error!No start/end time!')

		times = []

		#put only time, because we need to run this task every dan/month/year between the same time
		while dt1 < dt2:
			times.append(dt1.time())
			dt1 = dt1 + td

		return times

	def execute(self, security, target, url):
		pass

	def is_time_for_job(self):
		return datetime.now().today() in self.run_times

	def __str__(self):
		return repr("Time {}, Unit {}, When {}".format(self.time, self.unit, self.when))
		