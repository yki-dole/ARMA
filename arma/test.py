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
    #print("入力するcsvファイルの名称")
    #nameOfCsvfiles = input()
    nameOfCsvfiles = "output"
    nameOfCsvfiles = "csv/"+nameOfCsvfiles
    groupValue = 87;
    ipuSum = 0
    for i in range(groupValue):
        nameOfCsvfile = nameOfCsvfiles +"_"+ str(i)+"_year-count.csv"
        data = pd.read_csv(nameOfCsvfile,names=['Year','Count'])
        sdata = pd.read_csv(nameOfCsvfile,names=['Year','Count'])
        data.index = data["Year"]
        sdata.index = sdata["Year"]
        del data["Year"]
        del sdata["Year"]
        plt.plot(data)
        results=sm.tsa.ARMA(sdata["Count"],(1,0))
        result = results.fit()

        plt.plot(result.fittedvalues)
        saveFile = "output/graph_"+str(i)+".png"
        aa = data["Count"]
        #誤差率計算
        ipu = 100*(result.fittedvalues.values[-1] - data.values[-1])/data.values[-1]

        ipuSum+=ipu
        print(ipu)

        plt.savefig(saveFile)
        plt.close()
    print(ipuSum/groupValue)
