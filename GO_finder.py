#!/usr/bin/python3

## This script generetes a list of all GO terms associated with given categories, provided in an input file

import os
import sys
import argparse

## Parse the inputs and options

parser = argparse.ArgumentParser(description="GO_finder.py: This script searchs for certain GO tems in DAVID table output")

parser.add_argument("-in",dest="input_file",required=True,help="Provide the input file name. tip: DAVID table file")
parser.add_argument("-c",dest="input_conversion",required=True,help="Provide the conversion file name. tip: DAVID conversion file")
parser.add_argument("-go",dest="go_option",required=True,help="provide a list of GO terms to search for as an .txt file")


arg = parser.parse_args()
table_in = arg.input_file
conversion_in = arg.input_conversion
go_filter = arg.go_option

## Lists GO terms to search for

go_Infile = open(go_filter, "r")

GOinput_list = [x.strip() for x in go_Infile]

## Creates a link between david ids and accession numbers

Conv_Infile = open(conversion_in, "r")

Dic_conversion = {}

for line in Conv_Infile:
	tab_split = line.split("\t")
	ACC = tab_split[0].strip()
	DAVID_ID = tab_split[1].strip()
	Spp = tab_split[2].strip()
	Dic_conversion.setdefault(DAVID_ID, [])
	if DAVID_ID in Dic_conversion.keys():
		Dic_conversion[DAVID_ID].append(ACC)	
	else:
		Dic_conversion[DAVID_ID] = ACC

## writes an output with the ACC and GO only for the expected GO terms.

Table_Infile = open(table_in, "r")
next(Table_Infile)
outFile = open(table_in[:-9] + "other_GOs.txt", "w")
outFile.write("DAVID_ID" + "\t" + "ACC" +"\t" + "GO_term" + "\t" + "GO_description" + "\n")

L=[]
for line in Table_Infile:
	tab_split = line.split("\t")
	table_ID = tab_split[0].strip()
	if len(tab_split) > 4:				## Pay attention since some DAVID files may not have one or more column which forces to change this line and the following.
		Gos_list = tab_split[4].strip().split(",")
		for GO in Gos_list:
			counter = 0
			GO_term = ""
			GO_description = ""
			for character in GO:
				if character == "~":
					counter = 1
					pass
				elif counter == 0:
					GO_term = GO_term + character
				elif counter == 1:
					GO_description = GO_description + character
#			print(GO_term, GO_description)
			if GO_term in GOinput_list:
				outFile.write(table_ID + "\t" + ",".join(Dic_conversion[table_ID]) +"\t" + GO_term + "\t" + GO_description + "\n")
	else:
		pass

