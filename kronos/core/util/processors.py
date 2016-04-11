from datetime import time
from const import ordinal_dict, every_dict
from kronos.core.exception import ArgsException, LogicException

def every_command_processor(every_command):
	if every_command.n < 0:
		raise LogicException("Time can be positive number > 0!")

	if every_command.n == 0:
		every_command.n = 1

	every_command.unit = every_command.unit[0:-1]

def trim_ordinal(ordinal):
	if len(ordinal) == 1 or len(ordinal) > 3:
		return ordinal_dict[ordinal]
	elif len(ordinal) > 1 or len(ordinal) <= 3:
		return int(ordinal[:-2])

def check_values_list(val_list, marker):
	for x in val_list:
		if marker in x:
			return True

	return False

def list_marker_check(val_list, marker='every', flag='days'):
	value = None

	#print check_values_list(val_list, marker), val_list, marker

	if len(val_list) > 1 and marker in val_list:
		raise ArgsException('every marker can only be used single!He replace list of days, month or ordinals!')

	if check_values_list(val_list, marker):
		value = every_dict[marker+' '+flag[:-1]]
	elif not check_values_list(val_list, marker) and flag == 'ordinal':
		value = [trim_ordinal(ordinal) for ordinal in val_list]
	else:
		value = [x.capitalize() for x in val_list]

	return value

def selective_command_processor(selective_command):
	selective_command.ordinal = list_marker_check(val_list=selective_command.ordinal, flag='ordinals')
	selective_command.months = list_marker_check(val_list=selective_command.months, flag='months')
	selective_command.days = list_marker_check(selective_command.days, flag='days')

def priority_command_processor(job_command):
	if job_command.level <= 0:
		job_command.level = 1

def time_command_processor(time_command):
	times = time_command.time.split(":")

	time_command.time = time(int(times[0]), int(times[1]))