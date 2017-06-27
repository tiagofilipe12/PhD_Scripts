#!/usr/bin/python3

## qpcr_workflow.py v.0.6
##Input format:
## Condition\tSample name\t mean Cq (Three columns)
## because many of the steps before this analysis are dependent on the user this script does not accept as input the output from biorad software
## Also replicates must be processed before using this script because the user may want to discard some replicates.
## Reference gene normalization factors are also required for the following calculations
## Statistics implemented, however Dunn's test is not available and so an output file (containing the data frame for multiple comparison tests) is generated in case Dunn's test are required

## Author: T. F. Jesus
## Year: 2015
## Last update: 13-03-2015

import argparse, os
from collections import OrderedDict
import math
import statistics
import matplotlib.pyplot as plt
import sys
from scipy import stats
#import numpy as np
import pandas as pd
from statsmodels.stats.multicomp import (pairwise_tukeyhsd, MultiComparison)

## Parse the inputs and options

parser = argparse.ArgumentParser(description="qpcr_workflow, from cts do expression values (also includes statistics)")

parser.add_argument("-in",dest="input_file", required=True, help="Provide the input file name")
parser.add_argument("-ref",dest="ref_file", required=True, help="Provide the input file with references geometric mean")
parser.add_argument("-eff",dest="eff_value", default="None",help="Provide the value for efficiency for this gene, otherwise efficiency will be considered 2")
parser.add_argument("-log",dest="log_transformation",action="store_const", const=True, help="log10 transformation method for highly variable replicates. Outputs to different files than normal output.")
parser.add_argument("-st",dest="statistics",action="store_const", const=True, help="performes statistical analysis (Shapiro-Wilk, levenne's test, ANOVA and tukey hsd (including nonparametrics)")
parser.add_argument("-g",dest="graphic",action="store_const", const=True, help="outputs graphics with expression values for each condition")

arg = parser.parse_args()
InFile = arg.input_file
Refs = arg.ref_file
efficiencies = arg.eff_value
data_transformation = arg.log_transformation
sts = arg.statistics
graphics = arg.graphic

## get the input files directory
path = os.path.dirname(InFile)# + "/"

## Opens inputs
Input_file = open(InFile, "r")
RefsFile = open(Refs, "r")

######## Preamble - common to all the analyses ###########

## makes a dictionary with normalization values for several reference genes... that must be done a priori in excel (for example)
## this file must have a two column with sample name and geom mean already calculated for samples

ref_dic = {}

for line in RefsFile:
	tab_split = line.split("\t")
	Sample_name = tab_split[1].strip()
	Geom_mean = tab_split[2].strip()
	ref_dic[Sample_name] = float(Geom_mean)


## Preparing the output files
outFile = open(InFile[:-4] + "_non_transformed_data.txt", "w")
outFile.write("*** Descriptive statistics section ***\n")

## Checks the data transformation option from willems et al 2008

try:
	data_transformation
except NameError:
	data_transformation = None

## Calculates the means and s.d  using no transformation on data
dic = OrderedDict()

for line in Input_file:
	tab_split = line.split("\t")
#	Gene = tab_split[0].strip()
	condition = tab_split[0].strip()
	Sample_name = tab_split[1].strip()
	Cq = tab_split[2].strip()
	Float_Cq = float(Cq)
	dic[(Sample_name, condition)] = Float_Cq

List_keys_dic = list(x[-1] for x in dic.keys())
control_seq = List_keys_dic[0]
print("Control condition: " + control_seq)


## calculating mean Cq for control condition
L=[]
for k, v in dic.items():
	if control_seq == k[-1]:
		L.append(v)

Mean_Cq_Control = sum(L)/float(len(L))
print("Mean of the control: " + str(Mean_Cq_Control))

dic_calcs = OrderedDict()
for k, v in dic.items():
	delta_Cq = pow(float(efficiencies), Mean_Cq_Control - v)/ref_dic[k[0]]
	dic_calcs[k] = delta_Cq

############# calculating mean and s.d of ratios normalized for each condition - no data transformation #############
L_conditions= []
L_ratios = []
L_means = []
L_stdev = []
L_means_norm = []
L_stdev_norm = []
treatments = []
L_lower_errorbar = [] ## a list used to eliminate the lower variance bar in the plot section
x = 1 ## used to append the first entry in L_ratios list
y = 1 ## used to store the mean of first L_ratios, i.e, control condition for normalization purposes in next section.
print("Mean and stdev of conditions: ")
outFile.write("\nMean and stdev of conditions: \n")
for k, v in dic_calcs.items():
	L_conditions.append(k[1])
	if x == 1:
		L_ratios.append(v)
		x = 0
	else:
#		print(k[1], L_conditions[-1])
#		print(L_ratios)
		if k[1] == L_conditions[-2]:
			L_ratios.append(float(v))
		else:
			mean = statistics.mean(L_ratios)
			stdev = statistics.stdev(L_ratios)
			L_means.append(mean)
			L_stdev.append(stdev)
			treatments.append(L_conditions[-2])
			L_lower_errorbar.append(0)
			print("Raw mean and stdev: " + L_conditions[-2], mean, stdev)
			outFile.write("Raw mean and stdev: " + "\t" + L_conditions[-2] + "\t" + str(mean) + "\t" + str(stdev) + "\n")
			if y == 1:
				control_mean = mean
			else:
				pass
			mean_norm = mean/control_mean
			stdev_norm = stdev/control_mean
			L_means_norm.append(mean_norm)
			L_stdev_norm.append(stdev_norm)
			print("Normalized mean and stdev: " + L_conditions[-2], mean_norm, stdev_norm)
			outFile.write("Normalized mean and stdev: " + "\t" + L_conditions[-2] + "\t" + str(mean_norm) + "\t" + str(stdev_norm) + "\n")
			y = 2
			L_ratios=[]
			L_ratios.append(float(v))
		

print("For control purposes, this is the mean of the control condition: " + str(control_mean))

## no normalization formula
mean = statistics.mean(L_ratios)
stdev = statistics.stdev(L_ratios)
L_means.append(mean)
L_stdev.append(stdev)
treatments.append(L_conditions[-2])
L_lower_errorbar.append(0)
print("Raw mean and stdev: " +L_conditions[-2], mean, stdev)

## normalized mean and stdev relative to control condition formula

mean_norm = mean/control_mean
stdev_norm = stdev/control_mean
L_means_norm.append(mean_norm)
L_stdev_norm.append(stdev_norm)
print("Normalized mean and stdev: " + L_conditions[-2], mean_norm, stdev_norm)
outFile.write("Raw mean and stdev: " + "\t" + L_conditions[-2] + "\t" + str(mean) + "\t" + str(stdev) + "\n" + "Normalized mean and stdev: " + "\t" + L_conditions[-2] + "\t" + str(mean_norm) + "\t" + str(stdev_norm) + "\n")

## Block for graphic output ##
## only normalized data will be plotted given that this is the one that we want to show to readers when writting a manuscri

if graphics == None:
	pass
else:
	# input data
	mean_values = [x - 1 for x in L_means_norm]
	variance_upper = L_stdev_norm
	variance_lower = L_lower_errorbar
	bar_labels = treatments

	# plot bars
	x_pos = list(range(len(bar_labels)))
	rects = plt.bar(x_pos, mean_values, bottom=1, yerr=(variance_lower,variance_upper), color="grey", edgecolor="black", ecolor='black', align='center', alpha=1, log=True)

	# set height of the y-axis
	max_y = max(zip(mean_values, variance_upper)) # returns a tuple, here: (3, 5)
	min_y = min(mean_values)
	plt.yscale('log')
	plt.axhline(1, color='black')

	# set axes labels and title
	plt.ylabel('Ratio')
	plt.xticks(x_pos, bar_labels)
	plt.title('Expression values')

	#plt.show()
	plt.savefig(InFile[:-4] + '_plot_non_transformed_data.pdf')
	plt.close()


############ Statistical analysis ###########

##store some lists for statistic calculations and makes a dictionary that provides a list of values per treatment as key.
if sts == None:
	pass
else:
	outFile.write("\n*** Test statistics section ***\n")
	L_conditions=["None"]
	treatments = []
	dic=OrderedDict()
	L_tukey = []
	x = 0
	y = 1 		#corresponds to control condition
	for k,v in dic_calcs.items():
		L_tukey.append(v)
		if x == 0:		
			dic.setdefault(k[1],[]).append(v)
			L_conditions.append(k[1])
			x += 1
		else:
			L_conditions.append(k[1])
			if k[1] != L_conditions[-2]:
				y += 1
				treatments.append(L_conditions[-2])
				dic.setdefault(k[1],[]).append(v)
			else:
				dic.setdefault(k[1],[]).append(v)

	treatments.append(L_conditions[-1])

## pandas block used for tukey test and multiple comparison test output (por fazer ainda...)

	del L_conditions[0]
	data = pd.DataFrame({"exog": pd.Series(L_conditions), "endog": pd.Series(L_tukey)})
	print("\n***Check pandas data frame!***")
	print(data)
	## end of pandas block

	## shapiro wilk test
	outFile.write("\n***Shapiro-Wilk test - p-value > 0.05 means that sample distribution is normal***\n")
	print("\n***Shapiro-Wilk test - p-value > 0.05 means that sample distribution is normal***\n")
	for k in dic.keys():
		shapiro = stats.shapiro(dic[k])
		print(k, " p-value=",shapiro[1])
		outFile.write(k + "\t" + " p-value = " + str(shapiro[1]) + "\n")


	##Levenne's test new
	outFile.write("\n***Levenne's test - p-value > 0.05 means that sample are homocedastic***\n")
	print("\n***Levenne's test - p-value > 0.05 means that sample are homocedastic***")
	levenne = stats.levene(*dic.values())
	print("Levenne's test: p-value: ", levenne[1])
	outFile.write("Levenne's test: p-value = " + str(levenne[1]) + "\n")

	## anova new	
	## by default the two types of anova will be performed and the user must decide which one to use, since sometimes ignoring
	## some deviations from normality or homocedasticity is better than using nonparametrics

	anova = stats.f_oneway(*dic.values()) 
	anova_kruskal = stats.kruskal(*dic.values())
	outFile.write("\n***ANOVA (parametrics and nonparametrics) - p-value < 0.05 means that the null hypothesis is rejected and that there are differences between treatments***")
	outFile.write("\nNon-parametric Kruskal Wallis test statistics, P-value = " + str(anova_kruskal[0]) + ", " + str(anova_kruskal[1]) + "\n")
	outFile.write("One-way ANOVA F-statistics, P-value = " + str(anova[0]) + ", " + str(anova[1]) + "\n")
	print("\n***ANOVA (parametrics and nonparametrics) - p-value < 0.05 means that the null hypothesis is rejected and that there are differences between treatments***")
	print("Non-parametric Kruskal Wallis test statistics, P-value =", anova_kruskal[0], ", ", anova_kruskal[1])
	print("One-way ANOVA F-statistics, P-value = ", anova[0], ", ", anova[1], "\n")
	tukey = pairwise_tukeyhsd(data["endog"], data["exog"]) 
	tukey_01 = pairwise_tukeyhsd(data["endog"], data["exog"], alpha=0.1)
	outFile.write("\n" + str(tukey) + "\n" + str(tukey_01))
	print(tukey, "\n",tukey_01)
	data.to_csv(path + InFile[:-4] + "_multiple_comparisons_pandas.csv")
		
############### Log10 data transformation for qPCR data with high variance. #######################

log_dic_calcs = OrderedDict()
if data_transformation == None:
	print("No data transformation was applied. Done!")
	sys.exit()
else:
	outFile_log = open(InFile[:-4] + "_log_transformed_data.txt", "w")
	outFile_log.write("*** Descriptive statistics section ***\n")
	for k, v in dic_calcs.items():
		log_data = math.log10(v + 1)		# aqui provavelmente terá de ser log (x+1) e não log(x)
		log_dic_calcs[k] = log_data

	L_conditions= []
	L_ratios = []
	L_means = []
	L_stdev = []
	L_means_norm = []
	L_stdev_norm = []
	treatments = []
	L_lower_errorbar = [] ## a list used to eliminate the lower variance bar in the plot section
	x = 1 ## used to append the first entry in L_ratios list
	y = 1 ## used to store the mean of first L_ratios, i.e, control condition for normalization purposes in next section.
	print("\nLog Mean and stdev of conditions: ")
	for k, v in log_dic_calcs.items():
		L_conditions.append(k[1])
		if x == 1:
			L_ratios.append(v)
			x = 0
		else:
#		print(k[1], L_conditions[-1])
#		print(L_ratios)
			if k[1] == L_conditions[-2]:
				L_ratios.append(float(v))
			else:
				mean = statistics.mean(L_ratios)
				stdev = statistics.stdev(L_ratios)
				L_means.append(mean)
				L_stdev.append(stdev)
				treatments.append(L_conditions[-2])
				L_lower_errorbar.append(0)
				print("Raw mean and stdev: " + L_conditions[-2], mean, stdev)
				outFile_log.write("Raw mean and stdev: " + "\t" + L_conditions[-2] + "\t" + str(mean) + "\t" + str(stdev) + "\n")
				if y == 1:
					control_mean = mean
				else:
					pass
				mean_norm = pow(10,mean)/pow(10,control_mean)
				stdev_norm = pow(10,stdev)/pow(10,control_mean)
				L_means_norm.append(mean_norm)
				L_stdev_norm.append(stdev_norm)
				print("Normalized mean and stdev: " + L_conditions[-2], mean_norm, stdev_norm)
				outFile_log.write("Normalized mean and stdev: " + "\t" + L_conditions[-2] + "\t" + str(mean_norm) + "\t" + str(stdev_norm) + "\n")
				y = 2
				L_ratios=[]
				L_ratios.append(float(v))
		

	print("For control purposes, this is the mean of the control condition: " + str(control_mean))

	## no normalization formula
	mean = statistics.mean(L_ratios)
	stdev = statistics.stdev(L_ratios)
	L_means.append(mean)
	L_stdev.append(stdev)
	treatments.append(L_conditions[-2])
	L_lower_errorbar.append(0)
	print("Raw mean and stdev: " +L_conditions[-2], mean, stdev)

## normalized mean and stdev relative to control condition formula

	mean_norm = pow(10,mean)/pow(10,control_mean)
	stdev_norm = pow(10,stdev)/pow(10,control_mean)
	L_means_norm.append(mean_norm)
	L_stdev_norm.append(stdev_norm)
	print("Normalized mean and stdev: " + L_conditions[-2], mean_norm, stdev_norm)
	outFile_log.write("Raw mean and stdev: " + "\t" + L_conditions[-2] + "\t" + str(mean) + "\t" + str(stdev) + "\n" + "Normalized mean and stdev: " + "\t" + L_conditions[-2] + "\t" + str(mean_norm) + "\t" + str(stdev_norm) + "\n")

## Block for graphic output ##
## only normalized data will be plotted given that this is the one that we want to show to readers when writting a manuscri

	if graphics == None:
		pass
	else:
		# input data
		mean_values = [x - 1 for x in L_means_norm]
		variance_upper = L_stdev_norm
		variance_lower = L_lower_errorbar
		bar_labels = treatments

		# plot bars
		x_pos = list(range(len(bar_labels)))
		rects = plt.bar(x_pos, mean_values, bottom =1, yerr=(variance_lower,variance_upper), color="grey", edgecolor="black", ecolor='black', align='center', alpha=1, log=True)

		# set height of the y-axis
		max_y = max(zip(mean_values, variance_upper)) # returns a tuple, here: (3, 5)
		min_y = min(mean_values)
		plt.yscale('log')

		plt.axhline(1, color='black')

		plt.ylabel('log10(Ratio)')
		plt.xticks(x_pos, bar_labels)
		plt.title('log transformed expression values')

		#plt.show()
		plt.savefig(InFile[:-4] + '_plot_log_transformed_data.pdf')
		plt.close()

############ Statistical analysis log transformed data###########

##store some lists for statistic calculations and makes a dictionary that provides a list of values per treatment as key.
if sts == None:
	pass
else:
	outFile_log.write("\n*** Test statistics section ***\n")
	L_conditions=["None"]
	treatments = []
	dic=OrderedDict()
	L_tukey = []
	x = 0
	y = 1 		#corresponds to control condition
	for k,v in log_dic_calcs.items():
		L_tukey.append(v)
		if x == 0:		
			dic.setdefault(k[1],[]).append(v)
			L_conditions.append(k[1])
			x += 1
		else:
			L_conditions.append(k[1])
			if k[1] != L_conditions[-2]:
				y += 1
				treatments.append(L_conditions[-2])
				dic.setdefault(k[1],[]).append(v)
			else:
				dic.setdefault(k[1],[]).append(v)

	treatments.append(L_conditions[-1])

## pandas block used for tukey test and multiple comparison test output (por fazer ainda...)

	del L_conditions[0]
	data = pd.DataFrame({"exog": pd.Series(L_conditions), "endog": pd.Series(L_tukey)})
	print("\n***Check pandas data frame!***")
	print(data)
	## end of pandas block

	## shapiro wilk test
	print("\n***Shapiro-Wilk test - p-value > 0.05 means that sample distribution is normal***")
	outFile_log.write("\n***Shapiro-Wilk test - p-value > 0.05 means that sample distribution is normal***\n")
	for k in dic.keys():
		shapiro = stats.shapiro(dic[k])
		print(k, " p-value=",shapiro[1])
		outFile_log.write(k + "\t" + " p-value = " + str(shapiro[1]) + "\n")

	##Levenne's test new	
	print("\n***Levenne's test - p-value > 0.05 means that sample are homocedastic***")
	outFile_log.write("\n***Levenne's test - p-value > 0.05 means that sample are homocedastic***\n")
	levenne = stats.levene(*dic.values())
	print("Levenne's test: p-value: ", levenne[1])
	outFile_log.write("Levenne's test: p-value = " + str(levenne[1]) + "\n")

	## anova new	
	## by default the two types of anova will be performed and the user must decide which one to use, since sometimes ignoring
	## some deviations from normality or homocedasticity is better than using nonparametrics

	anova = stats.f_oneway(*dic.values()) 
	anova_kruskal = stats.kruskal(*dic.values())
	outFile_log.write("\n***ANOVA (parametrics and nonparametrics) - p-value < 0.05 means that the null hypothesis is rejected and that there are differences between treatments***")
	outFile_log.write("\nNon-parametric Kruskal Wallis test statistics, P-value = " + str(anova_kruskal[0]) + ", " + str(anova_kruskal[1]))
	outFile_log.write("\nOne-way ANOVA F-statistics, P-value = " + str(anova[0]) + ", " + str(anova[1]) + "\n")
	print("\n***ANOVA (parametrics and nonparametrics) - p-value < 0.05 means that the null hypothesis is rejected and that there are differences between treatments***")
	print("Non-parametric Kruskal Wallis test statistics, P-value =", anova_kruskal[0], ", ", anova_kruskal[1])
	print("One-way ANOVA F-statistics, P-value = ", anova[0], ", ", anova[1], "\n")
	tukey = pairwise_tukeyhsd(data["endog"], data["exog"]) 
	tukey_01 = pairwise_tukeyhsd(data["endog"], data["exog"], alpha=0.1)
	outFile_log.write("\n" + str(tukey) + "\n" + str(tukey_01))
	print(tukey, "\n",tukey_01)
	data.to_csv(path + InFile[:-4] + "_multiple_comparisons_log_pandas.csv")
 

########## Obsolete code... ###########

# compute one-way ANOVA P value   OBSOLETE ##################
#anova = stats.f_oneway(dic[treatments[0]],dic[treatments[1]],dic[treatments[2]],dic[treatments[3]])  
#levenne = stats.levene(dic[treatments[0]],dic[treatments[1]],dic[treatments[2]],dic[treatments[3]])
#print("One-way ANOVA F-statistics, P-value =", anova)
#print("p-value> 0.05 --> samples are homocedastic ", levenne[1])

##Obsolete... 
#shapiro = [(stats.shapiro(dic[treatments[0]]),stats.shapiro(dic[treatments[1]]),stats.shapiro(dic[treatments[2]]),stats.shapiro(dic[treatments[3]]))]
#print(shapiro)

## Non parametric statistics... still without multiple comparisons OBSOLETE
#anova_kruskal = stats.kruskal(dic[treatments[0]],dic[treatments[1]],dic[treatments[2]],dic[treatments[3]])

#print("Non-parametric One-way ANOVA F-statistics, P-value =", anova_kruskal)