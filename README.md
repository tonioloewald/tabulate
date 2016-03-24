# tabulate.py

Given a bunch of json files, generates data file as tab-delimited columns ready for import into Excel, SPSS, or whatever

## Background

JSON is an awesome format for quickly storing data. When used for research it has the advantage of wide support and
the flexibility to allow collected data to be changed during the course of an experiment. The downside is that typical
tools such as Excel and SPSS are not well-equipped to handle data in this format.

## Usage

You'll need some familiarity with the command-line to use this tool. If that doesn't frighten you, it's a snap.

To install, simply copy the file onto your machine and then `chmod a+x tabulate.py` to make it executable.

To use it, simply point your json files at it, so (for example) if you have tabulate.py in your home directory and a bunch 
of json files in a folder named my_data in your home directory, you would do something like:

`> ./tabulate.py my_data/*.json`

This would spit the table into your terminal window (allowing you to sanity check the results). To save the output to a file simply pipe it, e.g.

`> ./tabulate.py my_data/*.json > data_for_excel.txt`

## Note

This tool only deals with "flat file" object data, i.e. something like {"foo": "bar", "baz": 17}. Any complex values will simply be output as strings.

