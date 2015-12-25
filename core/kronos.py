from textx.metamodel import metamodel_from_file
from os import path
from processors import every_command_processor, priority_command_processor
from model import Job

class Kronos(object):
	"""docstring for Kronos"""
	def __init__(self, grammar='grammar/kronos.tx', kron_file='test.kronos'):
		self._meta_model = metamodel_from_file(grammar)

		self._meta_model.register_obj_processors({'Every': every_command_processor})
		self._meta_model.register_obj_processors({'Priority': priority_command_processor})

		self._model = self._meta_model.model_from_file(kron_file)
		self._number_of_tasks = len(self._model.jobs)

		self.jobs_list = []

		self._process(self._model, self._number_of_tasks)

	def _process(self, model, number_of_tasks):
		for job in model.jobs:
			kron_job = Job(job.desc.content, job.url.location.path)

			print kron_job.url
			print kron_job.description

			if hasattr(job.priority, 'level'):
				kron_job.priority = job.priority.level
				print kron_job.priority

			if hasattr(job.target, 'version'):
				kron_job.target = job.target.version.name
				print kron_job.target

			if hasattr(job.sync, 'value'):
				kron_job.sync = job.sync.value
				print kron_job.sync

			if hasattr(job.secure, 'key'):
				kron_job.secure = job.secure.key
				print kron_job.secure

			if hasattr(job.schedule, 'ordinal'):
				print job.schedule.ordinal
				print job.schedule.days
				print job.schedule.monthspec.months
				print job.schedule.when.time
			else:
				print job.schedule.when.start.time, job.schedule.when.end.time
				print job.schedule.n, job.schedule.unit

			print