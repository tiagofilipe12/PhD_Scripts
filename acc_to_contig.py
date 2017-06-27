#!/usr/bin/python3

### acc_to_contig.py v.0.2

## This script is intended to provide an input accession number (acc) and search it in a given list of xml files, retrieving the contig in a output fasta that consist in filtering a given fasta (normally the total transcriptome in fasta)

import os
import sys
import argparse

## Parse the inputs and options

parser = argparse.ArgumentParser(description="acc_to_contig.py: searches your accession number in several xml given a fasta with those contigs")

parser.add_argument("-f",dest="fasta_input",help="Provide the FASTA input file name")
parser.add_argument("-x",dest="xml_input",nargs='+',help="Provide the XML inputs file name")
parser.add_argument("-filter",dest="filter_option",required=True,help="Provide a file with accession numbers separated by new lines.")
parser.add_argument("-outname",dest="output_fasta",required=True,help="Provide the tag to add to the name of the output file")


arg = parser.parse_args()
fasta_in = arg.fasta_input
xml_in = arg.xml_input
filter_type = arg.filter_option
output_file = arg.output_fasta

## Open input files

fasta_file = open(fasta_in, "r")
filter_file = open(filter_type, "r")

## Write output files

outFile = open(output_file, "a")

## create a filter list from the input acc file list
filter_list=[]
for line in filter_file:
	filter_list.append(line.rstrip("\n"))


record_list = []                # Used to store contigs with the acc
counter = 0                     # Used to control when to stop appending to entry_storage variable. When = 0 stops appending and write to output XML.
hit_count = 0
# Despite quite specific this parser can be adapted for several types of filters
print(filter_list)
for i in xml_in:
	XMLFile = open(i, "r")
	for line in XMLFile:
		if "xml version=" in line:
			entry_storage=[]
			entry_storage.append(line)
			counter = 1
		elif "</BlastOutput>" in line:
			entry_storage.append(line+"\n")
			counter = 0
		elif counter == 1:
			entry_storage.append(line)
			if "Iteration_query-def" in line: #BlastOutput_query-def na versão antiga causava algumas sequências para serem mal atribuidas... especialmente quando se consultava o transcriptoma total
				line_split_contig = line.split(">")[1].split("<")[0]
			elif "Hit_num" in line:
				line_split_hit = line.split(">")[1].split("<")[0]
				if line_split_hit == "1":
					hit_count = 1
				else:
					hit_count = 0
			elif "Hit_accession" in line:
				line_split_acc = line.split(">")[1].split("<")[0]
				if line_split_acc in filter_list:			
					if hit_count == 1:
						record_list.append(line_split_contig)
				
			else:
				pass

print(record_list)
counter = 0
			
for line in fasta_file:
	if line.startswith(">") and line[1:].split()[0] in record_list:
		counter = 1
		outFile.write(line)
	elif line.startswith(">") and line[1:].split()[0] not in record_list:
		counter = 0
	elif counter == 0:
		pass
	elif counter == 1:
		outFile.write(line)

