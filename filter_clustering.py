#!/usr/bin/python2.7

import sys
import matplotlib.pyplot as plt
import numpy as np
from rpy_options import set_options
set_options(RHOME='/usr/lib/R')
from rpy import *

#Script designed to construct a rough sum of 6 columns of Fold Change, sort the input using this sum in descending order and generates a heatmap of this information

argument_list = sys.argv
File1 = sys.argv[1]
InFile1 = open(File1, "r")
outFile = open ("filter_cluster_out", "w")
L_newlines =[]
X=[]
for line in InFile1:
	if line.startswith("geneName"):
		outFile.write(line.rstrip("\n") + "\t" + "Sum" + "\n")
		column_label = [line.split()[2],line.split()[3],line.split()[4],line.split()[5],line.split()[6],line.split()[7]]
#IndexError: list index out of range

	else:
		tab_split = line.split("\t")
		if tab_split[2].strip() != "None":
			firstElement = float(tab_split[2].strip())
		else:
			firstElement = 0.0
		if tab_split[3].strip() != "None":
			secondElement = float(tab_split[3].strip())
		else:
			secondElement = 0.0
		if tab_split[4].strip() != "None":
			thirdElement = float(tab_split[4].strip())
		else:
			thirdElement = 0.0
		if tab_split[5].strip() != "None":
			fourthElement = float(tab_split[5].strip())
		else:
			fourthElement = 0.0
		if tab_split[6].strip() != "None":
			fifthElement = float(tab_split[6].strip())
		else:
			fifthElement = 0.0
		if tab_split[7].strip() != "None":
			sixthElement = float(tab_split[7].strip())
		else:
			sixthElement = 0.0
		Elements = [firstElement,secondElement,thirdElement,fourthElement,fifthElement,sixthElement]
		sumElements = sum(Elements)
		newline = line.rstrip("\n") + "\t" + str(sumElements)
		L_newlines.append(newline)
		List_elements = [firstElement,secondElement,thirdElement,fourthElement,fifthElement,sixthElement]
		X.append(List_elements)

rowlabel = []
sortedNewlines=sorted(L_newlines, key=lambda l: float(l.split()[-1]),reverse=True)
for item in sortedNewlines:
#	outFile.write(item + "\n")
	rowlabel.append(item.split()[:-7])

X_array = np.array(X)
#print (X_array)

def library_colour(library_id):
	for i in column_label:
		if i == "torg" :
			return "#FF0000" # Red
	else :
		return "#0000FF" # Blue
library_colours = map(library_colour, column_label)

print ("Heatmap as PDF")
r.pdf("heatmap_from_python.pdf")
r.heatmap(X_array,
          cexRow=0.3,
          labRow=rowlabel, labCol=column_label,
          ColSideColors = library_colours,
          col = r.topo_colors(50))
r.dev_off()
print ("Done")