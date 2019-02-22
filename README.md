# Excel Sheets Joiner
This script was made to join multiple excel sheets (from a unique excel file) that each sheet corresponds to a log2FC result for a list of genes. It generates a excel sheet output containing all the samples in the same sheet, with the gene name as the first column and the value of the samples' log2FC corresponding to those gene list at the next columns.
The output of this simple script can be used as an input to other *sofwares* like [agriGO](http://bioinfo.cau.edu.cn/agriGO/analysis.php) and heatmap creator softwares such as:

* [Gene-E](https://software.broadinstitute.org/GENE-E/)

* [Heatmapper](http://www.heatmapper.ca/)

* [Clustvis](https://biit.cs.ut.ee/clustvis/)

## Getting Started

Clone this repository into your local machine

```
git clone https://github.com/maylamolinari/Input-to-creat-Heatmap.git
```

## Prerequisites

* Python installed in your machine
* Excel file with each libraries log2FDC/or average GO log2FDC in each sheet (file name need to be excel.xlsx)

## Installing

No installation is required, the script is ready to use (executable).

```
python join.py excel.xlsx
```

## Usage

After you run the join.py script, it will prompt for excel.xlsx file, containing 2 columns per sheet, just the first column need to be named GeneName. You can use how many sheet you want.

## Authors

**[Mayla Daiane Correa molinari](https://github.com/maylamolinari)** - *Initial work*

**[Fernanda Luz P Costa](https://github.com/fernandalpcosta)** - *Script developer*

## License

Open-source
