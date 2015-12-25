from textx.metamodel import metamodel_from_file
from os import path

class Kronos(object):
	"""docstring for Kronos"""
	def __init__(self, grammar='grammar/kronos.tx', kron_file='test.kronos'):
		self._meta_model = metamodel_from_file(grammar)
		self._model = self._meta_model.model_from_file(kron_file)
		self._number_of_tasks = len(self._model.jobs)

		self._process(self._model, self._number_of_tasks)

	def _process(self, model, number_of_tasks):
		pass