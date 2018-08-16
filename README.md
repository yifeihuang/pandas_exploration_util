# Pandas Data Exploration Utility Package

## Table of content
  * [Overview](#overview)
  * [Installation](#installation)
  * [Usage](#usage)
    + [Pareto plot](#pareto-plot)
    + [Distribution plot](#distribution-plot)
    + [X-Y plot](#x-y-plot)

## Overview
Pandas Data Exploration utility is an interactive, notebook based library for quickly profiling and exploring the shape of data and the relationships between data. Using existing APIs from IpyWidget, Plot.ly, and Pandas, it creates a flexible point and click widget that allows the user to easily explore and visualize the dataset.

## Installation
```
pip install Pandas-Data-Exploration-Utility-Package
```

## Usage
```
import pandas as pd
import pandas_exploration_util.viz.explore as pe

global_temp = pd.read_csv("./data/GlobalTemperatures.csv", parse_dates = [0], infer_datetime_format=True)

pe.generate_widget(global_temp)
```
see `/test` for sample data and test jupyter notebook
https://github.com/yifeihuang/pandas_exploration_util/tree/master/test

***
### Pareto plot
Visualize the top values of any column as ranked by aggregation of any other column. Support aggregation functions include `'count', 'sum', 'mean', 'std', 'max', 'min', 'uniques'`
<p align="center">
    <img src="https://raw.githubusercontent.com/yifeihuang/pandas_exploration_util/master/img/pareto.png">
</a></p>

### Distribution plot
Visualize distribution of any numerical value. Binning is automatically determined by the plot.ly histogram method.
<p align="center">
    <img src="https://raw.githubusercontent.com/yifeihuang/pandas_exploration_util/master/img/distribution.png">
</a></p>

### X-Y plot
Visualize the X-Y scatter of any column vs aggregation of any other column. Support aggregation functions include `'count', 'sum', 'mean', 'std', 'max', 'min', 'uniques'`
<p align="center">
    <img src="https://raw.githubusercontent.com/yifeihuang/pandas_exploration_util/master/img/x-y.png">
</a></p>


## Recommended development setup

### Local Dev
1. Setup virtualenv
2. Create a virtual environment using `virtualenv /path/to/env/dir`
3. Activate virtual environment using `source /path/to/env/dir/bin/activate`
4. Clone the repo locally
5. Navigate the root directory of the repo where the `setup.py` lives
6. Install the module in development mode using `python setup.py develop`
7. Run the Jupyter notebook that is in the virtual environment directory, which should have installed as the part of the dependency of the module
8. Dev away
9. When done uninstall the package using `python setup.py develop --uninstall`
10. Deactive the environment using `deactivate`

### Building and distributing
https://packaging.python.org/tutorials/packaging-projects/
Assuming all relevant tools are installed and the relevant project files are properly defined
1. build the distribution using `python3 setup.py sdist bdist_wheel`
2. upload the distribution using `twine upload dist/*`