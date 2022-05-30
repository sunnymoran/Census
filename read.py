import csv
from hashlib import new
import pandas as pd
import xml.dom.minidom as minidom
import wikipedia
from locations import State , Location, City, County


data = pd.read_csv("resources/censusdata19102020.csv")
data2 = pd.read_csv("resources/censusdata2021.csv")
#data 3 = practice reading from pdf file
#Reading Excel Data
data4 = pd.read_excel("resources/Idaho/Idaho2020-2021.xlsx", header = 3, na_values=['NA'], usecols=None)
#Wikipedia searching
result = wikipedia.search("Category:Cities in Idaho by county")

page = wikipedia.page(result[2])
categories = page.categories
print(result)
content = page.content



idahoCounties = [County(x[0].split(",")[0].split(".")[1],2020,x[2]) for x in data4.values if x[0].find("County") != -1 ]
# print(idahoCounties)




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