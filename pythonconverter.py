import csv
import json

def make_json(csvFilePath, jsonFilePath):
    data = {}

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        aux=0
        for rows in csvReader:
            data[aux] = rows
            aux += 1

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))



csvFilePath = r'introducaoAoLatex.csv'
jsonFilePath = r'introducaoAoLatex.json'


make_json(csvFilePath, jsonFilePath)