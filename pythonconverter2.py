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



csvFilePath = r'introducaoDocker.csv'
jsonFilePath = r'introducaoDocker.json'
make_json(csvFilePath, jsonFilePath)

csvFilePath = r'cleanCodeLinkedin.csv'
jsonFilePath = r'cleanCodeLinkedin.json'
make_json(csvFilePath, jsonFilePath)

csvFilePath = r'maratonaProgramacao.csv'
jsonFilePath = r'maratonaProgramacao.json'
make_json(csvFilePath, jsonFilePath)

csvFilePath = r'programacaofuncional.csv'
jsonFilePath = r'programacaofuncional.json'
make_json(csvFilePath, jsonFilePath)

csvFilePath = r'brincandoComLEDs.csv'
jsonFilePath = r'brincandoComLEDs.json'
make_json(csvFilePath, jsonFilePath)

csvFilePath = r'BatepapocomEgressos.csv'
jsonFilePath = r'BatepapocomEgressos.json'
make_json(csvFilePath, jsonFilePath)

csvFilePath = r'cerimoniadeEncerramento.csv'
jsonFilePath = r'cerimoniadeEncerramento.json'
make_json(csvFilePath, jsonFilePath)