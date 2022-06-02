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



csvFilePath = r'introducaoaNodeJS.csv'
jsonFilePath = r'introducaoaNodeJS.json'
make_json(csvFilePath, jsonFilePath)

csvFilePath = r'comoMelhorarSeuNegocio.csv'
jsonFilePath = r'comoMelhorarSeuNegocio.json'
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

csvFilePath = r'porqueFazerCursoDeComputacao.csv'
jsonFilePath = r'porqueFazerCursoDeComputacao.json'
make_json(csvFilePath, jsonFilePath)