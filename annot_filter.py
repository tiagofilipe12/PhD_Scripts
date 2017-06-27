#!/usr/bin/python3

## annot_filter.py v1.0.0
##
## This script filters .annot files given a list of Accesion numbers and contigIDs
## Input: Named_genes file for correspondences; list of ACCs or contig IDs;.annot file from b2go
##
## Author: T. F. Jesus
## Year: 2015
## Last update: 29-10-2015

import os
import sys
import argparse

## Parse the inputs and options

parser = argparse.ArgumentParser(description="annot_filter.py: this script filters annot files given a list of Accesion numbers or contig IDs")

parser.add_argument("-n",dest="correspondences",help="Provide the Named_genes_* file name")
parser.add_argument("-l",dest="list",help="Provide the list file name")
parser.add_argument("-a",dest="annot",help="Provide the .annot file name")




arg = parser.parse_args()
corr_in = arg.correspondences
list_obj = arg.list
annotation = arg.annot

corrFile = open(corr_in, "r")
ListObj = open(list_obj, "r")

## list of IDs

L_ids =[]
for line in ListObj:
        L_ids.append(line.strip("\n"))


## makes a list of contig IDs to filter in the .annot file

L_contigs =[]
x= 0
for line in corrFile:
        if line.startswith("contig"):
                pass
        else:
                tab_split = line.split("\t")
                ACC = tab_split[-1].strip()
                contig = tab_split[0].strip()
                if ACC in L_ids:
                        L_contigs.append(contig)
                elif contig in L_ids:
                        L_contigs.append(contig)
                        x = x +1
                else:
                        pass
print(len(L_contigs))

## Filter the annot file and it is ready for b2go statistics.
Annot = open(annotation, "r")
outFile = open("filtered_" + annotation, "w")

for line in Annot:
        tab_split = line.split("\t")
        contig = tab_split[0].strip()
        if contig in L_contigs:
                outFile.write(line)
        else:
                pass


