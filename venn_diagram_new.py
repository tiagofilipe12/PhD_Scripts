#!/usr/bin/python2.7

import sys
from matplotlib_venn import venn3
import matplotlib.pyplot as plt

argument_list = sys.argv
File1 = sys.argv[1]
InFile1 = open(File1, "r")

List_carol = []
List_torg = []
x = 0
for line1 in InFile1:
	line = line1.split("\t")
	element1= line[2].strip()
	print("control:",element1)
	element2= line[3].strip()
	element3= line[4].strip()
	element4= line[5].strip()
	element5= line[6].strip()
	element6= line[7].strip()
	if x == 0:
		set1= element1
		set2= element2
		set3= element3
		set4= element4
		set5= element5
		set6= element6
		x += 1
	elif x == 1:
		if element1 == "None":
			element1 = "None"
		elif float(element1) < 0.58:
			element1 = "None"
			print("teste1",element1)
		if element2 == "None":
			element2 = "None"
		elif float(element2) < 0.58:
			element2 = "None"
		if element3 == "None":
			element3 = "None"
		elif float(element3) < 0.58:
			element3 = "None"
		if element4 == "None":
			element4 = "None"
		elif float(element4) < 0.58:
			element4 = "None"
		if element5 == "None":
			element5 = "None"
		elif float(element5) < 0.58:
			element5 = "None"
		if element6 == "None":
			element6 = "None"
		elif float(element6) < 0.58:
			element6 = "None"
		print("teste2", element1)
		
	List_carol.append([element1,element2,element3])
	List_torg.append([element4,element5,element6])

##Build counter for carolitertii venn diagramm
#print(List_carol)

FLM_carol = 0
FL_carol = 0
F_carol = 0
LM_carol = 0
L_carol = 0
M_carol = 0
FM_carol = 0

for item in List_carol:
	if item[0:] == ["None"]*3:
		pass
	elif item[0:2] == ["None"]*2 and item[2] != "None":
		M_carol += 1
	elif item[1:] == ["None"]*2 and item[0] != "None":
		F_carol += 1
	elif [item[0],item[2]] == ["None"]*2 and item[1] != "None":
		L_carol += 1
	elif item[0:2] != ["None"]*2 and item[2] == "None":
			FL_carol += 1
	elif item[1:] != ["None"]*2 and item[0] == "None":
		LM_carol += 1
	elif [item[0],item[2]] != ["None"]*2 and item[1] == "None":
		FM_carol += 1
	elif item[0:] != ["None"]*3:
		FLM_carol += 1


a = FLM_carol
b = FL_carol
c = F_carol
d = LM_carol
e = L_carol
f = M_carol
g = FM_carol

print(a,b,c,d,e,f,g)

fig = plt.figure()

venn3(subsets = (c, e, b, f, g, d, a), set_labels = (set1, set2, set3))
fig.savefig("carol_alls" + '_venn3.pdf', format='PDF') #depends on the input sequence of the cluster_output file... in this case torgalensis was first and then carolitertii
plt.close(fig)

##Build counter for torgalensis venn diagramm

FLM_torg = 0
FL_torg = 0
F_torg = 0
LM_torg = 0
L_torg = 0
M_torg = 0
FM_torg = 0

for item in List_torg:
	if item[0:] == ["None"]*3:
		pass
	elif item[0:2] == ["None"]*2 and item[2] != "None":
		M_torg += 1
	elif item[1:] == ["None"]*2 and item[0] != "None":
		F_torg += 1
	elif [item[0],item[2]] == ["None"]*2 and item[1] != "None":
		L_torg += 1
	elif item[0:2] != ["None"]*2 and item[2] == "None":
		FL_torg += 1
	elif item[1:] != ["None"]*2 and item[0] == "None":
		LM_torg += 1
	elif [item[0],item[2]] != ["None"]*2 and item[1] == "None":
		FM_torg += 1
	elif item[0:] != ["None"]*3:
		FLM_torg += 1


a1 = FLM_torg
b1 = FL_torg
c1 = F_torg
d1 = LM_torg
e1 = L_torg
f1 = M_torg
g1 = FM_torg



fig1 = plt.figure()
venn3(subsets = (c1, e1, b1, f1, g1, d1, a1), set_labels = (set4, set5, set6))
fig1.savefig("Torg_alls" + '_venn3.pdf', format='PDF') #depends on the input sequence of the cluster_output file... in this case torgalensis was first and then carolitertii
plt.close(fig1)