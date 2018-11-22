# -*- coding:utf-8 -*-
import csv
import ctypes
from scipy import stats
if __name__ == '__main__':
    numberList= []
    groupList = []
    yearList = []
    value =[]
    print("入力するdotファイルの名前:")
    nameDot = raw_input()
    print("入力するcsvファイルの名前:")
    nameCsv = raw_input()
    print("出力ファイルの名称:")
    name = raw_input()
    outputFileName1 = "csv/"+name + "_number-group-year.csv"
    #outputFileName2 = name + "_year-group.csv"
    nameCsv = "csv/"+nameCsv
    nameDot = "csv/"+nameDot
    groupFile = open(nameCsv,"r")
    numberFile = open(nameDot,"r")
    outputFile =open(outputFileName1,"w")
    for i in numberFile:
        number,_ = i.split("\n")
        numberList.append(number.replace(";",""))
    numberFile.close()
    group =csv.reader(groupFile)
    for row in group:
        groupList.append(row)
    groupFile.close()
    for i in xrange(len(groupList[0])):
        outputFile.write(numberList[i+1][5:11])
        outputFile.write(",")
        outputFile.write(groupList[0][i])
        outputFile.write(",")
        outputFile.write(numberList[i+1][1:5])
        outputFile.write("\n")
        row[i] = int(row[i])
    outputFile.close()
    outputFiles=[]
    value = [0]*(max(row)+1)
    for i in range(max(row)):
        names = "csv/"+name+"_"+str(i)+"_year-count.csv"
        outputFiles.append(open(names,"w"))
    for i in xrange(len(groupList[0])):
        check = numberList[i+1][1:5] in  yearList
        if check == False:
            for n in xrange(max(row)) :
                if value[n]>0:
                    outputFiles[n].write(year)
                    outputFiles[n].write(",")
                    outputFiles[n].write(str(value[n]))
                    outputFiles[n].write("\n")
                    value[n] = 0
            yearList.append(numberList[i+1][1:5])
            year = yearList[-1]
            value[int(groupList[0][i])]+=1
        else:
            value[int(groupList[0][i])]+=1
