#!/usr/bin/python2.7
#input files are named_genes files, the output of Gene_naming.py.
#this script retrieves the number of annotated genes in one transcriptome

import sys

argument_list = sys.argv

#Fetch the input files for species 1.
File1 = sys.argv[1]
File2 = sys.argv[2]	
File3 = sys.argv[3]	


#Open file 1
InFile1 = open(File1, "r")
InFile2 = open(File2, "r")
InFile3 = open(File3, "r")

L1sp = []

#make a list for speceis annotated sequences considering 3 libraries.
for file in [InFile1,InFile2,InFile3]:
	for line in file:
		if line.startswith("contig"):
			pass
		else:
			line_strip = line.split("\t")
			ACC = line_strip[6].strip()
			if ACC == "None":
				pass
			else:
				L1sp.append(ACC)

print(len(L1sp))
Set_final_1sp = list(set(L1sp))
print(len(Set_final_1sp))


#Fetch the input files for species 2.
File4 = sys.argv[4]
File5 = sys.argv[5]	
File6 = sys.argv[6]	


#Open file 1
InFile4 = open(File4, "r")
InFile5 = open(File5, "r")
InFile6 = open(File6, "r")

L2sp = []

#make a list for speceis annotated sequences considering 3 libraries.
for file in [InFile4,InFile5,InFile6]:
	for line in file:
		if line.startswith("contig"):
			pass
		else:
			line_strip = line.split("\t")
			ACC = line_strip[6].strip()
			if ACC == "None":
				pass
			else:
				L2sp.append(ACC)

print(len(L2sp))
Set_final_2sp = list(set(L2sp))
print(len(Set_final_2sp))

Intersection = list(set(Set_final_1sp) & set(Set_final_2sp))
print(len(Intersection))

## construct a venn diagram for this info
from matplotlib_venn import venn2
import matplotlib.pyplot as plt
fig = plt.figure()
venn2(subsets = (len(Set_final_1sp)-len(Intersection),len(Set_final_2sp)-len(Intersection) , len(Intersection)), set_labels = ("S. carolitertii", "S. torgalensis"))
fig.savefig("annotated_genes_fulltranscriptomes" + '_venn2.pdf', format='PDF') 
plt.close(fig)