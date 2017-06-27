#!/usr/bin/python3
     
import sys
from collections import OrderedDict
     
def parse_file (input_file):
     
        file_handle = open(input_file)
        next(file_handle) # Skips first line
     
        data_storage = {} 
        ACC_storage = {}
        seqID_storage = {}


        for line in file_handle:
                tab_split = line.split("\t")
                seqName = tab_split[5].strip()
                ACC = tab_split[6].strip()
#                seqID = seqName + "\t" + ACC
                logFC = float(tab_split[1].strip())
                FDR = tab_split[4].strip()
                if float(FDR) < 0.0005:                         # FDR filter, one can change this option
                        if ACC == "None":
                                ACC = tab_split[0].strip()
                                ACC_storage.setdefault(ACC, []).append(logFC)
                                seqID_storage[ACC] = "unknown"
                        else:
                                ACC_storage.setdefault(ACC, []).append(logFC)
                                seqID_storage[ACC] = seqName



        for Accessions, logFCs in ACC_storage.items():
                logFC_mean = sum(logFCs)/len(logFCs)
#                Ided_ACC = Accessions + "\t" +seqID_storage[Accessions]
#                if abs(logFC_mean) > 0.58:                              # LogFC filter, that can also be changed, although the default means a log2(0.58) = 1.5 This option may be problematic here. IMPORTANT: IT IS HIGHLY DISINCORAGED THE USAGE OF THIS OPTION, SO KEEP COMMENTED
                data_storage[Accessions]=str(logFC_mean)
#                else:
#                       pass
                
        data_storage_ascending = OrderedDict(sorted(data_storage.items(), key=lambda t: t[0]))
#        data_storage_sorted = OrderedDict()

#        for k,v in data_storage_ascending.items():
#                data_storage_sorted[k]=v
     
        return data_storage_ascending
     
     
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
                                converted_list.append("None")
                output_handle.write(key+"\t"+"\t".join(converted_list)+"\n")
     
        return 0
     
def main():
     
        dic_list = OrderedDict()
        output_file = "Cluster_output_6"
     
        for input_file in sys.argv[1:]:
                current_dic = parse_file(input_file)
                dic_list[input_file] =  current_dic
     
        write_master_dic (dic_list, output_file)
     
main()