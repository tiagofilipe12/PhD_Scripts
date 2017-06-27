#!/usr/bin/python3

# this script compares two conditions (two files like fins_torg_to_DAVID_ALL.txt) and retrieves a list of exclusive ACC for each species and shared ACC that is intend to be further
# analyzed using annot_filter.py and b2go to retrieve the functions of these ACC.

import sys

Filegrab1 = sys.argv[1]
Filegrab2 = sys.argv[2] 

L1 = []
L2 = []

file_handle1 = open(Filegrab1)

for line in file_handle1:
	L1.append(line)


file_handle2 = open(Filegrab2)

for line in file_handle2:
	L2.append(line)
annot_filter.py
shared = set(L1).intersection(L2)
outFile = open("shared" + Filegrab2 + Filegrab1, "w")
for item in shared:
	outFile.write(item)

print("shared = ",  len(shared))

exclusive_File1 = [x for x in L1 if x not in shared]
exclusive_File2 = [x for x in L2 if x not in shared]
print("exclusive from ",  Filegrab1, " = ", len(exclusive_File1), "\nexclusive from ", Filegrab2, " = ", len(exclusive_File2))
outFile1 = open("exclusive from " +  Filegrab1, "w")
outFile2 = open("exclusive from " +  Filegrab2, "w")
for item1 in exclusive_File1:
	outFile1.write(item1)

for item2 in exclusive_File2:
	outFile2.write(item2)