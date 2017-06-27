#!/usr/bin/python
import os
## import re
## X="BEGIN DnaSP"
## regexpX=re.compile(X, IGNORECASE)
fileInput = raw_input("Insert path to the input: ")
Gama = raw_input("Insert number of gamma categories:")
currentDir = os.getcwd()
os.system("java -jar modelgenerator.jar /home/tiago/VMshareProjectos_sequencher/Phase/bmp4/TODOS/Analises_single_locus/ML/1aligned_reduced_dataset_bmp4.fas" + Gama + ">" + currentDir +"modelgen_output.txt")
os.chdir(currentDir)
os.system("gedit modelgen_output.txt")
print "Files were stored in ", currentDir
