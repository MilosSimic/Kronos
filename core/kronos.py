from textx.metamodel import metamodel_from_file
from os import path
from processors import every_command_processor, priority_command_processor
from model import Job, Every, Selective, When
from utils import cmp_time_string
from exceptions import LogicException

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

			if hasattr(job.priority, 'level'):
				kron_job.priority = job.priority.level

			if hasattr(job.target, 'version'):
				kron_job.target = job.target.version.name

			if hasattr(job.sync, 'value'):
				kron_job.sync = job.sync.value

			if hasattr(job.secure, 'key'):
				kron_job.secure = job.secure.key

			if hasattr(job.schedule.when, 'start') and hasattr(job.schedule.when, 'end'):
				if not cmp_time_string(job.schedule.when.start.time, job.schedule.when.end.time):
					raise LogicException("end time must be greather then start time!")

				kron_job.when = When(job.schedule.when.start.time, job.schedule.when.end.time)

			schedule = None

			if hasattr(job.schedule, 'ordinal'):
				schedule = Selective(job.schedule.ordinal, job.schedule.days)
				
				if hasattr(job.schedule.monthspec, 'months'):
					schedule.month_list = job.schedule.monthspec.months

				if hasattr(job.schedule.when, 'time'):
					kron_job.when = When(job.schedule.when.time)
			else:
				schedule = Every(job.schedule.n, job.schedule.unit)

			kron_job.schedule.append(schedule)