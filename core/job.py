class Job(object):
	"""docstring for Job"""
	def __init__(self, description, url, schedule, priority=1, security="", target="", sync=False):
		self.description = description
		self.url = url
		self.schedule = schedule
		self.priority = priority
		self.security = security
		self.target = target
		self.sync = sync

	def do_job(self):
		pass