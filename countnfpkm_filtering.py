#!/usr/bin/python3

### countnfpkm.py v.0.1

## This script filters couns or fpkms and summarizes in terms of up and down genes in a csv

import os
import sys
import argparse

## Parse the inputs and options

parser = argparse.ArgumentParser(description="acc_to_contig.py: searches your accession number in several xml given a fasta with those contigs")

parser.add_argument("-in",dest="input",required=True,nargs='+',help="Provide the input files")
parser.add_argument("-fpkm",dest="fpkm",help="this option selects fpkm filter instead of count")
parser.add_argument("-counts",dest="count",help="this option selects counts filter instead of fpkm")
parser.add_argument("-save",dest="save",required=True,help="Provide the name of the output file. extension will be added by itself.")


arg = parser.parse_args()
inputfile = arg.input
fpkms = arg.fpkm
counts = arg.count
saveFile = arg.save

try:
	print(fpkms)
except NameError:
	print("fpkms option is disabled")
else:
	try:
		print(counts)
	except NameError:
		print("counts option is disabled")
	else:
		print("You need to use one of the two options: -fpkm or -count")

## Write output files

OutFile = open(saveFile + ".txt", "w")
OutFile.write("sample_id\ttotal\tup\tdown\n")



for File in inputfile:
	InFile = open(File, "r")
	next(InFile)
	Down_list = []
	Up_list = []
	All_list = []
	for line in InFile:
		tab_split = line.split("\t")
		sample_name = tab_split[0].strip()
		sample_1 = float(tab_split[1].strip())
		sample_2 = float(tab_split[2].strip())
		abs_sample_1 = abs(sample_1)
		abs_sample_2 = abs(sample_2)
		sum_samples = abs_sample_1 + abs_sample_2
		if fpkms == None:
			if sum_samples > float(counts):
				All_list.append(sample_name)
				Diff = sample_1 - sample_2
				if Diff < 0:
					Down_list.append(sample_name)
				elif Diff > 0:
					Up_list.append(sample_name)
				else:
					pass
			else:
				pass
		elif counts == None:
			if sum_samples > float(fpkms):
				All_list.append(sample_name)
				Diff = sample_1 - sample_2
				print(Diff)
				if Diff < 0:
					Down_list.append(sample_name)
				elif Diff > 0:
					Up_list.append(sample_name)
				else:
					pass
			else:
				pass
		else:
			print("something is wrong!!!")
	OutFile.write(File + "\t" + str(len(All_list)) + "\t" + str(len(Up_list)) + "\t" + str(len(Down_list)) + "\n")




