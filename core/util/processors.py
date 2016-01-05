from datetime import time

def every_command_processor(every_command):
	if every_command.n <= 0:
		every_command.n = 1

	every_command.unit = every_command.unit[0:-1]

def trim_ordinal(ordinal):
	if len(ordinal) > 3:
		return int(ordinal[:-2])

	return int(ordinal[:-2])

def selective_command_processor(selective_command):
	ordinal = [trim_ordinal(ordinal) for ordinal in selective_command.ordinal]
	selective_command.ordinal = ordinal

	if selective_command.monthspec:
		months = [month.capitalize() for month in selective_command.monthspec.months]
		selective_command.monthspec.months = months

	days = [days.capitalize() for days in selective_command.days]
	selective_command.days = days

def priority_command_processor(job_command):
	if job_command.level <= 0:
		job_command.level = 1

def time_command_processor(time_command):
	times = time_command.time.split(":")

	time_command.time = time(int(times[0]), int(times[1]))