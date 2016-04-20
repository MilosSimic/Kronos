#Kronos
Scheduled task DSL

##Instalation
Download zip or clone project on local machine, then do python setup.py install. This command should install
kronos on yout local machine in python site-packages folder. After that kronos is ready to use.

##Kronos DSL
Tasks that execute must be specified in *.kronos file, and path to that file must be in Kronos constructor.

###Definition
The core concept of Kronos DSL is Kronos rule which starts with "kronos:" keyword and contains one or more
tasks that contain all the information needed for proper task execution. Only few rules are mandatory, and the rest are optional. 
Short description (plain text, mainly for logging reasons), URL for service to be executed and the time interval for task execution must be specified.

Optionally, users can specify: 
1) priority to task execution over the others specified tasks (value of 1 is assumedif not given)
2) security key in the form of authorization and/or authentication token (empty string is assumed if not given)
3) ability to sync tasks that access shared data
4) and service version.

There can be a lot of tasks, and the best practice is to separate tasks with one empty line, and every new task to mark with "-" symbol in description part. These are recommendations, not rules and they are optional for convenient reading. It is possible to put one line comments for every task defined. These comments contain plain text, and they are ignored by the interpreter

###Tasks
Kronos use two kinds of tasks: Every and Selective.

Every rule describes tasks that executes: 
1) daily every n hours or minutes in from-to pattern 
2) in combination with synchronized rule, users can easily define pattern that repeat during whole day. 
In both cases tasks is executed in a range of n hours or minutes, but minimum amount is one minute. For shorten writing, users can use mins instead of minutes.

Every task form : 'every N (hours|mins|minutes) ["from" (time) "to" (time)]'

Example:
```
kronos:
	description: "Some random description on Every task"
	url: https://path.to.service/call
	every 2 mins from 11:46 to 11:50 

avoid from 00:00 to 23:59, use synchronized keyword -> every 2 hours synchronized
```

On the other hand, Selective rule is designed for tasks that happened, not that often, or for some more complex patterns that needs to be used. Selective rule must be defined in the form: 
(ordinal number list) (day list) (month list) (when to run).

For example, if task need to be executed at the first and the second Monday and Wednesday of September and
October at specific time, or even in from-to pattern in some range, every n hours or minutes, this rule can offer that
functionality.

This ordinal numbers can be represented via text: first, second, third etc., or in ordinal representations:
1st, 2nd, 3rd etc. Kronos is able to detect more Months, Days, and Ordinal numbers but they must be
separated with "," symbol.

Also, every keyword can be used, if they what to specify that tasks run every day, month or ordinal respecting its place of usage. If the task runs whole day, Synchronized rule can be applied here
too.

Example:

kronos:

	description: "Some random description on Selective task"

	url: https://path.to.service/call

	every ordinal mon of sep,oct,nov every 2 hours from 17:00 to 22:00

##Usage
from kronos.core import Kronos

kron = Kronos(kron_file='path_to_your_.kronos_file')

run yout python script and that's it :)

##Requires
python
textX
requests