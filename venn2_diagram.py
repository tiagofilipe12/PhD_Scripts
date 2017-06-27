#!/usr/bin/python2.7

import sys
from matplotlib_venn import venn2
import matplotlib.pyplot as plt

argument_list = sys.argv
File1 = sys.argv[1]
InFile1 = open(File1, "r")

List_fins=[]
List_liver=[]
List_muscle=[]
x = 0
for line1 in InFile1:
	line = line1.split("\t")
	element1= line[2].strip()
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
	
	List_fins.append([element1,element4])
	List_liver.append([element2,element5])
	List_muscle.append([element3,element6])

t = 0
c = 0
tc = 0

for item in List_fins:
	if item[0:] == ["None"]*2:
		pass
	elif item[0] == "None" and item[1] != "None":
		c += 1 
	elif item[1] == "None" and item[0] != "None":
		t += 1
	elif item[0:] != ["None"]*2:
		tc +=1

print(t,c,tc)

fig_fins = plt.figure()

venn2(subsets = (t, c, tc), set_labels = (set1, set4))
fig_fins.savefig("FinsUP_IDs" + '_venn2.pdf', format='PDF') 
plt.close(fig_fins)

t1 = 0
c1 = 0
tc1 = 0

for item in List_liver:
	if item[0:] == ["None"]*2:
		pass
	elif item[0] == "None" and item[1] != "None":
		c1 += 1 
	elif item[1] == "None" and item[0] != "None":
		t1 += 1
	elif item[0:] != ["None"]*2:
		tc1 += 1

fig_liver = plt.figure()

venn2(subsets = (t1, c1, tc1), set_labels = (set2, set5))
fig_liver.savefig("LiverUP_IDs" + '_venn2.pdf', format='PDF') 
plt.close(fig_liver)

t2 = 0
c2 = 0
tc2 = 0

for item in List_muscle:
	if item[0:] == ["None"]*2:
		pass
	elif item[0] == "None" and item[1] != "None":
		c2 += 1 
	elif item[1] == "None" and item[0] != "None":
		t2 += 1
	elif item[0:] != ["None"]*2:
		tc2 += 1

fig_muscle = plt.figure()

venn2(subsets = (t2, c2, tc2), set_labels = (set3, set6))
fig_muscle.savefig("MuscleUP_IDs" + '_venn2.pdf', format='PDF') 
plt.close(fig_muscle)