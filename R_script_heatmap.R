
#Read File
setwd("/home/tiago/Copy/blast2GO_assembly_all/Cluster_analysis")
dataM <- as.matrix(read.table("Cluster_output_Carolsums_withIDs", sep="\t", header=TRUE, row.names=NULL))

head(dataM)

#Replace "None" values by zero
dataM[which(dataM == "None")] <- 0

#Buil heatmap with genes showing higher fold-changes (top 5000)
heatTable <- apply(dataM[,3:5], c(1,2), as.numeric)
maxFoldChanges <- apply(heatTable, 1, function(x) max(abs(x)))
indexHigherFoldChanges <- order(maxFoldChanges, decreasing=T)[1:1000]
heatTable <- heatTable[indexHigherFoldChanges,]
pdf("Heatmap.pdf")
plotCol <- colorRampPalette( c("green", "black", "red"), space="rgb")(7)
breaks <- c(seq(min(heatTable), -0.58, length=4), seq(0.58, max(heatTable), length=4))
#heatTable_ordered <- heatTable[order(heatTable[,1], heatTable[,2], heatTable[,3], decreasing=T),]
heatmap(heatTable, scale="n", breaks=breaks, col=plotCol, cexCol=1, labRow="")
dev.off()
