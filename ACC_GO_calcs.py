#!/usr/bin/python3

# ACC_GO_calcs.py version 0.1
# This script is used to calculate the logFC of GOs taking as input the list of DAVID conversions ACC to david id
# Then atribbute to each david id in david_chart.txt an acc
# and lastly, sum the respective acc logFC displayed in named_genes_* resulting in the sum of the genes of a given GO.

import sys
from collections import OrderedDict


argument_list = sys.argv

#Fetch the correspondence file between david id and acc's.

david_to_acc_File_grab = sys.argv[1]

#Fetch david chart file with pvalues, etc...

david_chartFile = sys.argv[2]


#Fetch the named_genes_* file generated in gene_naming.py
namedFile_grab = sys.argv[3]

# give a name for the output file
outFilename = sys.argv[4]

#Block to open and read files and output files.
accFile = open(david_to_acc_File_grab, "r")
chartFile = open(david_chartFile, "r")
namedFile = open(namedFile_grab, "r")
outFile = open (outFilename + ".txt", "w")

# do a correspondence of acc and david ids
next(accFile)
ACC_dic = {}

for line in accFile:
	tab_split = line.split("\t")
	ACC = tab_split[0].strip()
	DavidID = tab_split[1].strip()
	ACC_dic[DavidID] = ACC

#print(ACC_dic["Q90474"])

# for each acc store a logFC
next(namedFile)
logFC_dic = {}

# creates a dictionary of logFC given a ACC.
for line in namedFile:
		tab_split = line.split("\t")
		logFC = tab_split[1].strip()
		ACC_2 = tab_split[6].strip()
		logFC_dic[ACC_2] = logFC

##
next(chartFile)
GOdic = {}

for line in chartFile:
	if line.startswith("GOTERM"):
		logFCList = []
		tab_split = line.split("\t")
		GO_term = tab_split[1].strip().split("~")[0] + "\t" + tab_split[1].strip().split("~")[1]
		for element in tab_split[5].split(","):
			gene = element.strip()
			logFC_gene = logFC_dic[ACC_dic[gene]]
			logFCList.append(float(logFC_gene))
		logFC_sum = sum(logFCList)
		lenght_logFCList = len(logFCList)
		GOdic[GO_term] = logFC_sum, lenght_logFCList
		print(GO_term)
		print(logFC_sum)

print(GOdic)

dic_sorted = OrderedDict(sorted(GOdic.items(), key=lambda kv: kv[1][0], reverse = True))
outFile.write("GO_term" + "\t" + "GO_description" + "\t" + "sum_LogFC" + "\t" + "#_of_genes" + "\n")
for k, v in dic_sorted.items():
		outFile.write(k + "\t" + str(v[0]) + "\t" + str(v[1]) + "\n")



