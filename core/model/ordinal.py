from schedule import Schedule

class Selective(Schedule):
	"""docstring for Ordinal"""
	def __init__(self, ordinal_list, days_list, month_list=None, when=None):
		super(Selective, self).__init__(when)

		self.ordinal_list = ordinal_list
		self.days_list = days_list
		self.month_list = month_list

	def execute(self):
		pass

	def __str__(self):
		if self.month_list:
			return repr("Ordinal {}, Days {}, When {}, Months {}".format(self.ordinal_list, self.days_list, self.when, self.month_list))
		return repr("Ordinal {}, Days {}, When {}".format(self.ordinal_list, self.days_list, self.when))
		