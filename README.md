# Input-to-creat-Heatmap
Script creates an excel file comparing expression levels of  same gene in all libraries. You can use this script like input to PAGE agriGO and a lot of different heatmap softwares.

Parametric Analysis of Gene Set Enrichment-PAGE (http://bioinfo.cau.edu.cn/agriGO/analysis.php)

Gene-E heatmap (https://software.broadinstitute.org/GENE-E/)

Heatmapper heatmap (http://www.heatmapper.ca/)

Clustvis heatmap and PCA (https://biit.cs.ut.ee/clustvis/)

# Prerequisites

Python installed in your machine
Excell file with each libraries log2FDC/or average GO log2FDC in each sheet 

# Installing

No installation is required, the script is ready to use (executable).

python join.py excel.xlsx

# Usage

To ran the join.py script, it will prompt for excel.xlsx file, containing 2 columns per sheet, just the first column need to be named GeneName. You can use how much sheet you want.

# Authors

Mayla Daiane Correa molinari - Initial work - maylamolinari
Fernanda Luz P Costa - Initial work - fernandalpcosta

# License

Open-source



