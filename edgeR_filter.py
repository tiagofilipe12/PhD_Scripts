#!/usr/bin/python3

# This script filters any fasta file, with the contigs that proved
# to be differently expressed between pairs of libraries (from EdgeR output).
# The resulting output provides a fasta to use for BLAST purposes, namely
# to use in Blast2GO.
# This is version 2 of this script and it was added a function to filter the
# FDR values from the EdgeR_File. Default FDR value is 0.05.

import sys

argument_list = sys.argv

Fastagrab = sys.argv[1]
EdgeR_grab = sys.argv[2]
File_ext = sys.argv[3]

FastaFile = open(Fastagrab, "r")
EdgeR_File = open(EdgeR_grab, "r")
next(EdgeR_File)

outFile = open ("Filtered_EdgeR_2" + File_ext +".fasta", "w")

L=[]
for line1 in EdgeR_File:
	tab_split = line1.split()
	newline1 = tab_split[0].strip()
	logFC = tab_split[1].strip()
	FDR = tab_split[-1].strip()
	if float(FDR) < 0.0005:	#Feel free to change FDR value
		if abs(float(logFC)) > 0.58:
			L.append(newline1)
	else:
		pass

print("\n# of contigs with FDR < 0.0005")
print(len(L))
print("Please confirm with grep '>' Filtered_EdgeR_2" + File_ext + ".fasta | wc -l")		
counter = 0
for line in FastaFile:
	if line.startswith(">") and line[1:].split()[0] in L:
		outFile.write(">%s\n" % (line[1:].split()[0]))
		counter = 0
	elif line.startswith(">") and line[1:].split()[0] not in L:
		counter = 1
	elif counter == 0:
		outFile.write(line)

print ("\nFinished")
