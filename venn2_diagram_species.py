#!/usr/bin/python2.7

import sys
from matplotlib_venn import venn2
import matplotlib.pyplot as plt

#input cluster_output_6 with both species

argument_list = sys.argv
File1 = sys.argv[1]
InFile1 = open(File1, "r")

List_torg=[]
List_carol=[]

x = 0
for line1 in InFile1:
	line = line1.split("\t")
	ACC = line[0].strip()
	element1= line[1].strip()
	element2= line[2].strip()
	element3= line[3].strip()
	element4= line[4].strip()
	element5= line[5].strip()
	element6= line[6].strip()
#	print (ACC)
	if "comp" in ACC:
		pass
	else:
		if [element1, element2, element3] == ["None"]*3:
			pass
		else:
			List_carol.append(ACC)
		if [element4, element5, element6] == ["None"]*3:
			pass
		else:
			List_torg.append(ACC)


	
Set_torg = list(set(List_torg))
Set_carol = list(set(List_carol))
Intersection = list(set(Set_carol) & set(Set_torg))

print("torg", len(Set_torg))
print("carol", len(Set_carol))
print("inter", len(Intersection))
	

#print(t,c,tc)

fig = plt.figure()

venn2(subsets = (len(Set_torg)-len(Intersection),len(Set_carol)-len(Intersection) , len(Intersection)), set_labels = ("Torg", "Carol"))
fig.savefig("bothtranscriptomes" + '_venn2.pdf', format='PDF') 
plt.close(fig)
