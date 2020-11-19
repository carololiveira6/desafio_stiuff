import csv


class Estudante:
    def __init__(self, matricula, disciplina, curso, nota, ch, ano_semestre):
        self._matricula = matricula
        self._dicionario = {'disciplina': [disciplina], 'curso': [curso], 'nota': [nota],
                            'ch': [ch], 'ano_semestre': [ano_semestre]}
        return


class Container:
    pass


with open('notas.csv', 'r', encoding='utf-8') as arquivo_csv:
    csv_reader = csv.DictReader(arquivo_csv, delimiter=',')
    next(csv_reader)
    for linha in arquivo_csv:
        print(linha)
