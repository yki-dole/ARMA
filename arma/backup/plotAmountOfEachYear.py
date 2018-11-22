# coding:utf-8
#実行時はpython3
import scipy
import csv
import copy
import sys
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import statsmodels.api
from statsmodels.tsa.stattools import acf
from statsmodels.tsa.stattools import pacf
from statsmodels.tsa.seasonal import seasonal_decompose

if __name__ == '__main__':

    plt.figure()
    data = pd.read_csv("csv/output_0_year-count.csv",skiprows=2,names=['Year','Count'])
    data.index = data["Year"]
    del data["Year"]
    data.plot()
    plt.savefig('pandas_iris_line.png')
    print(data)
