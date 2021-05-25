# -*- coding: utf-8 -*-
"""
Richard Paredes
PSID: 1492535
COSC 1306
Homework #3
"""

def getFileName():
    fileName = input("Please enter the data file name: ")
    print()
    return fileName

def parseCSV(fileName):
    
    with open(fileName) as file:
        allData = [] # contains annual data
        for line in file:
            allData.append(line.strip().split(','))
        
        allData.pop(0) # eliminate column headers
        parseData(allData)

    
def parseData(allData):

    # format per line:
    _date = 0
    _open = 1
    _high = 2
    _low = 3 
    _close = 4
    _adjClose = 5
    _volume = 6

    print("Reading data. . .")

    days = len(allData)
    highestDay = getHighestDay(allData)
    lowestDay = allData[0]
    maxProfit = float(highestDay[_high]) - float(lowestDay[_low])
    
    # find a days with max profit
    for currentDay in range(days-1):
        remainingData = allData[currentDay+1:]
        
        currentLowDay = allData[currentDay]
        currentLowValue = float(currentLowDay[_low])

        annualHighDay = getHighestDay(remainingData)
        annualHighValue = float(annualHighDay[_high])
        
        currentProfit = annualHighValue - currentLowValue
        
        if (currentProfit > maxProfit):
            lowestDay = allData[currentDay]
            highestDay = annualHighDay
            maxProfit = currentProfit
    
    refineData(lowestDay, highestDay)

def getHighestDay(remainingData):
    _high = 2
    annualHighDay = remainingData[0]
    for day in range(len(remainingData)):
        annualHighValue = float(annualHighDay[_high])
        currentHighValue = float(remainingData[day][_high])
        if (currentHighValue > annualHighValue):
            annualHighDay = remainingData[day]
    return annualHighDay

def refineData(lowestDay, highestDay):
    _date = 0
    _high = 2
    _low = 3 

    low = float(lowestDay[_low])
    low = round(low, 2)
    lowDate = lowestDay[_date]

    high = float(highestDay[_high])
    high = round(high, 2)
    highDate = highestDay[_date]
    
    maxProfit = round(high - low, 2)
    ratio = round(high/low, 3)
    printData(lowDate, low, highDate, high, maxProfit, ratio)

def printData(lowDate, low, highDate, high, maxProfit, ratio):
    print('****************************************')
    print('The maximum profit is', maxProfit, 'per share')
    print()
    print('Buy on', lowDate, 'at a price of', low)
    print('Sell on', highDate, 'at a price of', high)
    print()
    print('Change in value ratio:', ratio)
    print('****************************************')
    print()

def main():
    fileName = getFileName()
    while (fileName != ''):
        # one year's worth of data.
        parseCSV(fileName)
        fileName = getFileName()
    print("Thank you and Good Bye!")
main()