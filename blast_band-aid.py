#!/usr/bin/python3

## blast_band-aid.py v1.0.0
##
## blast_band-aid.py replaces the previous version blast_wrapper_aid.py and adds two main functions: Removal of duplicated contigs either from XML files or fasta files.
## This script is intended not only to generate a fasta file to resume a blast run provided the original fasta and blast results, but it also intends to remove duplicated 
## blast entries from the XML file that may be generated when using blast.py (https://github.com/tiagofilipe12/blast_wrapper), either because you made some mistake and cat
## wrong XMLs or either you were distracted like me and forgot which files to cat. The script also removes duplicated contigs from fasta files either with 'both' or 
##'fasta' options.
## Note that this script does not concatenate the several XML files that one blast run may generate due to errors or broken pipes and thus it is your responsability to cat
## the desired XML files into one XML file that can be given to blast_band-aid.py. This is intentional so the user pay attetion to what is being cat before any filter.
## Script works under BLASTX 2.2.29+, for different versions that changed the XML format it may not work properly, so use it with caution.
##
## Author: T. F. Jesus
## Year: 2014
## Last update: 29-01-2014

import os
import sys
import argparse

## Parse the inputs and options

parser = argparse.ArgumentParser(description="BLAST wrapper band-aid: Filters a fasta file using blast XML format and/or removes duplicated entries from blast XML files")

parser.add_argument("-f",dest="fasta_input",help="Provide the FASTA input file name")
parser.add_argument("-x",dest="xml_input",help="Provide the XML input file name")
parser.add_argument("-filter",dest="filter_option",required=True,default="both",choices=["both","fasta","xml"],help="Select the file(s) to filter (default is '%(default)s'). '%(default)s' option also removes duplicated entries from blast XML files. 'fasta' option removes duplicated sequences from the fasta generating a new one")
parser.add_argument("-rm",dest="remove_fasta",help="Provide the text input file name with sequences to remove from fasta")


arg = parser.parse_args()
fasta_in = arg.fasta_input
xml_in = arg.xml_input
filter_type = arg.filter_option
remove_seq = arg.remove_fasta
Warn = ""


## This options removes duplicated entries from XML files generated by blast+. This XML parser may be useful to parse anything in this type of XML file, however for now it is limited.

if "xml" in filter_type:
        ## Open input files

        XMLFile = open(xml_in, "r")

        ## Write output files
        xml_filtered = xml_in + "_filtered.xml"
        if os.path.exists(xml_filtered):
                condition = input("The file %s already exists.\n\nDo you want to overwrite it? (y/n): " % xml_filtered)
                if condition == "y":
                        pass
                elif condition == "n":
                        sys.exit("Exiting")
                else:
                        sys.exit("Option %s not recognized. Exiting!\n" % condition)

        xml_out_File = open(xml_filtered, "w")
        duplicates_File = open(xml_in + "_duplicates.txt", "w")

        ## Variables useful to control the loop used for XML parsing and/or for descriptive purposes

        all_records = 0 		# descriptive
        number_of_duplicates = 0	# descriptive
        record_list = []		# Used to filter for duplicated contigs and also descriptive
        duplicates_list = []		# descriptive - one can access the list of duplicated contigs in the .txt generated
        counter = 0			# Used to control when to stop appending to entry_storage variable. When = 0 stops appending and write to output XML.

        ## XML parser
        # Despite quite specific this parser can be adapted for several types of filters
        for line in XMLFile:
                if "xml version=" in line:
                        entry_storage=[]
                        entry_storage.append(line)
                        counter = 1
                elif "</BlastOutput>" in line:
                        entry_storage.append(line+"\n")
                        counter = 0
                        for element in entry_storage:
                                xml_out_File.write(element)
                elif counter == 1:
                        entry_storage.append(line)
                        if "BlastOutput_query-def" in line:
                                line_split = line.split(">")[1].split("<")[0]
                                all_records += 1 
                                if line_split in record_list:
                                        number_of_duplicates += 1
                                        duplicates_list.append(line_split)
                                        Warn = "true"
                                        entry_storage = []
                                        counter = 0
                                elif line_split not in record_list:
                                        record_list.append(line_split)
                
          

        # Generate the txt file containing the list of duplicated entries
        duplicates_File.write("Duplicated contigs\n" + "\n".join(duplicates_list))

        print(str(all_records) + " total number of entries")
        if Warn == "true":
                print("\033[1m" +"WARNING: " + "\033[0m" + str(number_of_duplicates) + " duplicated entries were found")
        else:
                pass

        print(str(len(record_list)) + " sequences blasted")

## This option already removes duplicated entries from the fasta file since it uses a record_list from the XML file without duplicated contigs

elif "both" in filter_type:

        ##### This first block is exactly equal to the block above, until I figure a way to resume this code..... xD ######
        ## Open input files

        XMLFile = open(xml_in, "r")

        ## Write output files
        xml_filtered = xml_in + "_filtered.xml"
        if os.path.exists(xml_filtered):
                condition = input("The file %s already exists.\n\nDo you want to overwrite it? (y/n): " % xml_filtered)
                if condition == "y":
                        pass
                elif condition == "n":
                        sys.exit("Exiting")
                else:
                        sys.exit("Option %s not recognized. Exiting!\n" % condition)

        xml_out_File = open(xml_filtered, "w")
        duplicates_File = open(xml_in + "_duplicates.txt", "w")

        ## Variables useful to control the loop used for XML parsing and/or for descriptive purposes

        all_records = 0                 # descriptive
        number_of_duplicates = 0        # descriptive
        record_list = []                # Used to filter for duplicated contigs and also descriptive
        duplicates_list = []            # descriptive - one can access the list of duplicated contigs in the .txt generated
        counter = 0                     # Used to control when to stop appending to entry_storage variable. When = 0 stops appending and write to output XML.

        ## XML parser
        # Despite quite specific this parser can be adapted for several types of filters
        for line in XMLFile:
                if "xml version=" in line:
                        entry_storage=[]
                        entry_storage.append(line)
                        counter = 1
                elif "</BlastOutput>" in line:
                        entry_storage.append(line+"\n")
                        counter = 0
                        for element in entry_storage:
                                xml_out_File.write(element)
                elif counter == 1:
                        entry_storage.append(line)
                        if "BlastOutput_query-def" in line:
                                line_split = line.split(">")[1].split("<")[0]
                                all_records += 1 
                                if line_split in record_list:
                                        number_of_duplicates += 1
                                        duplicates_list.append(line_split)
                                        Warn = "true"
                                        entry_storage = []
                                        counter = 0
                                elif line_split not in record_list:
                                        record_list.append(line_split)
                
          

        # Generate the txt file containing the list of duplicated entries
        duplicates_File.write("Duplicated contigs\n" + "\n".join(duplicates_list))

        print(str(all_records) + " total number of entries")
        if Warn == "true":
                print("\033[1m" +"WARNING: " + "\033[0m" + str(number_of_duplicates) + " duplicated entries were found")
        else:
                pass

        print(str(len(record_list)) + " sequences blasted")

        ##### Block used to filter the fasta, that is not repeated #####
        FastaFile = open(fasta_in, "r")
        fasta_resume = fasta_in + "_resume"
        if os.path.exists(fasta_resume):
                condition = input("The file %s already exists.\n\nDo you want to overwrite it? (y/n): " % fasta_resume)
                if condition == "y":
                        pass
                elif condition == "n":
                        sys.exit("Exiting")
                else:
                        sys.exit("Option %s not recognized. Exiting!\n" % condition)
        outFile = open(fasta_resume, "w")
        counter = 0
        fasta_list = []
        x = 0
        y = 0
        z = 0
        for line in FastaFile:
                if line.startswith(">") and line[1:].split()[0] in fasta_list:
                        counter = 1
                        z += 1
                elif line.startswith(">") and line[1:].split()[0] not in fasta_list and line[1:].split()[0] in record_list:
                        counter = 1
                        y += 1
                elif line.startswith(">") and line[1:].split()[0] not in fasta_list and line[1:].split()[0] not in record_list:
                        fasta_list.append(line[1:].split()[0])
                        counter = 0
                        x += 1    
                        outFile.write(">%s\n" % (line[1:].split()[0]))
                elif counter == 0:
                        outFile.write(line)
        
        print("\n" + str(x) + " remaining sequences to blast\n" + str(x+y) + " total number of sequences\n" + "\033[1m" + str(z) + " duplicated sequence(s) removed" + "\033[0m")

# This option only removes duplicated contigs from the input fasta

elif "fasta" in filter_type:
        
        # Check if the -rm option is defined or absent and if present uses the specified file to create a list of sequences to be remove from the fasta file

        fasta_list = []
        if remove_seq == "None":
                pass
        elif remove_seq != "None":
                TXT_File = open(remove_seq, "r")
                for row in TXT_File:
                        fasta_list.append(row.rstrip("\n"))
                else:
                        pass

                print(str(len(fasta_list)) + " sequences removed by user")


        # Open the actual fasta to be cleaned for replicates and/or sequences specified by the user

        FastaFile = open(fasta_in, "r")
        fasta_clean = fasta_in + "_clean"
        if os.path.exists(fasta_clean):
                condition = input("The file %s already exists.\n\nDo you want to overwrite it? (y/n): " % fasta_clean)
                if condition == "y":
                        pass
                elif condition == "n":
                        sys.exit("Exiting")
                else:
                        sys.exit("Option %s not recognized. Exiting!\n" % condition)
#        outFile = open(fasta_clean, "w")       #removed today... repor caso seja necessário as sequencias a não remover.
        outFile2 = open(remove_seq + "_removed_seqs", "w")      #originalmente onde estava remove_seq era a variavel fasta_in
        counter= 0
        x = 0
        y = 0
        Warn2 = "false"
        for line in FastaFile:
                if line.startswith(">") and line[1:].split()[0] in fasta_list:
                        Warn2 = "true"
                        counter = 1
                        y = y + 1
                        outFile2.write(line)
                elif line.startswith(">") and line[1:].split()[0] not in fasta_list:
                        fasta_list.append(line[1:].split()[0])
                        counter = 0
                        x = x + 1
 #                       outFile.write(">%s\n" % (line[1:].split()[0]))         #removed today... repor caso seja necessário as sequencias a não remover.
 #               elif counter == 0:     #removed today... repor caso seja necessário as sequencias a não remover.
 #                       outFile.write(line)    #removed today... repor caso seja necessário as sequencias a não remover.
                elif counter == 1:
                        outFile2.write(line)

        print(str(x) + " unique sequences\n")
        if Warn2 == "true":
                print("\033[1m" +"WARNING: " + "\033[0m" + str(y) + " duplicated sequence(s)")
        else:
                os.remove(fasta_clean)
                print("There are no duplicated sequences")
