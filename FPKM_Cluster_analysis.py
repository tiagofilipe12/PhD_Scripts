#!/usr/bin/python3

## This script is intended to merge data from different RSEM outputs with the extension .FPKM

     
import sys
from collections import OrderedDict
     
def parse_file (input_file):
     
		file_handle = open(input_file)
		next(file_handle)

		dic ={}

		for line in file_handle:
			tab_split = line.split("\t")
			dic[tab_split[0].strip()]=tab_split[1].strip() + "\t" + tab_split[2].strip()

#			dic.setdefault(tab_split[0].strip(), []).append(tab_split[1].strip())
#			dic.setdefault(tab_split[0].strip(), []).append(tab_split[2].strip())

     
		return dic
     
def write_master_dic (dic_list, output_file):
     
        output_handle = open(output_file,"w")
        master_dic = OrderedDict()
     
        for name, dic in dic_list.items():
                for key in dic:
                        if key in master_dic:
                                master_dic[key].append(name)
                        elif key not in master_dic:
                                master_dic[key] = [name]
     

     
        for key, file_name_list in master_dic.items():
                converted_list = []
                for file_name in dic_list:
                        if file_name in file_name_list:
                                converted_list.append(dic_list[file_name][key])
                        else:
                                converted_list.append("0.00")
                output_handle.write(key+"\t"+"\t".join(converted_list)+"\n")
     
        return 0
     
def main():
     
        dic_list = OrderedDict()
        output_file = "Cluster_output_FPKM"
     
        for input_file in sys.argv[1:]:
                current_dic = parse_file(input_file)
                dic_list[input_file] =  current_dic
     
        write_master_dic (dic_list, output_file)
     
main()



