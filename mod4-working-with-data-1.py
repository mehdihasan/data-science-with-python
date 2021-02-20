###
# Learning Objectives
# 1. Reading files with open
# 2. Writing files with open
# 3. Loading data with Pandas
# 4. Working with and Saving data with Pandas
# simple moving average (SMA): 
###

import matplotlib.pyplot as plt


statData ="resources/ex4.csv"

def getNAvg(file,N):
    
    """
    file - File containting all the raw weather station data
    N - The number of days to compute the moving average over

 

    Return a list of containg the moving average of all data points
    
    """
    with open(file, 'r') as rows:
        lastN = []
        meanList = [0]
        rowListWithHeader = rows.readlines()
        rowList = rowListWithHeader[1:]
        for i, row in enumerate(rowList):
            data = float(row.split(',')[1].strip())
            if (i+1) <= N:
                lastN.append(data)
                meanList[0] = (data + meanList[0] * i) / (i + 1)
            else:
                meanList.append( meanList[i - N] + (data - lastN[0]) / N )
                lastN = lastN[1:]
                lastN.append(data)
        return meanList

                    
def plotData(mean,N):
    """ Plots running averages """    
    mean = [round(x,3) for x in mean]
    plt.plot(mean,label=str(N) + ' day average')
    plt.xlabel('Day')
    plt.ylabel('Precipiation')
    plt.legend()


plotData(getNAvg(statData,1),1)
plotData ([0 for x in range(1,5)]+ getNAvg(statData,5),5 )
plotData([0 for x in range(1,7)] + getNAvg(statData,7),7)