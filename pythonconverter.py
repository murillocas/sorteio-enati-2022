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



csvFilePath = r'introduçãoaNodeJS.csv'
jsonFilePath = r'introduçãoaNodeJS.json'
make_json(csvFilePath, jsonFilePath)

csvFilePath = r'comoMelhorarSeuNegócio.csv'
jsonFilePath = r'comoMelhorarSeuNegócio.json'
make_json(csvFilePath, jsonFilePath)

csvFilePath = r'fotografiaAudioVisual.csv'
jsonFilePath = r'fotografiaAudioVisual.json'
make_json(csvFilePath, jsonFilePath)

csvFilePath = r'hospedagemDeSite.csv'
jsonFilePath = r'hospedagemDeSite.json'
make_json(csvFilePath, jsonFilePath)

csvFilePath = r'recomendaçãoDeMusica.csv'
jsonFilePath = r'recomendaçãoDeMusica.json'
make_json(csvFilePath, jsonFilePath)

csvFilePath = r'games.csv'
jsonFilePath = r'games.json'
make_json(csvFilePath, jsonFilePath)

csvFilePath = r'porqueFazerCursoDeComputação.csv'
jsonFilePath = r'porqueFazerCursoDeComputação.json'
make_json(csvFilePath, jsonFilePath)