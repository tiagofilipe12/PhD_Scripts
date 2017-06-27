#!/usr/bin/python
import os
## import re
## X="BEGIN DnaSP"
## regexpX=re.compile(X, IGNORECASE)
fileInput = raw_input("Insert path to the input: ")
batch = open(fileInput ,"a")
batch.write("\nbegin paup;\nexec /home/tiago/Programas/MrModeltest2.3/MrModelblock;\nend;")
batch.close()
os.system("LD_PRELOAD=/usr/lib/faketime/libfaketime.so.1 FAKETIME='@2009-05-28' /home/tiago/Programas/paup -n " + fileInput) # Calling paup... with some trick XD
os.system("mrmodeltest2 < /home/tiago/Programas/MrModeltest2.3/mrmodel.scores > /home/tiago/Programas/MrModeltest2.3/output") # Notice that you have to costumize the folder accordingly
os.system("gedit /home/tiago/Programas/MrModeltest2.3/output") # This opens the output file with the models of substitution
