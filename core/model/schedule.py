class Schedule(object):
	"""docstring for Schedule"""
	def __init__(self, when=None):
		self.when = when

	def execute(self, security, target, url):
		pass

	def is_time_for_job(self):
		pass

	def sleep_time(self):
		pass
		