import csv
from hashlib import new
import pandas as pd
import xml.dom.minidom as minidom
from locations import State , Location, City, County
#Practice object oriented practices
data = pd.read_csv("resources/censusdata19102020.csv")
data2 = pd.read_csv("resources/censusdata2021.csv")
#data 3 = practice reading from pdf file
data4 = pd.read_excel("resources/Idaho/Idaho2020-2021.xlsx", sheet_name=None)
print(data4.values[4])
# county_names = [x for x in data4.column('Idaho')]
# print(county_names)
'''
Column Names:
    Name
    Geography Type
    Year
    Resident Population
    Percent Change in Resident Population
    Resident Population Density
    Resident Population Density Rank
    Number of Representatives
    Change in Number of Representatives
    Average Apportionment Population Per Representative
'''
column_names = [x for x in data.values]
idahoResults = (data[data['Name']=="Idaho"])
# print(idahoResults)
newlist =  [State(x[0],x[2],x[3]) for x in idahoResults.values]
# print(len(newlist))
# print(newlist[11])
# stateIdaho = State(idahoResults[0][0],idahoResults.values[0][2],idahoResults.values[0][9])
# f = open("resources/data.txt", "w")
# f.write(f"{column_names}")
# f.close()
# f = open("resources/data.txt", "r")
# print(f.read())