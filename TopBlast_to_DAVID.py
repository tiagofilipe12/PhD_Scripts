#!/usr/bin/python3

# TopBlast_to_DAVID.py version 0.1
# This script is used to generate a list of acc or gi to give as input to DAVID.
# This script is still under development, but it already do what is intended to.

import sys

argument_list = sys.argv

#Fetch the input file from edgeR with DE genes.
option_mode = sys.argv[2]		# valid inputs: acc | gi

#Fetch the topBlast file (export topblast) from blast2GO.
topBlastFile_grab = sys.argv[1]

#Block to open and read files and output files.
topBlast = open(topBlastFile_grab, "r")
if "acc" in option_mode:
	outFile = open ("David_input_acc_" + topBlastFile_grab, "w")
else:
	outFile = open ("David_input_gi_" + topBlastFile_grab, "w")

#Reads topBlast and outputs a list of acc or gi
for line in topBlast:	
	if line.startswith("Sequence"):
		pass
	else:
		tab_split = line.split("\t")
		contigName = tab_split[0].strip()
		seqName = tab_split[1].strip()
		ACC = tab_split[4].strip()
		GI_element = tab_split[3].strip()
		GI = GI_element[3:].split("|")[0]
		if "acc" in option_mode:
			outFile.write(ACC+"\n")
		else:
			outFile.write(GI+"\n")

