from textx.metamodel import metamodel_from_file
from processors import every_command_processor, priority_command_processor
from model import Job, Every, Selective, When
from utils import cmp_time_string
from exceptions import LogicException
from Queue import PriorityQueue

class Kronos(object):
	"""docstring for Kronos"""
	def __init__(self, grammar='grammar/kronos.tx', kron_file='test.kronos'):
		self._meta_model = metamodel_from_file(grammar)

		self._meta_model.register_obj_processors({'Every': every_command_processor})
		self._meta_model.register_obj_processors({'Priority': priority_command_processor})

		self._model = self._meta_model.model_from_file(kron_file)
		self._number_of_tasks = len(self._model.jobs)

		self.queue = PriorityQueue()

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
				kron_job.security = job.secure.key

			when = None

			if hasattr(job.schedule.when, 'start') and hasattr(job.schedule.when, 'end'):
				if not cmp_time_string(job.schedule.when.start.time, job.schedule.when.end.time):
					raise LogicException("end time must be greather then start time!")
				else:
					when = When(job.schedule.when.start.time, job.schedule.when.end.time)

			if hasattr(job.schedule, 'ordinal'):
				kron_job.schedule = Selective(job.schedule.ordinal, job.schedule.days)
				
				if hasattr(job.schedule.monthspec, 'months'):
					kron_job.schedule.month_list = job.schedule.monthspec.months

				if hasattr(job.schedule.when, 'time'):
					when = When(job.schedule.when.time)
			else:
				kron_job.schedule = Every(job.schedule.n, job.schedule.unit)

			kron_job.schedule.when = when

			self.queue.put(kron_job)

		def empty_queue(self):
			while not self.queue.empty():
				next_level = self.queue.get()
				print 'Processing level:', next_level.description

		def get_from_queue(self):
			return self.queue.get()

		def queue_size(self):
			return self.queue.size()
