#!/usr/local/bin/python3

import sys
from collections import OrderedDict

argument_list = sys.argv

Fastagrab = sys.argv[1]  # Fasta file for the assembly to be used for filtering
EdgeR_grab = sys.argv[2] 	#File from edgeR that give a list of genes DE, not taking into account FDR filter
matrix_grab = sys.argv[3] 		# Matrix file is the file generated with TRINITY_HOME/util/RSEM_util/merge_RSEM_frag_counts_single_table.pl  sampleA.RSEM.isoform.results sampleB.RSEM.isoform.results ... > transcripts.counts.matrix
run_label = sys.argv[4]

FastaFile = open(Fastagrab, "r")
EdgeR_File = open(EdgeR_grab, "r")
Matrix_File = open(matrix_grab, "r")

Fastagrab_label = Fastagrab[:-2]

L=[]
next(EdgeR_File)
for line1 in EdgeR_File:
	tab_split = line1.split()
	newline1 = tab_split[0].strip()
	logFC = tab_split[1].strip()
	FDR = tab_split[-1].strip()
	if float(FDR) > 0.05 and float(logFC) > 0.9 and float(logFC) < 1.1:
		L.append(newline1)

contig_storage={}
next(Matrix_File)
for line in Matrix_File:
	tab_split = line.split()
	contig_name = tab_split[0].strip()
	if contig_name in L:
		value_18C = float(tab_split[1].strip())
		value_30C = float(tab_split[2].strip())
		dif_values = abs(value_30C - value_18C)
		sum_values = value_30C + value_18C
		if value_18C > 100 and value_30C > 100:
			contig_storage[contig_name] = dif_values
		else:
			pass
	elif contig_name not in L:
		pass
	
sorted_contig_storage = OrderedDict(sorted(contig_storage.items(), key=lambda kv: kv[1]))
print(len(sorted_contig_storage.keys()))

import csv
w = csv.writer(open(run_label + "_non_DE.csv", "w"))
for key, val in sorted_contig_storage.items():
    w.writerow([key, val])

outFile = open(run_label + "_non_DE.fas", "w")

for row in FastaFile:
	if row.startswith(">") and row[1:].split()[0] in sorted_contig_storage.keys(): #and FoldChange >= Log_FC:
		outFile.write(">%s\n" % (row[1:].split()[0]))
		counter = 0
	elif row.startswith(">") and row[1:].split()[0] not in sorted_contig_storage.keys():
		counter = 1
	elif counter == 0:
		outFile.write(row)