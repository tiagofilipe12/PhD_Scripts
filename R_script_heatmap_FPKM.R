
#Read File
#setwd("~/Copy/FPKM_analysis")
#dataM <- as.matrix(read.table("Cluster_output_FPKM_carol", sep="\t", header=TRUE, row.names=NULL))

#head(dataM)

#Replace "None" values by zero
#dataM[which(dataM == "None")] <- 0

#Calculate variance and select 2000 top variable genes
# This part should be applied to a matrix containing expression values and not fold-changes
#v <- apply(dataM[,c(2:7)], 1, function(x) var(as.numeric(x)))
#indexTopVarGenes <- order(v, decreasing=T)[1:2000] 
#dataM_topVarGenes <- dataM[indexTopVarGenes,]
#heatTable <- apply(dataM_topVarGenes[,2:7], c(1,2), as.numeric)
#pdf("Heatmap.pdf")
#plotCol <- colorRampPalette( c("blue", "black", "red"), space="rgb")(7)
#breaks <- c(seq(min(heatTable), 0, length=4), seq(1, max(heatTable), length=4))
#heatTable_ordered <- heatTable[order(heatTable[,1], heatTable[,2], heatTable[,3], decreasing=T),]
#heatmap(heatTable, scale="n", breaks=breaks, col=plotCol, cexCol=1, labRow="")
#dev.off()



setwd("~/Copy/FPKM_analysis")
fpkm <- as.matrix(read.table("Cluster_output_FPKM_carol", sep="\t", header=TRUE, row.names=NULL))
temp <- apply(fpkm[,2:7], c(1,2), as.numeric)
tempLog <- apply(temp, c(1,2), function(x) log2(x+0.001))
varLog <- apply(tempLog, 1, var)
mostVar <- order(varLog, decreasing=T)[1:4000]
pdf("Heatmap_carol_log2.pdf")
heatTable <- tempLog[mostVar,]
plotCol <- colorRampPalette( c("blue", "black", "red"), space="rgb")(7)
breaks <- c(seq(min(heatTable), 0, length=4), seq(1, max(heatTable), length=4))
#heatTable_ordered <- heatTable[order(heatTable[,1], heatTable[,2], heatTable[,3], decreasing=T),]
heatmap(heatTable, breaks=breaks, col=plotCol, cexCol=1, labRow="")
dev.off()
