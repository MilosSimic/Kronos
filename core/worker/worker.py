from threading import Lock, Thread
from time import sleep

LOCK = Lock()

class Worker(Thread):
	def __init__(self, job, name, threadID, isdaemon=False, nap_time=1):
		Thread.__init__(self)
		self.setDaemon(isdaemon)
		self.nap_time = nap_time
		self.job = job

	'''
		When the run() method returns (or sys.exit() is called in the thread), 
		the thread will be destroyed. All threads in a program must be destroyed before the program terminates. 
		The program will still be running as long as there is one running thread.
	'''
	def run(self):
		while True:
			if job.is_time_for_job():
				LOCK.acquire()
				job.do_job()
				LOCK.release()
			else:
				sleep(self.nap_time)
