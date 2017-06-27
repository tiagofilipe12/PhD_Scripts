#!/usr/bin/python3

# DAVID_to_REVIGO.py version 0.1
# This script is used to generate a list of GO and p values from DAVID output chart.
# This script is still under development, but it already do what is intended to.

import sys

argument_list = sys.argv

#Fetch the topBlast file (export topblast) from blast2GO.
inFile_grab = sys.argv[1]

#Block to open and read files and output files.
inFile = open(inFile_grab, "r")
next(inFile)
outFile = open ("REVIGO_input_" + inFile_grab, "w")

#Reads topBlast and outputs a list of acc or gi
for line in inFile:	
	if line.startswith("GOTERM"):
		tab_split = line.split("\t")
		Go_term = tab_split[1].strip().split("~")[0]
		p_value = tab_split[4].strip()
		outFile.write(Go_term + "\t"+ p_value +"\n")
