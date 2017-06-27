#!/usr/bin/python3

import sys
from matplotlib.mlab import PCA
import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
from collections import OrderedDict

argument_list = sys.argv
File1 = sys.argv[1]
output_tag = sys.argv[2]
analysisType = sys.argv[3]
InFile1 = open(File1, "r")

#Which Libraries do you want to compare?
x_lib=4
y_lib=7

X=[]
Labels=[]
GeneStorage=[]
genecounter=-1
for line in InFile1:
	genecounter += 1
	if analysisType == "pair":
		if line.startswith("geneName"):
			pass
		else:
			dataMatrix = []
			for x in [line.strip().split('\t')[x_lib], line.strip().split('\t')[y_lib]]:
				if x != "None":
					dataMatrix.append(float(x))
				else:
					dataMatrix.append(0.0)
			if dataMatrix[0] == 0.0 and dataMatrix[1] == 0.0:
				genecounter -= 1
				pass
			else:
				X.append(dataMatrix)
				GeneStorage.append(line.strip().split('\t')[0])

	else: 
		if line.startswith("geneName"):
			for x in line.strip().split('\t')[x_lib:y_lib]:
				Labels.append(x)
		else:
			dataMatrix = []
			for x in line.strip().split('\t')[x_lib:y_lib]:
				if x != "None":
					dataMatrix.append(float(x))
				else:
			 		dataMatrix.append(0.0)
			X.append(dataMatrix)

data = np.array(X)
results = PCA(data)

#this will return an array of variance percentages for each component
PCvariance=results.fracs
# Construct a bar plot for Principal component variance
fig = pl.figure()
ax = fig.add_subplot(1,1,1)
ind=range(len(PCvariance))
ax.bar(ind, PCvariance, facecolor='#777777', align="center")
ax.set_ylabel('Variance')
ax.set_title('Variance of each component')
ax.set_xticks(ind)
ax.set_xticklabels(['PC1','PC2','PC3','PC4','PC5','PC6']) 			#for 6 PC... for more, under devolopment

# Extremely nice function to auto-rotate the x axis labels.
# It was made for dates (hence the name) but it works
# for any long x tick labels

fig.autofmt_xdate()
# plot barplot
fig.savefig(output_tag + '_variance_PCA.pdf', format='PDF')
#this will return a 2d array of the data projected into PCA space
PCA_array=results.Y
#returns the eigen values for each of the PC in the library order
EigenValue=results.Wt
##construct a 2D PCA
x1 = []
y1 = []
z1 = []
for item in PCA_array:
	x1.append(item[0])
	y1.append(item[1])
	if analysisType != "pair":
		z1.append(item[2])

e1 = []
e2 = []
e3 = []
for item in EigenValue:
	e1.append(item[0])
	e2.append(item[1])
	if analysisType != "pair":
		e3.append(item[2])

#print(e1,e2,e3)

fig2 = plt.figure()
ax2 = fig2.add_subplot(1,1,1)
#ax2.grid(True, linestyle="-", color="0.75")
pltData2 = [x1,y1]
pltEigen2 = [e1,e2]
plt.scatter(pltData2[0], pltData2[1])
plt.scatter(pltEigen2[0],pltEigen2[1], color="red")			#Falta ver como é que se mete os red para a frente e como meter labels de alguma forma nos pontos red

# make simple, bare axis lines through space:
xAxisLine2 = ((min(pltData2[0]), max(pltData2[0])), (0,0)) # 2 points make the x-axis line at the data extrema along x-axis 
ax2.plot(xAxisLine2[0], xAxisLine2[1], 'r') # make a red line for the x-axis.
yAxisLine2 = ((0,0), (min(pltData2[1]), max(pltData2[1]))) # 2 points make the y-axis line at the data extrema along y-axis
ax2.plot(yAxisLine2[0], yAxisLine2[1], 'r') # make a red line for the y-axis.

# label the axes 
ax2.set_xlabel("PC1") 
ax2.set_ylabel("PC2")
ax2.set_title("PCA")
fig2.savefig(output_tag +'_2D_PCA.pdf', format='PDF')


if analysisType == "pair":
	pass
else:
##construct a 3D PCA
	from mpl_toolkits.mplot3d import Axes3D


#plt.close('all') # close all latent plotting windows
	fig1 = plt.figure() # Make a plotting figure
	ax = Axes3D(fig1) # use the plotting figure to create a Axis3D object.
	pltData = [x1,y1,z1]
	pltEigen = [e1,e2,e3]
	ax.scatter(pltData[0], pltData[1], pltData[2], 'bo') # make a scatter plot of blue dots from the data
	ax.scatter(pltEigen[0],pltEigen[1], pltEigen[2], color="red")

 
# make simple, bare axis lines through space:
	xAxisLine = ((min(pltData[0]), max(pltData[0])), (0, 0), (0,0)) # 2 points make the x-axis line at the data extrema along x-axis 
	ax.plot(xAxisLine[0], xAxisLine[1], xAxisLine[2], 'r') # make a red line for the x-axis.
	yAxisLine = ((0, 0), (min(pltData[1]), max(pltData[1])), (0,0)) # 2 points make the y-axis line at the data extrema along y-axis
	ax.plot(yAxisLine[0], yAxisLine[1], yAxisLine[2], 'r') # make a red line for the y-axis.
	zAxisLine = ((0, 0), (0,0), (min(pltData[2]), max(pltData[2]))) # 2 points make the z-axis line at the data extrema along z-axis
	ax.plot(zAxisLine[0], zAxisLine[1], zAxisLine[2], 'r') # make a red line for the z-axis.
 
# label the axes 
	ax.set_xlabel("PC1") 
	ax.set_ylabel("PC2")
	ax.set_zlabel("PC3")
	ax.set_title("PCA")

	fig1.savefig(output_tag +'_3D_PCA.pdf', format='PDF') # show the plot

print(genecounter)
# construct a confused stacked bar plot # maybe a better policy would be to filter the output somehow... 
# maybe for the major differences between both species. Largura das barras optimizada para 100 genes
if analysisType == "pair":
	ind=np.arange(genecounter)


#	PairwiseList = []
	

	DifList= []
	dic_list = {}
	cycle = -1 
	color_code = []
	for value in X:
		cycle += 1
		if cycle < genecounter:
			if value[0] >= 0.0 and value[1] >= 0.0:
				dif = abs(value[0]+value[1])
				if value[0] == 0.0:
					code = "red"
				elif value[1] == 0.0:
					code = "blue"
				else:
					code = "black"	# ha demasiados black no top100... deve haver um problema com esta condição
			elif value[0] < 0.0 and value[1] < 0.0:
				dif = abs(value[0]+value[1])
				code = "grey"
			else:
				dif = abs(value[0] - 0) + abs(value[1] - 0)
				if value[0] == 0.0:
					code = "blue"
				elif value[1] == 0.0:
					code = "red"
			DifList.append(dif)
			color_code.append(code)
			dic_list[GeneStorage[cycle]] = DifList[cycle], color_code[cycle]#, data
		else:
			break

#	print(dic_list)
	dic_sorted = OrderedDict(sorted(dic_list.items(), key=lambda t: t[1], reverse=True))
#	print(dic_sorted)
#	print(GeneStorage)
#	print(DifList)
#	print(data)

	#escolher apenas os top 100. Pode ser editado para qualquer valor desde que se altere o valor de a dentro da condição if
	dif_bar = []
	dif_label = []
	dif_bar_color = []
	a = 0
#	print(dic_sorted.keys())
	for syn in dic_sorted.items():
#		print(syn[1])
		if a < 100:
			dif_label.append(syn[0])
			a += 1
			dif_bar.append(syn[1][0])
			dif_bar_color.append(syn[1][1])
		elif a >= 100:
			break
#	print(dif_label)
	print(dif_bar)
	print(dif_bar_color)
#	ind=np.arange(a)
	fig3 = plt.figure(figsize=(15, 8), dpi=300)
	ax = plt.subplot(2,1,1)
	w = 0.4
	p1 = ax.bar(range(len(dif_bar)), dif_bar, width=0.2, color='blue', edgecolor='blue', align="center")
	#p2 = ax.bar(ind+w, torg, width=0.2, color='#B0B0B0', edgecolor= '#B0B0B0', align="center")#, bottom=carol)
	ax.autoscale(tight=True, axis='x')


	plt.ylabel('Difference in log(Fold Change) between\nS. carolitetii and S. Torgalensis')
	plt.title('Top 100 Most differentially expressed transcripts')
	ax.set_xticks(range(len(dif_label)))
	ax.set_xticklabels(dif_label, rotation=60, size=6, rotation_mode="anchor", position=(0, 0), ha='right')
	ax.set_xlabel("genes")
#	plt.yticks(np.arange(0,81,10))
#	ax.legend( (p1[0], p2[0]), ('Carol', 'Torg') )

	fig3.savefig(output_tag +'bars.pdf', format='PDF')