#!/usr/bin/python3

import sys

argument_list = sys.argv
goFC_File_grab = sys.argv[1]
filterFile_grab = sys.argv[2]

goFCFile = open(goFC_File_grab, "r")
filterFile = open(filterFile_grab, "r")

file_prefix = filterFile_grab[:9]

outFile = open (file_prefix + "_" + goFC_File_grab + ".txt", "w")


L = {}
for line in filterFile:
	tab_split = line.split("\t")
	GO_term = tab_split[0].strip()
	p_value = tab_split[1].strip()
	L[GO_term] = p_value


outFile.write("GO_term" + "\t" + "GO_description" + "\t" + "sum_LogFC" + "\t" + "#_of_genes" + "\t" + "p_value\n")

for line in goFCFile:
	tab_split = line.split("\t")
	GO_term_2 = tab_split[0].strip()
	if GO_term_2 in L.keys():
		outFile.write(line.rstrip("\n") + "\t" + L[GO_term_2] + "\n")


