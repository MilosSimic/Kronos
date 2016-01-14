from core import Kronos
		

kron = Kronos()
kron.workers.empty_queue()

'''for job in kron.model.jobs:
	print job.desc.content
	print job.url.location.path

	if hasattr(job.schedule, 'ordinal'):
		print job.schedule.ordinal
		print job.schedule.days
		print job.schedule.monthspec.months
		print job.schedule.when.time
	else:
		print job.schedule.when.start.time, job.schedule.when.end.time

	print'''
