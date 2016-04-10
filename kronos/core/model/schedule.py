class Schedule(object):
	"""docstring for Schedule"""
	def __init__(self, when=None):
		self.when = when

	def execute(self, security, target, url):
		print self.__class__

	def is_time_for_job(self):
		return False

	def sleep_time(self):
		return 1
		