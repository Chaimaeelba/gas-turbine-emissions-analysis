# Raw data files

Download the **Gas Turbine CO and NOx Emission Data Set** from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/551/gas+turbine+co+and+nox+emission+data+set).

Extract the five original annual CSV files into this folder:

- `gt_2011.csv`
- `gt_2012.csv`
- `gt_2013.csv`
- `gt_2014.csv`
- `gt_2015.csv`

Alternatively, from the repository root, run `python scripts/download_dataset.py` to fetch and split the UCI data automatically.

The five CSV files are intentionally excluded from Git. The notebook merges them and adds a `year` column.
