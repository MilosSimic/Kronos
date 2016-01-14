from textx.metamodel import metamodel_from_file
from util import every_command_processor, priority_command_processor
from util import selective_command_processor, time_command_processor
from model import Job, Every, Selective, When
from exception import LogicException
from Queue import PriorityQueue
from worker import Worker
from datetime import time, datetime

class Kronos(object):
	"""docstring for Kronos"""
	def __init__(self, grammar='grammar/kronos.tx', kron_file='test.kronos', blocking=True):
		self._meta_model = metamodel_from_file(grammar)
		self._add_processors(self._meta_model)
		self._model = self._meta_model.model_from_file(kron_file)

		self._number_of_tasks = len(self._model.jobs)
		self.queue = PriorityQueue()
		self._process(self._model)
		self.workers = []

		#self._start(self.queue, self.workers)

	def _collect_common_part(self, job, kron_job):
		if hasattr(job.priority, 'level'):
			kron_job.priority = job.priority.level

		if hasattr(job.target, 'version'):
			kron_job.target = job.target.version.name

		if hasattr(job.sync, 'value'):
			kron_job.sync = job.sync.value

		if hasattr(job.secure, 'key'):
			kron_job.security = job.secure.key

	def _create_basic_with(self, job):
		if hasattr(job.schedule.when, 'start') and hasattr(job.schedule.when, 'end'):
			if not job.schedule.when.start.time < job.schedule.when.end.time:
				raise LogicException("end time must be greather then start time!")
			else:
				return When(job.schedule.when.start.time, job.schedule.when.end.time)
		else:
			return When(time(0, 0), time(23, 59))#if from to not given go for all day

	def _collect_apendix_for_ordinal(self, job):
		apendix = []

		if hasattr(job.schedule.when, 'n'):
			apendix.append(job.schedule.when.n)

		if hasattr(job.schedule.when, 'unit'):
			apendix.append(job.schedule.when.unit)

		return apendix

	def _process(self, model):
		for job in model.jobs:
			kron_job = Job(job.desc.content, job.url.location.path)

			self._collect_common_part(job, kron_job)
			when = self._create_basic_with(job)

			if hasattr(job.schedule, 'ordinal'):
				apendix = None

				if hasattr(job.schedule.when, 'time'):
					when = When(job.schedule.when.time)
				else:
					apendix = self._collect_apendix_for_ordinal(job)
					when = When(job.schedule.when.when.start.time,
						job.schedule.when.when.end.time)

				kron_job.schedule = Selective(job.schedule.ordinal, job.schedule.days, 
					when, apendix, job.schedule.months)

			else:
				kron_job.schedule = Every(job.schedule.n, job.schedule.unit, when)

			self.queue.put(kron_job)

	def _add_processors(self, metamodel):
		metamodel.register_obj_processors({
			'Every': every_command_processor,
			'Selective': selective_command_processor,
			'Priority': priority_command_processor,
			'Time': time_command_processor})

	def empty_queue(self):
		while not self.queue.empty():
			next_level = self.queue.get()
			print 'Processing level:', next_level.description

	def get_from_queue(self):
		return self.queue.get()

	def queue_size(self):
		return self.queue.size()

	def _start(self, queue, workers):
		while not queue.empty():
			next_job = self.queue.get()
			worker = Worker(next_job, next_job.description, next_job.description)
			workers.append(worker)

		for worker in workers:
			worker.start()
			worker.join()