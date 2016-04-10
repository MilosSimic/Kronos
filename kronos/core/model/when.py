class When(object):
	"""docstring for When"""
	def __init__(self, *time):
		self.time = time

	def __str__(self):
		return repr(self.time)
		