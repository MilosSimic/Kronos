
def every_command_processor(every_command):
	if every_command.n <= 0:
		every_command.n = 1

	every_command.unit = every_command.unit[0:-1]

def selective_command_processor(selective_command):
	pass

def priority_command_processor(job_command):
	if job_command.level <= 0:
		job_command.level = 1