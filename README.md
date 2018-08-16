# Pandas Data Exploration Utility Package
***
## Overview
Pandas Data Exploration utility is an interactive, notebook based library for quickly profiling and exploring the shape of data and the relationships between data.
***
## Installation
```
pip install Pandas-Data-Exploration-Utility-Package
```
***
## Usage
```
import pandas as pd
import pandas_exploration_util.viz.explore as pe

global_temp = pd.read_csv("./data/GlobalTemperatures.csv", parse_dates = [0], infer_datetime_format=True)

pe.generate_widget(global_temp)
```
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