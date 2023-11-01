"""Create a JSON file wilt nobel prize winners who's first name start with the letter A"""
import csv
import json
from pprint import pprint

laureates_beginning_with_a = []

def readCsv(filename):
    with open("laureates.csv", "r") as csvReader:
        return list(csv.DictReader(csvReader))


def filterData(list):
    filter = []
    for item in list:
        name = item['name'].lower()
        if name[0] == "a":
            filter.append(item)
    return filter




def saveJson(dict):
    with open("laureates.json", "w") as jsonWriter:
        json.dump(dict,jsonWriter,indent=2)

laureates = readCsv("laureates.csv")
filteredLaureates = filterData(laureates)
saveJson(filteredLaureates)
