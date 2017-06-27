#!/usr/bin/python3

## Script to be run after cluster_analysis.py with the output from that program. This script orders the sum of logFCs from all libs do be compared with cluster_analysis.py,
## giving an ordered list of the most DEs genes.

import sys
from collections import OrderedDict

input_file = sys.argv[1]
file_handle = open(input_file)
output_file_IDs = input_file + "sums_withIDs"
output_file_noIDs = input_file + "sums_noIDs"

output_handle = open(output_file_IDs,"w")
output_handle_2 = open(output_file_noIDs,"w")


dic = {}


for line in file_handle:
	tab_split = line.split("\t")
	ACC = tab_split[0].strip()
	seqName = tab_split[1].strip()
	seqID = ACC + "\t" +seqName
	List_logFC=[]
	List_strings = []
	for item in tab_split[2:]:
		element = item.rstrip("\n")
		List_strings.append(element)
		if element == "None":
			element = 0.00
			List_logFC.append(element)
		else:
			List_logFC.append(float(element))

	logFC_sum = sum(List_logFC)
	dic[seqID] = List_strings,logFC_sum

#print(dic)

dic_sorted = OrderedDict(sorted(dic.items(), key=lambda kv: kv[1][1], reverse = True))

for k, v in dic_sorted.items():
	if k.startswith("comp"):
		output_handle_2.write(k + "\t" + "\t".join(v[0]) + "\t" + str(v[1]) + "\n")
	else:
		output_handle.write(k + "\t" + "\t".join(v[0]) + "\t" + str(v[1]) + "\n")


