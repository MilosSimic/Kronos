from multiprocessing import Process
from time import sleep

class WorkerJob(Process):
	def __init__(self, job, threadID):
		Process.__init__(self)
		self.job = job
		self.threadID = threadID

	def run(self):
		print self.name
		self.job.do_job()