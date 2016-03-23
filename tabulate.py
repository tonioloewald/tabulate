#!/usr/bin/env python

# By Tonio Loewald, (c) 2016
# Permission is granted to do anything you like with this file. Use at your own risk.
#
# Given a bunch of json files, generates data file as tab-delimited columns
# ready for import into Excel, SPSS, or whatever
#
# Usage
# To install, simply copy the file onto your machine and chmod a+x tabulate.py
# to make it executable.
#
# To use it, simply point your json files at it, so (for example) if you have
# tabulate.py in your home directory and a bunch of json files in a folder
# named my_data in your home directory, you would do something like:
#
# > ./tabulate.py my_data/*.json
#
# This would spit the table into your terminal view. To save the output to a file
# simply pipe it, e.g.
#
# > ./tabulate.py my_data/*.json > data_for_excel.txt

import sys
import json

# list of column names
cols = []

# rows of data
rows = []

for i in range(1, len(sys.argv)):
	file = sys.argv[i]
	ref = open(file, 'r')
	text = ref.read()
	ref.close()
	data = json.loads(text)
	keys = data.keys()
	row = []
	for k in range(len(keys)):
		key = keys[k]
		try:
			idx = cols.index(key)
		except ValueError:
			cols.append(key)
			idx = len(cols) - 1
# python doesn't allow insertion of elements at arbitrary positions in a list
# so we need to make sure it's big enough
		while(len(row) <= idx):
			row.append('')
		row[idx] = str(data[key])
	rows.append(row)

print '\t'.join(cols)
for i in range(len(rows)):
	print '\t'.join(rows[i])