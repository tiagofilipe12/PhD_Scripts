#!/usr/bin/python2

## A script intended to calculate FDR values with the correction of BY or BH, provide a below diagonal with the pvalues. The above diagonal will be ignored.

import sys
from rpy2.robjects.packages import importr
from rpy2.robjects.vectors import FloatVector
stats = importr('stats')

input_file = sys.argv[1]
file_handle = open(input_file)
output_file = input_file + "_qvalues"
output_handle = open(output_file,"w")


x = 0
L=[]
L_samples = []
for line in file_handle:
	x += 1
	tab_split = line.split(",")
	sampleID = tab_split[0]
	L_samples.append(sampleID)
	if x == 1:
		pass
	elif x < 73:
		for element in tab_split[1:x]:
			L.append(element)

p_adjust = stats.p_adjust(FloatVector(L), method = 'BY')	## change to BH for default FDR

print(p_adjust)

counter = -1
y=0
for sample in L_samples:
	counter += 1
	if counter == 0:
	 	output_handle.write(L_samples[counter] + "\n")
	elif counter > 0:
		L_fdr = []
		z = y + counter
		for i in p_adjust[y:z]: 	
			L_fdr.append(str(i))
			y = z
		output_handle.write(L_samples[counter] + "\t" + "\t".join(L_fdr) + "\n")

