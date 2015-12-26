import threading

LOCK = threading.Lock()

class Worker(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
