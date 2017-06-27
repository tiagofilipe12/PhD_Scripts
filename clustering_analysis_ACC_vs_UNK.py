#!/usr/bin/python3

# only_ACC_clustering.py version 0.1
# Generates a cluster_output with only blasted contigs (take into account that this list is already filtered for duplicated entries contrarily to TopBlast_to_David.py)
# This script is still under development, but it already do what is intended to.

import sys

argument_list = sys.argv

#Fetch the input file cluster_output with 6 entries from clustering_analysis.py.
input_grap = sys.argv[1]
inFile = open(input_grap, "r")	

outFile = open(input_grap + "_onlyACC.txt", "w")
outFile2 = open(input_grap + "_non_annotated.txt", "w")


for line in inFile:
	tab_split = line.split("\t")
	if tab_split[1].strip() == "unknown":
		outFile2.write(line)
	else:
		outFile.write(line)

