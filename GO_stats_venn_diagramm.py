#!/usr/bin/python3

## GO_stats_venn_diagramm v 0.1 

import sys

Filegrab = sys.argv[1:] 



L_1 = []
dic_pvalue1 = {}
L_2 = []
dic_pvalue2 = {}
L_3 = []
dic_pvalue3 = {}
L_4 = []
dic_pvalue4 = {}
L_5 = []
dic_pvalue5 = {}
L_6 = []
dic_pvalue6 = {}

dic_Go_term = {}

x = 0
for infile in Filegrab:
	file_handle = open(infile)
	x += 1
	print(infile)
	for line in file_handle:
		if line.startswith("GOTERM"):
			tab_split = line.split("\t")
			Go_type = tab_split[0].strip()
			Go_term = tab_split[1].strip().split("~")[0]
			Go_description = tab_split[1].strip().split("~")[1]
			p_value = tab_split[4].strip()
			if Go_term in dic_Go_term.keys():
				pass
			else:
				dic_Go_term[Go_term] = [Go_description, Go_type]				
			if x == 1:
				L_1.append(Go_term)
				dic_pvalue1[Go_term] = p_value
			elif x == 2:
				L_2.append(Go_term)
				dic_pvalue2[Go_term] = p_value
			elif x == 3:
				L_3.append(Go_term)
				dic_pvalue3[Go_term] = p_value
			elif x == 4:
				L_4.append(Go_term)
				dic_pvalue4[Go_term] = p_value
			elif x == 5:
				L_5.append(Go_term)
				dic_pvalue5[Go_term] = p_value
			elif x == 6:
				L_6.append(Go_term)
				dic_pvalue6[Go_term] = p_value
			else:
				print("error: to much infiles, script is limited to 6 input files... but feel free to change it anytime")
		else:
			pass


print(L_5)			
print("First venn3 diagramm")
print(str(len(L_1)) + " GOs in " + Filegrab[0])
print(str(len(L_2)) + " GOs in " + Filegrab[1])
print(str(len(L_3)) + " GOs in " + Filegrab[2] + "\n")

print(str(len(list(set(L_1) & set(L_2)))) + " GOs common to " + Filegrab[0] + " and " + Filegrab[1])
print(str(len(list(set(L_2) & set(L_3)))) + " GOs common to " + Filegrab[1] + " and " + Filegrab[2])
print(str(len(list(set(L_1) & set(L_3)))) + " GOs common to " + Filegrab[0] + " and " + Filegrab[2])
print(str(len(list(set(L_1) & set(L_2) & set(L_3)))) + " GOs common to " + Filegrab[0]+ " and " + Filegrab[1] + " and " + Filegrab[2] + "\n")

print("Second venn3 diagramm")
print(str(len(L_4)) + " GOs in " + Filegrab[3])
print(str(len(L_5)) + " GOs in " + Filegrab[4])
print(str(len(L_6)) + " GOs in " + Filegrab[5] + "\n")

print(str(len(list(set(L_4) & set(L_5)))) + " GOs common to " + Filegrab[3] + " and " + Filegrab[4])
print(str(len(list(set(L_5) & set(L_6)))) + " GOs common to " + Filegrab[4] + " and " + Filegrab[5])
print(str(len(list(set(L_4) & set(L_6)))) + " GOs common to " + Filegrab[3] + " and " + Filegrab[5])
print(str(len(list(set(L_4) & set(L_5) & set(L_6)))) + " GOs common to " + Filegrab[3]+ " and " + Filegrab[4] + " and " + Filegrab[5] +"\n")

print("venn2 diagramms")
print(str(len(list(set(L_1) & set(L_4)))) + " GOs common to " + Filegrab[0] + " and " + Filegrab[3])
print(str(len(list(set(L_2) & set(L_5)))) + " GOs common to " + Filegrab[1] + " and " + Filegrab[4])
print(str(len(list(set(L_3) & set(L_6)))) + " GOs common to " + Filegrab[2] + " and " + Filegrab[5])


## write output files

outFile_venn3_1 = open("carol_common_GOs.txt", "w")
outFile_venn3_2 = open("torg_common_GOs.txt", "w")

outFile_venn2_3 = open("fins_common_GOs.txt", "w")
outFile_venn2_4 = open("liver_common_GOs.txt", "w")
outFile_venn2_5 = open("muscle_common_GOs.txt", "w")

## preamble of the files

outFile_venn3_1.write("Go_term\tGo_description\tGo_type\t" + Filegrab[0] +"\t" + Filegrab[1] + "\t" + Filegrab[2] + "\n")
outFile_venn3_2.write("Go_term\tGo_description\tGo_type\t" + Filegrab[3] +"\t" + Filegrab[4] + "\t" + Filegrab[5] + "\n")
outFile_venn2_3.write("Go_term\tGo_description\tGo_type\t" + Filegrab[0] +"\t" + Filegrab[3] + "\n")
outFile_venn2_4.write("Go_term\tGo_description\tGo_type\t" + Filegrab[1] +"\t" + Filegrab[4] + "\n")
outFile_venn2_5.write("Go_term\tGo_description\tGo_type\t" + Filegrab[2] +"\t" + Filegrab[5] + "\n")

## output the list of common GOs for all organs of S. carolitertii

for item in list(set(L_1) & set(L_2) & set(L_3)):
	outFile_venn3_1.write(item + "\t" + dic_Go_term[item][0] + "\t" + dic_Go_term[item][1] + "\t" + dic_pvalue1[item] + "\t" + dic_pvalue2[item] + "\t" + dic_pvalue3[item] + "\n")

for item in list(set(L_4) & set(L_5) & set(L_6)):
	outFile_venn3_2.write(item + "\t" + dic_Go_term[item][0] + "\t" + dic_Go_term[item][1] + "\t" + dic_pvalue4[item] + "\t" + dic_pvalue5[item] + "\t" + dic_pvalue6[item] + "\n")

for item in list(set(L_1) & set(L_4)):
	outFile_venn2_3.write(item + "\t" + dic_Go_term[item][0] + "\t" + dic_Go_term[item][1] + "\t" + dic_pvalue1[item] + "\t" + dic_pvalue4[item]  + "\n")

for item in list(set(L_2) & set(L_5)):
	outFile_venn2_4.write(item + "\t" + dic_Go_term[item][0] + "\t" + dic_Go_term[item][1] + "\t" + dic_pvalue2[item] + "\t" + dic_pvalue5[item] + "\n")

for item in list(set(L_3) & set(L_6)):
	outFile_venn2_5.write(item + "\t" + dic_Go_term[item][0] + "\t" + dic_Go_term[item][1] + "\t" + dic_pvalue3[item] + "\t" + dic_pvalue6[item] + "\n")
