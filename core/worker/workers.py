from Queue import PriorityQueue
from ..exception import WorkerException
from . import Worker

class WorkersList(object):
	"""docstring for WorkersList"""
	def __init__(self):
		super(WorkersList, self).__init__()
		self.queue = PriorityQueue()
		self.workers = []

	def empty_queue(self):
		while not self.queue.empty():
			next_level = self.queue.get()
			print 'Processing level:', next_level.description

	def get_from_queue(self):
		return self.queue.get()

	def queue_size(self):
		return self.queue.size()

	def _collect_workers(self):
		while not self.queue.empty():
			next_job = self.queue.get()
			worker = Worker(next_job, next_job.description, next_job.description)
			self.workers.append(worker)

	def start(self):
		self._collect_workers()

		for worker in self.workers:
			worker.start()
			worker.join()

	def put_in_queue(self, job):
		self.queue.put(job)

	def stop_single_worker(self, value):
		for worker in self.workers:
			if worker.name == value or worker.threadID == value:
				worker.triggerStop = False
				break
		else:
			raise WorkerException("Worker with name/id {}".format(value))

	def stop_all_workers(self):
		for worker in self.workers:
			worker.triggerStop = False
		