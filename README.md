# Excel Sheets' Joiner
This script was made to join multiple excel sheets (in a unique excel file). Eeach sheet corresponds to a log2FC result for a list of genes. This script generates a excel sheet output containing all the samples in the same sheet, with the gene name as the first column and the value of the samples log2FC corresponding to those gene list at the next columns. The output of this simple script can be used as an input to other *sofwares* like [agriGO](http://bioinfo.cau.edu.cn/agriGO/analysis.php) and heatmap creator softwares such as:

* [Gene-E](https://software.broadinstitute.org/GENE-E/)

* [Heatmapper](http://www.heatmapper.ca/)

* [Clustvis](https://biit.cs.ut.ee/clustvis/)

## Getting Started

Clone this repository into your local machine

```
git clone https://github.com/maylamolinari/Input-to-creat-Heatmap.git
```

## Prerequisites

* Python version 3 or above installed in your machine
* Excel file with each libraries log2FC/or average GO log2FC in each sheet (file name needs to be excel.xlsx - we are working on the script to accept any file name)

## Installing

No installation is required, the script is ready to use (executable).

```
python join.py excel.xlsx
```

## Usage

After you run the join.py script, it will prompt for excel.xlsx file, containing at least 2 columns per sheet, the first column needs to be named GeneName and it contains a list of the gene names. The second column contains the values, and we recomend that you name it after your library/sample name (example: Library1). Your sheets may have other columns with different informations and contents, the script will just ignore them. Make sure that every sheet in your excel file correspond to a different sample/library.

## Authors

**[Mayla Daiane Correa molinari](https://github.com/maylamolinari)** - *Initial work*

**[Fernanda Luz P Costa](https://github.com/fernandalpcosta)** - *Script developer*

## License

Open-source
