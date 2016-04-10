from multiprocessing import Process
from time import sleep
from . import WorkerJob

class Worker(Process):
	def __init__(self, job, threadID):
		Process.__init__(self)
		self.job = job
		self.triggerStop = False
		self.threadID = threadID

	def run(self):
		while not self.triggerStop:
			if self.job.is_time_for_job():
				worker = WorkerJob(self.job, "")
				worker.start()
				worker.join()
			else:
				print 'sleep', self.job.description
				sleep(self.job.sleep_time())

		print "stop ", self.name