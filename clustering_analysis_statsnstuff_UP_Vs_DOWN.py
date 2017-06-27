#!/usr/bin/python3

# Input file must be cluster_output_5 with all 6 comparisons, with annotated, non annotated contigs, and with up and down regulated genes from cluser_analysis.py
# Generates a stats file that can be imported in excel with all simple stats of DE genes in clustering analysis resulting from cluster_anaysis.py.

import sys
import os

argument_list = sys.argv

#Fetch the input file from edgeR with DE genes.
Filegrab = sys.argv[1]

#Fetch the annotation file (expot topblast) from blast2GO exported as Seq.
topBlastFile_grab = sys.argv[1]

#Block to open and read files and output files.
InFile = open(Filegrab, "r")

outFile = open ("DE_genes_stats_table_v4.txt", "w")

next(InFile)
#Construct two dictionaries of contigs as keys and SeqNames and accession numbers as answer for given keys.
number_of_contigs = 0
non_annotated = 0
annotated = 0
up_non_annotated = 0
up_annotated = 0
# lists to assign each type of logFC
logFC_1_L_ACC_UP = []
logFC_1_L_ACC_DOWN = []
logFC_1_L_unk_UP = []
logFC_1_L_unk_DOWN = []

logFC_2_L_ACC_UP = []
logFC_2_L_ACC_DOWN = []
logFC_2_L_unk_UP = []
logFC_2_L_unk_DOWN = []

logFC_3_L_ACC_UP = []
logFC_3_L_ACC_DOWN = []
logFC_3_L_unk_UP = []
logFC_3_L_unk_DOWN = []

logFC_4_L_ACC_UP = []
logFC_4_L_ACC_DOWN = []
logFC_4_L_unk_UP = []
logFC_4_L_unk_DOWN = []

logFC_5_L_ACC_UP = []
logFC_5_L_ACC_DOWN = []
logFC_5_L_unk_UP = []
logFC_5_L_unk_DOWN = []

logFC_6_L_ACC_UP = []
logFC_6_L_ACC_DOWN = []
logFC_6_L_unk_UP = []
logFC_6_L_unk_DOWN = []

## assign each column entry to the respective list

for line in InFile:	
	tab_split = line.split("\t")
	ACC = tab_split[0].strip()
	logFC_1 = tab_split[1].strip()
	logFC_2 = tab_split[2].strip()
	logFC_3 = tab_split[3].strip()
	logFC_4 = tab_split[4].strip()
	logFC_5 = tab_split[5].strip()
	logFC_6 = tab_split[6].strip()
	if logFC_1 == "None":
		logFC_1 = 0.00
	else:
		logFC_1 = float(logFC_1)
	if logFC_2 == "None":
		logFC_2 = 0.00
	else:
		logFC_2 = float(logFC_2)
	if logFC_3 == "None":
		logFC_3 = 0.00
	else:
		logFC_3 = float(logFC_3)
	if logFC_4 == "None":
		logFC_4 = 0.00
	else:
		logFC_4 = float(logFC_4)
	if logFC_5 == "None":
		logFC_5 = 0.00
	else:
		logFC_5 = float(logFC_5)
	if logFC_6 == "None":
		logFC_6 = 0.00
	else:
		logFC_6 = float(logFC_6)

#	print(logFC_1, logFC_2, logFC_3, logFC_4, logFC_5, logFC_6)

	if ACC.startswith("comp"):
		if logFC_1 > 0.58:
			logFC_1_L_unk_UP.append(ACC)
		elif logFC_1 < -0.58:
			logFC_1_L_unk_DOWN.append(ACC)
		if logFC_2 > 0.58:
			logFC_2_L_unk_UP.append(ACC)
		elif logFC_2 < -0.58:
			logFC_2_L_unk_DOWN.append(ACC)
		if logFC_3 > 0.58:
			logFC_3_L_unk_UP.append(ACC)
		elif logFC_3 < -0.58:
			logFC_3_L_unk_DOWN.append(ACC)
		if logFC_4 > 0.58:
			logFC_4_L_unk_UP.append(ACC)
		elif logFC_4 < -0.58:
			logFC_4_L_unk_DOWN.append(ACC)
		if logFC_5 > 0.58:
			logFC_5_L_unk_UP.append(ACC)
		elif logFC_5 < -0.58:
			logFC_5_L_unk_DOWN.append(ACC)
		if logFC_6 > 0.58:
			logFC_6_L_unk_UP.append(ACC)
		elif logFC_6 < -0.58:
			logFC_6_L_unk_DOWN.append(ACC)
	else:
		if logFC_1 > 0.58:
			logFC_1_L_ACC_UP.append(ACC)
		elif logFC_1 < -0.58:
			logFC_1_L_ACC_DOWN.append(ACC)
		if logFC_2 > 0.58:
			logFC_2_L_ACC_UP.append(ACC)
		elif logFC_2 < -0.58:
			logFC_2_L_ACC_DOWN.append(ACC)
		if logFC_3 > 0.58:
			logFC_3_L_ACC_UP.append(ACC)
		elif logFC_3 < -0.58:
			logFC_3_L_ACC_DOWN.append(ACC)
		if logFC_4 > 0.58:
			logFC_4_L_ACC_UP.append(ACC)
		elif logFC_4 < -0.58:
			logFC_4_L_ACC_DOWN.append(ACC)
		if logFC_5 > 0.58:
			logFC_5_L_ACC_UP.append(ACC)
		elif logFC_5 < -0.58:
			logFC_5_L_ACC_DOWN.append(ACC)
		if logFC_6 > 0.58:
			logFC_6_L_ACC_UP.append(ACC)
		elif logFC_6 < -0.58:
			logFC_6_L_ACC_DOWN.append(ACC)

#print(logFC_6_L_ACC_DOWN )

### number of contigs for all 6 comparisons

numer_of_contigs_1 = len(logFC_1_L_ACC_DOWN) + len(logFC_1_L_ACC_UP) + len(logFC_1_L_unk_DOWN) + len(logFC_1_L_unk_UP)
numer_of_contigs_2 = len(logFC_2_L_ACC_DOWN) + len(logFC_2_L_ACC_UP) + len(logFC_2_L_unk_DOWN) + len(logFC_2_L_unk_UP)
numer_of_contigs_3 = len(logFC_3_L_ACC_DOWN) + len(logFC_3_L_ACC_UP) + len(logFC_3_L_unk_DOWN) + len(logFC_3_L_unk_UP)
numer_of_contigs_4 = len(logFC_4_L_ACC_DOWN) + len(logFC_4_L_ACC_UP) + len(logFC_4_L_unk_DOWN) + len(logFC_4_L_unk_UP)
numer_of_contigs_5 = len(logFC_5_L_ACC_DOWN) + len(logFC_5_L_ACC_UP) + len(logFC_5_L_unk_DOWN) + len(logFC_5_L_unk_UP)
numer_of_contigs_6 = len(logFC_6_L_ACC_DOWN) + len(logFC_6_L_ACC_UP) + len(logFC_6_L_unk_DOWN) + len(logFC_6_L_unk_UP)

### number of annotated contigs for all 6 comparisons

annotated_1 = len(logFC_1_L_ACC_DOWN) + len(logFC_1_L_ACC_UP)
annotated_2 = len(logFC_2_L_ACC_DOWN) + len(logFC_2_L_ACC_UP)
annotated_3 = len(logFC_3_L_ACC_DOWN) + len(logFC_3_L_ACC_UP)
annotated_4 = len(logFC_4_L_ACC_DOWN) + len(logFC_4_L_ACC_UP)
annotated_5 = len(logFC_5_L_ACC_DOWN) + len(logFC_5_L_ACC_UP)
annotated_6 = len(logFC_6_L_ACC_DOWN) + len(logFC_6_L_ACC_UP)

## upregulated

annotated_up_1 = len(logFC_1_L_ACC_UP)
annotated_up_2 = len(logFC_2_L_ACC_UP)
annotated_up_3 = len(logFC_3_L_ACC_UP)
annotated_up_4 = len(logFC_4_L_ACC_UP)
annotated_up_5 = len(logFC_5_L_ACC_UP)
annotated_up_6 = len(logFC_6_L_ACC_UP)


## downregultated

annotated_down_1 = len(logFC_1_L_ACC_DOWN)
annotated_down_2 = len(logFC_2_L_ACC_DOWN)
annotated_down_3 = len(logFC_3_L_ACC_DOWN)
annotated_down_4 = len(logFC_4_L_ACC_DOWN)
annotated_down_5 = len(logFC_5_L_ACC_DOWN)
annotated_down_6 = len(logFC_6_L_ACC_DOWN)


### number of non annotated contigs for all 6 comparisons


non_annotated_1 = len(logFC_1_L_unk_DOWN) + len(logFC_1_L_unk_UP)
non_annotated_2 = len(logFC_2_L_unk_DOWN) + len(logFC_2_L_unk_UP)
non_annotated_3 = len(logFC_3_L_unk_DOWN) + len(logFC_3_L_unk_UP)
non_annotated_4 = len(logFC_4_L_unk_DOWN) + len(logFC_4_L_unk_UP)
non_annotated_5 = len(logFC_5_L_unk_DOWN) + len(logFC_5_L_unk_UP)
non_annotated_6 = len(logFC_6_L_unk_DOWN) + len(logFC_6_L_unk_UP)

## upregulated

non_annotated_up_1 = len(logFC_1_L_unk_UP)
non_annotated_up_2 = len(logFC_2_L_unk_UP)
non_annotated_up_3 = len(logFC_3_L_unk_UP)
non_annotated_up_4 = len(logFC_4_L_unk_UP)
non_annotated_up_5 = len(logFC_5_L_unk_UP)
non_annotated_up_6 = len(logFC_6_L_unk_UP)

## downregultated

non_annotated_down_1 = len(logFC_1_L_unk_DOWN)
non_annotated_down_2 = len(logFC_2_L_unk_DOWN)
non_annotated_down_3 = len(logFC_3_L_unk_DOWN)
non_annotated_down_4 = len(logFC_4_L_unk_DOWN)
non_annotated_down_5 = len(logFC_5_L_unk_DOWN)
non_annotated_down_6 = len(logFC_6_L_unk_DOWN)


outFile.write("categories\tfins_carol\tliver_carol\tmuscle_carol\tfins_torg\tliver_torg\tmuscle_torg\n")
outFile.write("total numer of contigs\t" + str(numer_of_contigs_1) + "\t" + str(numer_of_contigs_2) + "\t" + str(numer_of_contigs_3) + "\t" + str(numer_of_contigs_4) + "\t" + str(numer_of_contigs_5) + "\t" + str(numer_of_contigs_6) + "\n")

outFile.write("annotated contigs\t" + str(annotated_1) + "\t" + str(annotated_2) + "\t" + str(annotated_3) + "\t" + str(annotated_4) + "\t" + str(annotated_5) + "\t" + str(annotated_6) + "\n")

outFile.write("annotated contigs upregulted\t" + str(annotated_up_1) + "\t" + str(annotated_up_2) + "\t" + str(annotated_up_3) + "\t" + str(annotated_up_4) + "\t" + str(annotated_up_5) + "\t" + str(annotated_up_6) + "\n")

outFile.write("annotated contigs downregulted\t" + str(annotated_down_1) + "\t" + str(annotated_down_2) + "\t" + str(annotated_down_3) + "\t" + str(annotated_down_4) + "\t" + str(annotated_down_5) + "\t" + str(annotated_down_6) + "\n")

outFile.write("non annotated contigs\t" + str(non_annotated_1) + "\t" + str(non_annotated_2) + "\t" + str(non_annotated_3) + "\t" + str(non_annotated_4) + "\t" + str(non_annotated_5) + "\t" + str(non_annotated_6) + "\n")

outFile.write("non annotated contigs upregulted\t" + str(non_annotated_up_1) + "\t" + str(non_annotated_up_2) + "\t" + str(non_annotated_up_3) + "\t" + str(non_annotated_up_4) + "\t" + str(non_annotated_up_5) + "\t" + str(non_annotated_up_6) + "\n")

outFile.write("non annotated contigs downregulted\t" + str(non_annotated_down_1) + "\t" + str(non_annotated_down_2) + "\t" + str(non_annotated_down_3) + "\t" + str(non_annotated_down_4) + "\t" + str(non_annotated_down_5) + "\t" + str(non_annotated_down_6) + "\n")


outFile.close()

## block to generate lists of ACC for each gene (either for DOWN and for UP regulated genes, the total can be achieved by merging the two lists afterwards)
## UP
outFile_1 = open ("fins_carol_to_DAVID_UP.txt", "w")

for element in logFC_1_L_ACC_UP:
	outFile_1.write(element + "\n")

outFile_1.close()
outFile_2 = open ("liver_carol_to_DAVID_UP.txt", "w")


for element in logFC_2_L_ACC_UP:
	outFile_2.write(element + "\n")

outFile_2.close()
outFile_3 = open ("muscle_carol_to_DAVID_UP.txt", "w")


for element in logFC_3_L_ACC_UP:
	outFile_3.write(element + "\n")

outFile_3.close()
outFile_4 = open ("fins_torg_to_DAVID_UP.txt", "w")


for element in logFC_4_L_ACC_UP:
	outFile_4.write(element + "\n")

outFile_4.close()
outFile_5 = open ("liver_torg_to_DAVID_UP.txt", "w")


for element in logFC_5_L_ACC_UP:
	outFile_5.write(element + "\n")

outFile_5.close()
outFile_6 = open ("muscle_torg_to_DAVID_UP.txt", "w")


for element in logFC_6_L_ACC_UP:
	outFile_6.write(element + "\n")

outFile_6.close()

## DOWN

outFile_11 = open ("fins_carol_to_DAVID_DOWN.txt", "w")

for element in logFC_1_L_ACC_DOWN:
	outFile_11.write(element + "\n")

outFile_11.close()
outFile_21 = open ("liver_carol_to_DAVID_DOWN.txt", "w")


for element in logFC_2_L_ACC_DOWN:
	outFile_21.write(element + "\n")

outFile_21.close()
outFile_31 = open ("muscle_carol_to_DAVID_DOWN.txt", "w")


for element in logFC_3_L_ACC_DOWN:
	outFile_31.write(element + "\n")

outFile_31.close()
outFile_41 = open ("fins_torg_to_DAVID_DOWN.txt", "w")


for element in logFC_4_L_ACC_DOWN:
	outFile_41.write(element + "\n")

outFile_41.close()
outFile_51 = open ("liver_torg_to_DAVID_DOWN.txt", "w")


for element in logFC_5_L_ACC_DOWN:
	outFile_51.write(element + "\n")

outFile_51.close()
outFile_61 = open ("muscle_torg_to_DAVID_DOWN.txt", "w")


for element in logFC_6_L_ACC_DOWN:
	outFile_61.write(element + "\n")

outFile_61.close()

## This step generates a list of ACC with all DE genes, without duplications since there is no overlap between whats DE UP and DE DOWN

os.system("cat fins_carol_to_DAVID_*.txt > fins_carol_to_DAVID_ALL.txt")
os.system("cat liver_carol_to_DAVID_*.txt > liver_carol_to_DAVID_ALL.txt")
os.system("cat muscle_carol_to_DAVID_*.txt > muscle_carol_to_DAVID_ALL.txt")
os.system("cat fins_torg_to_DAVID_*.txt > fins_torg_to_DAVID_ALL.txt")
os.system("cat liver_torg_to_DAVID_*.txt > liver_torg_to_DAVID_ALL.txt")
os.system("cat muscle_torg_to_DAVID_*.txt > muscle_torg_to_DAVID_ALL.txt")


## create merged lists of annotated and non annotated contigs for UP and DOWN regulated categories

mergedLogFC_1_DOWN = logFC_1_L_ACC_DOWN + logFC_1_L_unk_DOWN
mergedLogFC_1_UP = logFC_1_L_ACC_UP + logFC_1_L_unk_UP

mergedLogFC_2_DOWN = logFC_2_L_ACC_DOWN + logFC_2_L_unk_DOWN
mergedLogFC_2_UP = logFC_2_L_ACC_UP + logFC_2_L_unk_UP

mergedLogFC_3_DOWN = logFC_3_L_ACC_DOWN + logFC_3_L_unk_DOWN
mergedLogFC_3_UP = logFC_3_L_ACC_UP + logFC_3_L_unk_UP

mergedLogFC_4_DOWN = logFC_4_L_ACC_DOWN + logFC_4_L_unk_DOWN
mergedLogFC_4_UP = logFC_4_L_ACC_UP + logFC_4_L_unk_UP

mergedLogFC_5_DOWN = logFC_5_L_ACC_DOWN + logFC_5_L_unk_DOWN
mergedLogFC_5_UP = logFC_5_L_ACC_UP + logFC_5_L_unk_UP

mergedLogFC_6_DOWN = logFC_6_L_ACC_DOWN + logFC_6_L_unk_DOWN
mergedLogFC_6_UP = logFC_6_L_ACC_UP + logFC_6_L_unk_UP

## block that lists every UP and DOWN regulated genes in a text file for all contigs regardless of being annotated or not.
# UP

outFile_12 = open ("ALL_fins_carol_UP.txt", "w")

for element in mergedLogFC_1_UP :
	outFile_12.write(element + "\n")

outFile_12.close()
outFile_22 = open ("ALL_liver_carol_UP.txt", "w")


for element in mergedLogFC_2_UP :
	outFile_22.write(element + "\n")

outFile_22.close()
outFile_32 = open ("ALL_muscle_carol_UP.txt", "w")


for element in mergedLogFC_3_UP :
	outFile_32.write(element + "\n")

outFile_32.close()
outFile_42 = open ("ALL_fins_torg_UP.txt", "w")


for element in mergedLogFC_4_UP :
	outFile_42.write(element + "\n")

outFile_42.close()
outFile_52 = open ("ALL_liver_torg_UP.txt", "w")


for element in mergedLogFC_5_UP :
	outFile_52.write(element + "\n")

outFile_52.close()
outFile_62 = open ("ALL_muscle_torg_UP.txt", "w")


for element in mergedLogFC_6_UP :
	outFile_62.write(element + "\n")

outFile_62.close()

## DOWN

outFile_112 = open ("ALL_fins_carol_DOWN.txt", "w")

for element in mergedLogFC_1_DOWN :
	outFile_112.write(element + "\n")

outFile_112.close()
outFile_212 = open ("ALL_liver_carol_DOWN.txt", "w")


for element in mergedLogFC_2_DOWN :
	outFile_212.write(element + "\n")

outFile_212.close()
outFile_312 = open ("ALL_muscle_carol_DOWN.txt", "w")


for element in mergedLogFC_3_DOWN :
	outFile_312.write(element + "\n")

outFile_312.close()
outFile_412 = open ("ALL_fins_torg_DOWN.txt", "w")


for element in mergedLogFC_4_DOWN :
	outFile_412.write(element + "\n")

outFile_412.close()
outFile_512 = open ("ALL_liver_torg_DOWN.txt", "w")


for element in mergedLogFC_5_DOWN :
	outFile_512.write(element + "\n")

outFile_512.close()
outFile_612 = open ("ALL_muscle_torg_DOWN.txt", "w")


for element in mergedLogFC_6_DOWN :
	outFile_612.write(element + "\n")

outFile_612.close()

## This step generates a list of ACC with all DE genes, without duplications since there is no overlap between whats DE UP and DE DOWN

os.system("cat ALL_fins_carol_*.txt > fins_carol_ALL.txt")
os.system("cat ALL_liver_carol_*.txt > liver_carol_ALL.txt")
os.system("cat ALL_muscle_carol_*.txt > muscle_carol_ALL.txt")
os.system("cat ALL_fins_torg_*.txt > fins_torg_to_ALL.txt")
os.system("cat ALL_liver_torg_*.txt > liver_torg_ALL.txt")
os.system("cat ALL_muscle_torg_*.txt > muscle_torg_ALL.txt")