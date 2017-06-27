#!/usr/bin/python

import os
os.chdir("/home/tiago/Programas/phase.2.1.1.linux")
print "Current directory:"
currentDir = os.getcwd()
print os.getcwd()
listFiles = os.system("ls")
print listFiles
print " "
fileInput=raw_input("Insert path/to/file: ")
print " "
print "info: default is 100"
Iterations=raw_input("Insert the number of iterations: ")
print " "
print "info: default is 1"
thinningInterval=raw_input("Insert thinning interval: ")
print " "
print "info: default is 100"
burnIn=raw_input("Insert burn-in: ")
print " "
print "-S flag options: leave blank - default; '-S123 - seed set to be 123"
seed = raw_input("Insert seed: ")
print " "
print "-M flag options: '-MS' - ignores recombination; '-MR' - default and accounts for recombination; '-MQ' - hybridization model"
print " "
mOption = raw_input("Insert option: ")
print " "
print "File Format Options: '-f0' - default; '-f1' - genotype listed in a single line; '-f2' - genotypes are denoted with a single character"
fileFormat = raw_input("Insert option: ")
print " "
print "File Format Options: leave blank - default; '-n' - indicates that file does not contain IDs"
fileIDs= raw_input("Insert option: ")
os.system("./PHASE"+ " " + mOption + " " + fileFormat + " " + fileIDs + " " + seed + " " + fileInput + " output.out" + " " + Iterations + " " + thinningInterval + " " + burnIn)
print " "
print " "
print "IF YOU WANT TO SKIP THIS STEP TYPE 'skip'"
path = raw_input("Insert path where to copy output files: ")
if path == "skip":
	print "Done! Output files are in ", currentDir
	raise SystemExit
else:
	os.system("mv output.out" + " " + "output.out_freqs" + " " + "output.out_hbg" + " " + "output.out_monitor" + " " + "output.out_pairs" + " " + "output.out_probs" + " " + "output.out_recom" + " " + path)
	print "Files were moved to ", path
