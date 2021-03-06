#############################################################################
# Heatmap with functional analysis (all; up and down)
#############################################################################

#Change workspace to directory where are the txt files with DAVID tables
setwd("/home/tiago/Copy/blast2GO_assembly_all/Cluster_analysis/fdr_0_0005/Cluster_output_v6/blasthits/common_GOs/heatmaps")
#read all files in directory 
allFiles <- dir(pattern=".txt")

#build R list to record all results
allTerms <- vector("list", length=length(allFiles))
names(allTerms) <- gsub("DAVID_","", gsub(".txt", "", allFiles))

# For each file: import data, select significant pathways and split results in 3 functional categories
for(i in 1:length(allFiles)){ #Mudei allPathways para allFiles pois a variável allPathways não estava definida anteriormente
  temp <- as.matrix(read.table(allFiles[i], sep="\t", header=T))
  temp <- temp[which(as.numeric(temp[,"Benjamini"]) < 0.05),] #replace for adjusted p-value (Benjamini para já porque temo que o FDR leve a muito poucos resultados) #filters rows.
  temp <- matrix(data=temp, ncol=13)  # adds a first line with column names which helps with dimnames of array.
  colnames(temp) <- c("Category","Term","Count","%","PValue","Genes","List Total","Pop Hits","Pop Total","Fold Enrichment","Bonferroni","Benjamini","FDR") # new line in tests
  curFile <- vector("list", 3); names(curFile) <- c("BP", "MF", "KEGGPathways")
  curFile[[1]] <- sapply(temp[which(temp[,"Category"] == "GOTERM_BP_FAT"),"Term"], function(x) strsplit(x, "~")[[1]][[2]]) 
  curFile[[2]] <- sapply(temp[which(temp[,"Category"] == "GOTERM_MF_FAT"),"Term"], function(x) strsplit(x, "~")[[1]][[2]]) 
  curFile[[3]] <- sapply(temp[which(temp[,"Category"] == "KEGG_PATHWAY"),"Term"], function(x) strsplit(x, ":")[[1]][[2]]) 
  allTerms[[i]] <- curFile
}


 
#Build a matrix with all data and plot
allValues <- rep(c(4, -2,2), 6)
allTitles <- c("Biological Processes", "Molecular Functions", "KEGG Pathways")
pdf("Heatmap_DAVID_v2.pdf")
for(i in 1:3){
  curTerms <- unique(unlist(lapply(allTerms, function(x) x[[i]])))

  heatTable <- matrix(data=0, nrow=length(curTerms), ncol=length(allTerms), dimnames=list(curTerms, names(allTerms)))
  for(a in 1:length(allTerms)){
    heatTable[match(allTerms[[a]][[i]], rownames(heatTable)),a] <- allValues[a]
  }
  
  heatTable <- cbind(heatTable[,1], heatTable[,2]+heatTable[,3],heatTable[,4], heatTable[,5]+heatTable[,6],heatTable[,7], heatTable[,8]+heatTable[,9],heatTable[,10], heatTable[,11]+heatTable[,12],heatTable[,13], heatTable[,14]+heatTable[,15],heatTable[,16], heatTable[,17]+heatTable[,18])    #Acrescentei mais heatTables porque em principio também tenho mais colunas no heatmap
#  heatTeste <- heatTable[-(1:5),]   #heatTeste
#  print(heatTeste)    #heatTeste
  plotCol <- c("forestgreen", "white", "red", "steelblue")
  breaks <- c(-3, -1,1, 3, 5)
  par(oma=c(0,0,0,12))
#  if (i == 1){     ## tem de se usar estes if's para fazer o que fiz em cima com o heatTeste de modo a retirar GO redudantes... de apenas um das variaveis sendo q 1 é o correspondente ao biological process
#  heatBP <- heatmap(heatTable, scale="n", breaks=breaks, col=plotCol, Rowv=NA,Colv=NA, cexCol=1, labCol=c("fins_carol_all","fins_carol_up/down","fins_torg_all","fins_torg_up/down","liver_carol_all","liver_carol_up/down","liver_torg_all","liver_torg_up/down","muscle_carol_all","muscle_carol_up/down","muscle_torg_all","muscle_torg_up/down"), main=allTitles[i])  # Comecei a editar os nomes, mas não continuei daqui para a frente
  #heatmap(heatTable[41:80,], scale="n", breaks=breaks, col=plotCol, Rowv=NA,Colv=NA, cexCol=1, labCol=c("fins_carol_all","fins_carol_up/down","fins_torg_all","fins_torg_up/down","liver_carol_all","liver_carol_up/down","liver_torg_all","liver_torg_up/down","muscle_carol_all","muscle_carol_up/down","muscle_torg_all","muscle_torg_up/down"), main=allTitles[i])  # Comecei a editar os nomes, mas não continuei daqui para a frente
  #heatmap(heatTable[81:120,], scale="n", breaks=breaks, col=plotCol, Rowv=NA,Colv=NA, cexCol=1, labCol=c("fins_carol_all","fins_carol_up/down","fins_torg_all","fins_torg_up/down","liver_carol_all","liver_carol_up/down","liver_torg_all","liver_torg_up/down","muscle_carol_all","muscle_carol_up/down","muscle_torg_all","muscle_torg_up/down"), main=allTitles[i])  # Comecei a editar os nomes, mas não continuei daqui para a frente
  #heatmap(heatTable[121:160,], scale="n", breaks=breaks, col=plotCol, Rowv=NA,Colv=NA, cexCol=1, labCol=c("fins_carol_all","fins_carol_up/down","fins_torg_all","fins_torg_up/down","liver_carol_all","liver_carol_up/down","liver_torg_all","liver_torg_up/down","muscle_carol_all","muscle_carol_up/down","muscle_torg_all","muscle_torg_up/down"), main=allTitles[i])  # Comecei a editar os nomes, mas não continuei daqui para a frente
  #heatmap(heatTable[161:200,], scale="n", breaks=breaks, col=plotCol, Rowv=NA,Colv=NA, cexCol=1, labCol=c("fins_carol_all","fins_carol_up/down","fins_torg_all","fins_torg_up/down","liver_carol_all","liver_carol_up/down","liver_torg_all","liver_torg_up/down","muscle_carol_all","muscle_carol_up/down","muscle_torg_all","muscle_torg_up/down"), main=allTitles[i])  # Comecei a editar os nomes, mas não continuei daqui para a frente
  #heatmap(heatTable[201:240,], scale="n", breaks=breaks, col=plotCol, Rowv=NA,Colv=NA, cexCol=1, labCol=c("fins_carol_all","fins_carol_up/down","fins_torg_all","fins_torg_up/down","liver_carol_all","liver_carol_up/down","liver_torg_all","liver_torg_up/down","muscle_carol_all","muscle_carol_up/down","muscle_torg_all","muscle_torg_up/down"), main=allTitles[i])  # Comecei a editar os nomes, mas não continuei daqui para a frente
  #heatmap(heatTable[201:240,], scale="n", breaks=breaks, col=plotCol, Rowv=NA,Colv=NA, cexCol=1, labCol=c("fins_carol_all","fins_carol_up/down","fins_torg_all","fins_torg_up/down","liver_carol_all","liver_carol_up/down","liver_torg_all","liver_torg_up/down","muscle_carol_all","muscle_carol_up/down","muscle_torg_all","muscle_torg_up/down"), main=allTitles[i])  # Comecei a editar os nomes, mas não continuei daqui para a frente
  #heatmap(heatTable[241:280,], scale="n", breaks=breaks, col=plotCol, Rowv=NA,Colv=NA, cexCol=1, labCol=c("fins_carol_all","fins_carol_up/down","fins_torg_all","fins_torg_up/down","liver_carol_all","liver_carol_up/down","liver_torg_all","liver_torg_up/down","muscle_carol_all","muscle_carol_up/down","muscle_torg_all","muscle_torg_up/down"), main=allTitles[i])  # Comecei a editar os nomes, mas não continuei daqui para a frente
  #heatmap(heatTable[281:length(curTerms),], scale="n", breaks=breaks, col=plotCol, Rowv=NA,Colv=NA, cexCol=1, labCol=c("fins_carol_all","fins_carol_up/down","fins_torg_all","fins_torg_up/down","liver_carol_all","liver_carol_up/down","liver_torg_all","liver_torg_up/down","muscle_carol_all","muscle_carol_up/down","muscle_torg_all","muscle_torg_up/down"), main=allTitles[i])  # Comecei a editar os nomes, mas não continuei daqui para a frente  temp <- heatTable[,c(1,3,5,7,9,11)]; temp <- temp[which(apply(temp, 1, function(x) all(x == 0)) ==F),]
#  }
#  if (i == 2){  
#  heatMF <- heatmap(heatTable, scale="n", breaks=breaks, col=plotCol, Rowv=NA,Colv=NA, cexCol=1, labCol=c("fins_carol_all","fins_carol_up/down","fins_torg_all","fins_torg_up/down","liver_carol_all","liver_carol_up/down","liver_torg_all","liver_torg_up/down","muscle_carol_all","muscle_carol_up/down","muscle_torg_all","muscle_torg_up/down"), main=allTitles[i])  # Comecei a editar os nomes, mas não continuei daqui para a frente
  #heatmap(heatTable[41:80,], scale="n", breaks=breaks, col=plotCol, Rowv=NA,Colv=NA, cexCol=1, labCol=c("fins_carol_all","fins_carol_up/down","fins_torg_all","fins_torg_up/down","liver_carol_all","liver_carol_up/down","liver_torg_all","liver_torg_up/down","muscle_carol_all","muscle_carol_up/down","muscle_torg_all","muscle_torg_up/down"), main=allTitles[i])  # Comecei a editar os nomes, mas não continuei daqui para a frente
  #heatmap(heatTable[81:120,], scale="n", breaks=breaks, col=plotCol, Rowv=NA,Colv=NA, cexCol=1, labCol=c("fins_carol_all","fins_carol_up/down","fins_torg_all","fins_torg_up/down","liver_carol_all","liver_carol_up/down","liver_torg_all","liver_torg_up/down","muscle_carol_all","muscle_carol_up/down","muscle_torg_all","muscle_torg_up/down"), main=allTitles[i])  # Comecei a editar os nomes, mas não continuei daqui para a frente
  #heatmap(heatTable[121:length(curTerms),], scale="n", breaks=breaks, col=plotCol, Rowv=NA,Colv=NA, cexCol=1, labCol=c("fins_carol_all","fins_carol_up/down","fins_torg_all","fins_torg_up/down","liver_carol_all","liver_carol_up/down","liver_torg_all","liver_torg_up/down","muscle_carol_all","muscle_carol_up/down","muscle_torg_all","muscle_torg_up/down"), main=allTitles[i])  # Comecei a editar os nomes, mas não continuei daqui para a frente
#  }
#  if (i == 3){  
#  heatKEGG <- heatmap(heatTable, scale="n", breaks=breaks, col=plotCol, Rowv=NA,Colv=NA, cexCol=1, labCol=c("fins_carol_all","fins_carol_up/down","fins_torg_all","fins_torg_up/down","liver_carol_all","liver_carol_up/down","liver_torg_all","liver_torg_up/down","muscle_carol_all","muscle_carol_up/down","muscle_torg_all","muscle_torg_up/down"), main=allTitles[i])  # Comecei a editar os nomes, mas não continuei daqui para a frente
  #heatmap(heatTable[41:length(curTerms),], scale="n", breaks=breaks, col=plotCol, Rowv=NA,Colv=NA, cexCol=1, labCol=c("fins_carol_all","fins_carol_up/down","fins_torg_all","fins_torg_up/down","liver_carol_all","liver_carol_up/down","liver_torg_all","liver_torg_up/down","muscle_carol_all","muscle_carol_up/down","muscle_torg_all","muscle_torg_up/down"), main=allTitles[i])  # Comecei a editar os nomes, mas não continuei daqui para a frente
#  }
  heatmap(heatTable, scale="n", breaks=breaks, col=plotCol, Rowv=NA,Colv=NA, cexCol=1, labCol=c("fins_carol_all","fins_carol_up/down","fins_torg_all","fins_torg_up/down","liver_carol_all","liver_carol_up/down","liver_torg_all","liver_torg_up/down","muscle_carol_all","muscle_carol_up/down","muscle_torg_all","muscle_torg_up/down"), main=allTitles[i])  # Comecei a editar os nomes, mas não continuei daqui para a frente
  temp <- heatTable[,c(1,3,5,7,9,11)]; temp <- temp[which(apply(temp, 1, function(x) all(x == 0)) ==F),]
  heat_all <- heatmap(temp, scale="n", breaks=breaks, col=plotCol, Rowv=NA,Colv=NA, cexCol=1, labCol=c("fins_carol_all","fins_torg_all","liver_carol_all","liver_torg_all","muscle_carol_all","muscle_torg_all"), main=allTitles[i])
  temp <- heatTable[,c(2,4,6,8,10,12)]; temp <- temp[which(apply(temp, 1, function(x) all(x == 0)) ==F),]
  temp
  heat_up_down <- heatmap(temp, scale="n", breaks=breaks, col=plotCol, Rowv=NA,Colv=NA, cexCol=1, labCol=c("fins_carol_up/down","fins_torg_up/down","liver_carol_up/down","liver_torg_up/down","muscle_carol_up/down","muscle_torg_up/down"), main=allTitles[i])
}
dev.off()

## block to open a resumed heatmaps with customized tags removed.
pdf("Heatmap_DAVID_v2_edited_v2.pdf")

for(i in 1:3){
  curTerms <- unique(unlist(lapply(allTerms, function(x) x[[i]])))

  heatTable <- matrix(data=0, nrow=length(curTerms), ncol=length(allTerms), dimnames=list(curTerms, names(allTerms)))
  for(a in 1:length(allTerms)){
    heatTable[match(allTerms[[a]][[i]], rownames(heatTable)),a] <- allValues[a]
  }
  
  heatTable <- cbind(heatTable[,1], heatTable[,2]+heatTable[,3],heatTable[,7], heatTable[,8]+heatTable[,9],heatTable[,13], heatTable[,14]+heatTable[,15],heatTable[,4], heatTable[,5]+heatTable[,6], heatTable[,10], heatTable[,11]+heatTable[,12],heatTable[,16], heatTable[,17]+heatTable[,18])    #Acrescentei mais heatTables porque em principio também tenho mais colunas no heatmap



  plotCol <- c("forestgreen", "white", "red", "steelblue")
  breaks <- c(-3, -1,1, 3, 5)
  par(oma=c(0,0,0,12))
  if (i == 1){
## removes undesired lines in heatmap
  heatBP <- heatTable[-c(2:3,5,10:11,13,16:19,22,27,30:32,34,36:39,41,43:44,46:53,56,58),]

##lines to remove:  x27 x30 x31 x41 x46 x48 x49 x51 x53 x32 x34 x47 x50 x38 x43 x58 x10 x11 x13 x16 x17 x18 x19 x2 x3 x5 x22 x36 x37 x39 x44 x52 x56

#  print(heatBP)
  heatmapBP <- heatmap(heatBP, scale="n", breaks=breaks, col=plotCol, Rowv=NA,Colv=NA, cexCol=1, labCol=c("fins_carol_all","fins_carol_up/down","liver_carol_all","liver_carol_up/down","muscle_carol_all","muscle_carol_up/down","fins_torg_all","fins_torg_up/down","liver_torg_all","liver_torg_up/down","muscle_torg_all","muscle_torg_up/down"), main=allTitles[i])  # Comecei a editar os nomes, mas não continuei daqui para a frente
  temp <- heatBP[,c(1,3,5,7,9,11)]; temp <- temp[which(apply(temp, 1, function(x) all(x == 0)) ==F),]
  heat_all <- heatmap(temp, scale="n", breaks=breaks, col=plotCol, Rowv=NA,Colv=NA, cexCol=1, labCol=c("fins_carol_all","liver_carol_all","muscle_carol_all","fins_torg_all","liver_torg_all","muscle_torg_all"), main=allTitles[i])
  temp <- heatBP[,c(2,4,6,8,10,12)]; temp <- temp[which(apply(temp, 1, function(x) all(x == 0)) ==F),]
  temp
  heat_up_down <- heatmap(temp, scale="n", breaks=breaks, col=plotCol, Rowv=NA,Colv=NA, cexCol=1, labCol=c("fins_carol_up/down","liver_carol_up/down","muscle_carol_up/down","fins_torg_up/down","liver_torg_up/down","muscle_torg_up/down"), main=allTitles[i])

  }

  if (i == 2){  
  ## removes undesired lines in heatmap
  heatMF <- heatTable[-c(1,3,8,11,13,14,15,17,21,23,35,37,40),]
  heatmapMF <- heatmap(heatMF, scale="n", breaks=breaks, col=plotCol, Rowv=NA,Colv=NA, cexCol=1, labCol=c("fins_carol_all","fins_carol_up/down","liver_carol_all","liver_carol_up/down","muscle_carol_all","muscle_carol_up/down","fins_torg_all","fins_torg_up/down","liver_torg_all","liver_torg_up/down","muscle_torg_all","muscle_torg_up/down"), main=allTitles[i])  # Comecei a editar os nomes, mas não continuei daqui para a frente
  temp <- heatMF[,c(1,3,5,7,9,11)]; temp <- temp[which(apply(temp, 1, function(x) all(x == 0)) ==F),]
  heat_all <- heatmap(temp, scale="n", breaks=breaks, col=plotCol, Rowv=NA,Colv=NA, cexCol=1, labCol=c("fins_carol_all","liver_carol_all","muscle_carol_all","fins_torg_all","liver_torg_all","muscle_torg_all"), main=allTitles[i])
  temp <- heatMF[,c(2,4,6,8,10,12)]; temp <- temp[which(apply(temp, 1, function(x) all(x == 0)) ==F),]
  temp
  heat_up_down <- heatmap(temp, scale="n", breaks=breaks, col=plotCol, Rowv=NA,Colv=NA, cexCol=1, labCol=c("fins_carol_up/down","liver_carol_up/down","muscle_carol_up/down","fins_torg_up/down","liver_torg_up/down","muscle_torg_up/down"), main=allTitles[i])

  }
  if (i == 3){ 
  heatKEGG <- heatTable[-c(3,7,11,13,14,19,4,22,24,26,20),]
  heatmapKEGG <- heatmap(heatKEGG, scale="n", breaks=breaks, col=plotCol, Rowv=NA,Colv=NA, cexCol=1, labCol=c("fins_carol_all","fins_carol_up/down","liver_carol_all","liver_carol_up/down","muscle_carol_all","muscle_carol_up/down","fins_torg_all","fins_torg_up/down","liver_torg_all","liver_torg_up/down","muscle_torg_all","muscle_torg_up/down"), main=allTitles[i])  # Comecei a editar os nomes, mas não continuei daqui para a frente
  temp <- heatKEGG[,c(1,3,5,7,9,11)]; temp <- temp[which(apply(temp, 1, function(x) all(x == 0)) ==F),]
  heat_all <- heatmap(temp, scale="n", breaks=breaks, col=plotCol, Rowv=NA,Colv=NA, cexCol=1, labCol=c("fins_carol_all","liver_carol_all","muscle_carol_all","fins_torg_all","liver_torg_all","muscle_torg_all"), main=allTitles[i])
  temp <- heatKEGG[,c(2,4,6,8,10,12)]; temp <- temp[which(apply(temp, 1, function(x) all(x == 0)) ==F),]
  heat_up_down <- heatmap(temp, scale="n", breaks=breaks, col=plotCol, Rowv=NA,Colv=NA, cexCol=1, labCol=c("fins_carol_up/down","liver_carol_up/down","muscle_carol_up/down","fins_torg_up/down","liver_torg_up/down","muscle_torg_up/down"), main=allTitles[i])
 
  }
}
dev.off()






## block to generate a list of all functions on each heatmap in order to search for them in AmiGO or KEGG database (http://www.genome.jp/kegg/pathway.html#metabolism)
curTerms_1 <- unique(unlist(lapply(allTerms, function(x) x[[1]])))
curTerms_2 <- unique(unlist(lapply(allTerms, function(x) x[[2]])))
curTerms_3 <- unique(unlist(lapply(allTerms, function(x) x[[3]])))


write.csv(curTerms_1, 'BPs_redundant.csv', row.names=F)
write.csv(curTerms_2,'MFs_redundant.csv', row.names=F)
write.csv(curTerms_3, 'KEGG_redundant.csv', row.names=F)
