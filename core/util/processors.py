from datetime import time
from const import ordinal_dict, days_dict, month_dict
from ..exception import ArgsException

def every_command_processor(every_command):
	if every_command.n <= 0:
		every_command.n = 1

	every_command.unit = every_command.unit[0:-1]

def trim_ordinal(ordinal):
	'''if len(ordinal) == 1 or len(ordinal) > 3:
		return ordinal_dict[ordinal]

	return int(ordinal[:-2])'''

	if len(ordinal) == 1 or len(ordinal) > 3:
		return ordinal_dict[ordinal]
	elif len(ordinal) > 1 or len(ordinal) <= 3:
		return int(ordinal[:-2])

def list_marker_check(val_list, marker='*', flag='days'):
	value = None

	if len(val_list) > 1 and marker in val_list:
		raise ArgsException('* marker can only be used single!He replace list of days, month or ordinals!')

	if marker in val_list:
		if flag == 'days':
			value = days_dict[marker]
		elif flag == 'months':
			value = month_dict[marker]
		else:
			value = ordinal_dict[marker]
	elif marker not in val_list and flag == 'ordinal':
		value = [trim_ordinal(ordinal) for ordinal in val_list]
	else:
		value = [x.capitalize() for x in val_list]

	return value

def selective_command_processor(selective_command):
	'''ordinal = None
	if '*' not in selective_command.ordinal:
		ordinal = [trim_ordinal(ordinal) for ordinal in selective_command.ordinal]
	else:
		ordinal = [trim_ordinal(ordinal) for ordinal in selective_command.ordinal][0]
	selective_command.ordinal = ordinal'''

	selective_command.ordinal = list_marker_check(val_list=selective_command.ordinal, flag='ordinal')
	selective_command.months = list_marker_check(val_list=selective_command.months, flag='months')
	selective_command.days = list_marker_check(selective_command.days)

def priority_command_processor(job_command):
	if job_command.level <= 0:
		job_command.level = 1

def time_command_processor(time_command):
	times = time_command.time.split(":")

	time_command.time = time(int(times[0]), int(times[1]))