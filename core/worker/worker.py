from multiprocessing import Process
from time import sleep

class Worker(Process):
	def __init__(self, job, threadID, isdaemon=False):
		Process.__init__(self)
		self.daemon = isdaemon
		self.job = job
		self.triggerStop = False

	def run(self):
		while not self.triggerStop:
			if self.job.is_time_for_job():
				self.job.do_job()
			else:
				sleep(self.job.sleep_time())
				print 'sleep', self.job.description

		print "stop ", self.name