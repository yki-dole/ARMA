# coding:utf-8
#実行時はpython3
import csv
import ctypes
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa import arma_mle
import statsmodels.api as sm

if __name__ == '__main__':

    plt.figure()
    print("入力するcsvファイルの名称")
    nameOfCsvfiles = input()
    nameOfCsvfiles = "csv/"+nameOfCsvfiles
    groupValue = 87;
    for i in range(groupValue):
        nameOfCsvfile = nameOfCsvfiles +"_"+ "0"+"_year-count.csv"
        data = pd.read_csv(nameOfCsvfile,names=['Year','Count'])
        data.index = data["Year"]
        del data["Year"]
        results=sm.tsa.ARMA(data["Count"],(1,3))
        result = results.fit(trend='nc',disp=-1)

        fig1, ax = plt.subplots()
        ax = data.loc['1964':].plot(ax=ax)
        endPlace = len(data)-1
        print(results)
        result.plot_predict(start = endPlace-1,end =endPlace,ax=ax,dynamic=True,plot_insample = False)
        saveFile = "output/graph_"+str(i)+".png"

        plt.savefig(saveFile)
        plt.close()
        
