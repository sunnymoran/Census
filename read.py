import csv
import pandas as pd
from locations import State
#Practice object oriented practices
data = pd.read_csv("censusdata19102020.csv")
data2 = pd.read_csv("censusdata2021.csv")
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
column_names = list(data.columns.values)
idahoResults = (data[data['Name']=="Idaho"])

print(type(idahoResults.values[0]))
stateIdaho = State(idahoResults.values[0][0],idahoResults.values[0][2],idahoResults.values[0][9])
print(stateIdaho)
# f = open("data.txt", "w")
# f.write(f"{results}")
# f.close()

# f = open("data.txt", "r")
# print(f.read())