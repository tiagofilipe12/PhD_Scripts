# PhD_Scripts

A bunch of ugly and de-organized scripts that still might be of use to someone... :stuck_out_tongue_closed_eyes:


* [ACC_GO_calcs.py](https://github.com/tiagofilipe12/PhD_Scripts/blob/master/ACC_GO_calcs.py) - This script is used to calculate the logFC of GOs taking as input the list of DAVID conversions ACC to david id
Then atribbute to each david id in david_chart.txt an acc
and lastly, sum the respective acc logFC displayed in named_genes_* resulting in the sum of the genes of a given GO.
* [DAVID_to_REVIGO.py](https://github.com/tiagofilipe12/PhD_Scripts/blob/master/DAVID_to_REVIGO.py) - This script is used to generate a list of GO and p values from DAVID output chart.
* [FPKM_Cluster_analysis.py](https://github.com/tiagofilipe12/PhD_Scripts/blob/master/FPKM_Cluster_analysis.py) - This script is intended to merge data from different RSEM outputs with the extension .FPKM
* [GO_finder.py](https://github.com/tiagofilipe12/PhD_Scripts/blob/master/GO_finder.py) - This script generetes a list of all GO terms associated with given categories, provided in an input file
* [GO_stats_venn_diagramm.py](https://github.com/tiagofilipe12/PhD_Scripts/blob/master/GO_stats_venn_diagramm.py) - This script generates a venn diagramm given as input ontologies
* [Gene_naming.py](https://github.com/tiagofilipe12/PhD_Scripts/blob/master/Gene_naming.py) - This script is used to atribute gene names to the differently expressed genes retrieved from EdgeR and sort it in descending order of logFC. 
* [Heatmap_DAVID.R](https://github.com/tiagofilipe12/PhD_Scripts/blob/master/Heatmap_DAVID.R) - Heatmap with functional analysis (all; up and down)
* [Heatmap_Genes.R](https://github.com/tiagofilipe12/PhD_Scripts/blob/master/Heatmap_Genes.R) - Heatmap for gene lists
* [PCA_DEs.py](https://github.com/tiagofilipe12/PhD_Scripts/blob/master/PCA_DEs.py) - Make a PCA with DE genes from EdgeR.
* [R_script_heatmap.R](https://github.com/tiagofilipe12/PhD_Scripts/blob/master/R_script_heatmap.R) - A script to generate Heatmaps
* [R_script_heatmap_FPKM.R](https://github.com/tiagofilipe12/PhD_Scripts/blob/master/R_script_heatmap_FPKM.R) - A script to generate an heatmap for fpkm values
* [TopBlast_to_DAVID.py](https://github.com/tiagofilipe12/PhD_Scripts/blob/master/TopBlast_to_DAVID.py) - This script is used to generate a list of acc or gi to give as input to DAVID.
* [acc_to_contig.py](https://github.com/tiagofilipe12/PhD_Scripts/blob/master/acc_to_contig.py) - This script is intended to provide an input accession number (acc) and search it in a given list of xml files, retrieving the contig in a output fasta that consist in filtering a given fasta (normally the total transcriptome in fasta)
* [after_clustering.py](https://github.com/tiagofilipe12/PhD_Scripts/blob/master/after_clustering.py) - Script to be run after cluster_analysis.py with the output from that program. This script orders the sum of logFCs from all libs do be compared with cluster_analysis.py,
 giving an ordered list of the most DEs genes.
* [annot_filter.py](https://github.com/tiagofilipe12/PhD_Scripts/blob/master/annot_filter.py) - This script filters .annot files given a list of Accesion numbers and contigIDs
 Input: Named_genes file for correspondences; list of ACCs or contig IDs;.annot file from b2go
* [annotation_statistics.py](https://github.com/tiagofilipe12/PhD_Scripts/blob/master/annotation_statistics.py) - input files are named_genes files, the output of Gene_naming.py.
this script retrieves the number of annotated genes in one transcriptome
* [blast_band-aid.py](https://github.com/tiagofilipe12/PhD_Scripts/blob/master/blast_band-aid.py) - blast_band-aid.py replaces the previous version blast_wrapper_aid.py and adds two main functions: Removal of duplicated contigs either from XML files or fasta files.
 This script is intended not only to generate a fasta file to resume a blast run provided the original fasta and blast results, but it also intends to remove duplicated 
 blast entries from the XML file that may be generated when using blast.py (https://github.com/tiagofilipe12/blast_wrapper), either because you made some mistake and cat
 wrong XMLs or either you were distracted like me and forgot which files to cat. The script also removes duplicated contigs from fasta files either with 'both' or 
'fasta' options.
 Note that this script does not concatenate the several XML files that one blast run may generate due to errors or broken pipes and thus it is your responsability to cat
 the desired XML files into one XML file that can be given to blast_band-aid.py. This is intentional so the user pay attetion to what is being cat before any filter.
 Script works under BLASTX 2.2.29+, for different versions that changed the XML format it may not work properly, so use it with caution.
* [cluster_analysis.py](https://github.com/tiagofilipe12/PhD_Scripts/blob/master/cluster_analysis.py) - Makes a clustering of several outputs from EdgeR
* [clustering_analysis_ACC_vs_UNK.py](https://github.com/tiagofilipe12/PhD_Scripts/blob/master/clustering_analysis_ACC_vs_UNK.py) - Generates a cluster_output with only blasted contigs (take into account that this list is already filtered for duplicated entries contrarily to TopBlast_to_David.py)
* [clustering_analysis_statsnstuff_UP_Vs_DOWN.py](https://github.com/tiagofilipe12/PhD_Scripts/blob/master/clustering_analysis_statsnstuff_UP_Vs_DOWN.py) - Input file must be cluster_output_5 with all 6 comparisons, with annotated, non annotated contigs, and with up and down regulated genes from cluser_analysis.py
 Generates a stats file that can be imported in excel with all simple stats of DE genes in clustering analysis resulting from cluster_anaysis.py.
* [clustering_analysis_venn_stats.py](https://github.com/tiagofilipe12/PhD_Scripts/blob/master/clustering_analysis_venn_stats.py) - script to generate stats to plot in venn_diagramm.svg with circles of the same size. Generates venns for 3 organs and between two organs of the same species
 This script takes as input, the outputs generated by clustering_analysis_stats.py and searches for common ACC in those files.
* [countnfpkm_filtering.py](https://github.com/tiagofilipe12/PhD_Scripts/blob/master/countnfpkm_filtering.py) -  This script filters couns or fpkms and summarizes in terms of up and down genes in a csv
* [edgeR_filter.py](https://github.com/tiagofilipe12/PhD_Scripts/blob/master/edgeR_filter.py) - This script filters any fasta file, with the contigs that proved
 to be differently expressed between pairs of libraries (from EdgeR output).
 The resulting output provides a fasta to use for BLAST purposes, namely
 to use in Blast2GO.
 This is version 2 of this script and it was added a function to filter the
 FDR values from the EdgeR_File. Default FDR value is 0.05.
* [exclusive_and_shared_ACC.py](https://github.com/tiagofilipe12/PhD_Scripts/blob/master/exclusive_and_shared_ACC.py) - this script compares two conditions (two files like fins_torg_to_DAVID_ALL.txt) and retrieves a list of exclusive ACC for each species and shared ACC that is intend to be further
 analyzed using annot_filter.py and b2go to retrieve the functions of these ACC.
* [fdr_calc.py](https://github.com/tiagofilipe12/PhD_Scripts/blob/master/fdr_calc.py) - A script intended to calculate FDR values with the correction of BY or BH, provide a below diagonal with the pvalues. The above diagonal will be ignored.
* [filter_ACC_GO_calcs.py](https://github.com/tiagofilipe12/PhD_Scripts/blob/master/filter_ACC_GO_calcs.py) - 
* [filter_clustering.py](https://github.com/tiagofilipe12/PhD_Scripts/blob/master/filter_clustering.py) - Script designed to construct a rough sum of 6 columns of Fold Change, sort the input using this sum in descending order and generates a heatmap of this information
* [mafft.sh](https://github.com/tiagofilipe12/PhD_Scripts/blob/master/mafft.sh) - a script to run mafft
* [modelgen.py](https://github.com/tiagofilipe12/PhD_Scripts/blob/master/modelgen.py) - a script to run modelgenerator
* [multiple_comparisons.csv](https://github.com/tiagofilipe12/PhD_Scripts/blob/master/multiple_comparisons.csv) - sample output from qpcr_workflow.py
* [phase.py](https://github.com/tiagofilipe12/PhD_Scripts/blob/master/phase.py) - a script to run phase
* [qpcr_workflow.py](https://github.com/tiagofilipe12/PhD_Scripts/blob/master/qpcr_workflow.py) - Input format:
 Condition\tSample name\t mean Cq (Three columns)
 because many of the steps before this analysis are dependent on the user this script does not accept as input the output from biorad software
 Also replicates must be processed before using this script because the user may want to discard some replicates.
 Reference gene normalization factors are also required for the following calculations
 Statistics implemented, however Dunn's test is not available and so an output file (containing the data frame for multiple comparison tests) is generated in case Dunn's test are required
* [top_non_DE.py](https://github.com/tiagofilipe12/PhD_Scripts/blob/master/top_non_DE.py) - a script to identify top non DE genes from EdgeR output.
* [venn2_diagram.py](https://github.com/tiagofilipe12/PhD_Scripts/blob/master/venn2_diagram.py) - makes a venn diagramm of 2 circles.
* [venn2_diagram_species.py](https://github.com/tiagofilipe12/PhD_Scripts/blob/master/venn2_diagram_species.py) - this is really hardcoded.. :confounded:
* [venn_diagram_new.py](https://github.com/tiagofilipe12/PhD_Scripts/blob/master/venn_diagram_new.py) - makes a venn diagramm of 3 circles.



