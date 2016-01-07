from datetime import time
from const import ordinal_dict, days_dict, month_dict
from ..exception import ArgsException

def every_command_processor(every_command):
	if every_command.n <= 0:
		every_command.n = 1

	every_command.unit = every_command.unit[0:-1]

def trim_ordinal(ordinal):
	if len(ordinal) == 1 or len(ordinal) > 3:
		return ordinal_dict[ordinal]

	return int(ordinal[:-2])

def list_marker_check(val_list, marker='*'):
	value = None

	if len(val_list) > 0 and marker in val_list:
		raise ArgsException('* marker can only be used single!He replace list of days, month or ordinals!')

	if marker in val_list:
		value = month_dict[marker]
	else:
		value = [x.capitalize() for x in val_list]

	return value

def selective_command_processor(selective_command):
	ordinal = [trim_ordinal(ordinal) for ordinal in selective_command.ordinal]
	selective_command.ordinal = ordinal

	selective_command.months = list_marker_check(selective_command.months)
	selective_command.days = list_marker_check(selective_command.days)

def priority_command_processor(job_command):
	if job_command.level <= 0:
		job_command.level = 1

def time_command_processor(time_command):
	times = time_command.time.split(":")

	time_command.time = time(int(times[0]), int(times[1]))