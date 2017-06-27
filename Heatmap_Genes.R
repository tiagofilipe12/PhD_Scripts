#############################################################################
# Heatmap for gene lists
#############################################################################

#Change workspace to directory where are the txt files with DAVID tables
setwd("/home/tiago/Copy/blast2GO_assembly_all")
#read input file in directory 
InFile <- as.matrix(read.table("heatmap_genes_GOinterest_protein_catergories_unknown.csv", sep="\t", header=T))
print(InFile)
InFile <- InFile[order(InFile[,10]),]
#A[order(A[,k]),]

#Build two heatmaps
## common to the two heatmaps
#plotCol <- c("forestgreen", "white", "red","steelblue")  # uncomment this two lines for non-gradient heatmap
#breaks <- c(-30, -0.58, 0.58, 30, 50)                    # uncomment this two lines for non-gradient heatmap
  
plotCol <- colorRampPalette( c("blue", "white", "red"), space="rgb")(75)  #comment this line for non-gradient heatmap

#specific of the literature heatmap
heatTable <- apply(InFile[,3:8], c(1,2), as.numeric)
print(heatTable)
breaks <- c(seq(min(heatTable), -0.58, length=38), seq(0.58, max(heatTable), length=38))  #comment this line for non-gradient heatmap
pdf("heatmap_genes_GOinterest_literature_2_gradient_v5_unknown.pdf")
#par(oma=c(0,0,0,0))
heatmap(heatTable, scale="n", breaks=breaks, col=plotCol, margins=c(5,15), cexRow= 0.6, Colv=NA, cexCol=1, labRow=c(paste(InFile[,2])), labCol=c("Fins", "Liver", "Muscle", "Fins", "Liver", "Muscle"))#, InFile[,10], sep="          ")), labCol=c("carol_fins", "carol_liver", "carol_muscle", "torg_fins", "torg_liver", "torg_muscle", "expected"), main="target DE genes")
#heatmap(heatTable, scale="n", breaks=breaks, col=plotCol, Colv=NA, cexCol=1, labRow=InFile[,1], labCol=c("carol_fins", "carol_liver", "carol_muscle", "torg_fins", "torg_liver", "torg_muscle", "expected"), main="target DE genes")

legend("right", title= "Legend:", cex= 0.7, fill = c("blue", "white", "red"), legend = c("Downregulated", "No DE", "Upregulated"))
dev.off()

##specific for the heatmaps with the new genes from selected GOs
#heatTable <- apply(InFile[,3:8], c(1,2), as.numeric)
#breaks <- c(seq(min(heatTable), -0.58, length=4), seq(0.58, max(heatTable), length=4))  #comment this line for non-gradient heatmap
#pdf("heatmap_genes_GOinterest_new_2_gradient.pdf")
#par(oma=c(0,0,0,12))
##dar nome funçao seguinte para depois puder manipular a figura com linhas tal como fiz para a heatTable
#heatmap(heatTable[28:60,], scale="n", breaks=breaks, col=plotCol, Rowv=NA, Colv=NA, cexCol=1, labRow=c(paste(InFile[28:60,2], InFile[28:60,10], sep="          ")), labCol=c("carol_fins", "carol_liver", "carol_muscle", "torg_fins", "torg_liver", "torg_muscle"), main="selected DE genes") #Rowv=NA retirar para fazr o agrupamento auto do heatmap.
#heatmap(heatTable[28:60,], scale="n", breaks=breaks, col=plotCol, Rowv=NA, Colv=NA, cexCol=1, labRow=InFile[28:60,1], labCol=c("carol_fins", "carol_liver", "carol_muscle", "torg_fins", "torg_liver", "torg_muscle"), main="selected DE genes")

#dev.off()
