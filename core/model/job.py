class Job(object):
	"""docstring for Job"""
	def __init__(self, description, url, schedule=None, priority=1, security="", target="", sync=False):
		self.description = description
		self.url = url
		self.schedule = schedule
		self.priority = priority
		self.security = security
		self.target = target
		self.sync = sync

	def do_job(self):
		self.schedule.execute(self.security, self.target, self.url)

	def is_time_for_job(self):
		return self.schedule.is_time_for_job()

	def __str__(self):
		return repr("Desc {}, URL {}, Schedule {}, Priority {}, Security {}, Target {}, Sync {}"
			.format(self.description, self.url, self.schedule, self.priority, self.security, self.target, self.sync))

	def __cmp__(self, other):
		return cmp(self.priority, other.priority)