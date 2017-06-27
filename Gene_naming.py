#!/usr/bin/python3

# Gene_naming.py version 0.1
# This script is used to atribute gene names to the differently expressed genes
# retrieved from EdgeR and sort it in descending order of logFC. 
# This script is still under development, but it already do what is intended to.

import sys

argument_list = sys.argv

#Fetch the input file from edgeR with DE genes.
Filegrab = sys.argv[1]
File_ext = Filegrab[63:]

#Fetch the annotation file (expot topblast) from blast2GO exported as Seq.
topBlastFile_grab = sys.argv[2]

#Block to open and read files and output files.
InFile = open(Filegrab, "r")
topBlast = open(topBlastFile_grab, "r")
outFile = open ("Named_genes_" + File_ext, "w")

#Block that creates a list of lines from the input file.
data=InFile.readlines()
outFile.write("contig" + "\t" + data[0].rstrip("\n") + "\tSeqName\tACC\n")
del data[0]

Dic = {}
ACCdic = {}

#Construct two dictionaries of contigs as keys and SeqNames and accession numbers as answer for given keys.
for line in topBlast:	
	if line.startswith("SeqName"):
		pass
	else:
		tab_split = line.split("\t")
		contigName = tab_split[0].strip()
		seqName = tab_split[1].strip()
		ACC = tab_split[4].strip()
		Dic[contigName] = seqName
		ACCdic[contigName] = ACC

#Sort the list of lines generated that retrieves for the output file in descendent order of logFC and append a new column with SeqName.
sorteData=sorted(data, key=lambda l: float(l.split()[1]),reverse=True)
for item in sorteData:
	tab_split2 = item.split()
	key = tab_split2[0].strip()
	if key in Dic.keys() and ACCdic.keys():
		outFile.write(item.rstrip("\n") + "\t" + Dic[key] + "\t" + ACCdic[key] + "\n")
	else:
		outFile.write(item.rstrip("\n") + "\tNone\tNone\n")