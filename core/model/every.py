from schedule import Schedule

class Every(Schedule):
	"""docstring for Continius"""
	def __init__(self, time, unit, when=None):
		super(Every, self).__init__(when)
		
		self.time = time
		self.unit = unit
		#self.when = when

	def __str__(self):
		return repr("Time {}, Unit {}, When {}".format(self.time, self.unit, self.when))
		