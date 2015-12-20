from textx.metamodel import metamodel_from_file
from os import path

if path.isfile('test.txt'):

	meta_model = metamodel_from_file('hello.tx')
	model = meta_model.model_from_file('test.kronos')

	for desc in model.descriptions:
		print desc.content
else:
	print "No valid file"