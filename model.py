from textx.metamodel import metamodel_from_file
from os import path

class Kronos(object):
	"""docstring for Kronos"""
	def __init__(self, grammar='kronos.tx', kron_file='test.kronos'):
		meta_model = metamodel_from_file(grammar)
		self.model = meta_model.model_from_file(kron_file)
		

kron = Kronos()

for job in kron.model.jobs:
	print job.desc.content
	print job.url.location
	print "every {} {}".format(job.schedule.n, job.schedule.unit)