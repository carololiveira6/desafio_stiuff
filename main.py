import csv
from sys import exit

with open('notas.csv', 'r', encoding='utf-8') as arquivo_csv:
    csv_reader = csv.DictReader(arquivo_csv, delimiter = ',')
    for linha in csv_reader:
        print(linha)

class Estudante:
    def __init__(self, matricula, disciplina, curso, nota, ch, ano_semestre):
        self._matricula = matricula
        self._dicionario = {'disciplina' : [disciplina], 'curso' : [curso], 'nota' : [nota],
                            'ch' : [ch], 'ano_semestre' : [ano_semestre]}
        return

class Container:
    pass
