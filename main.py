import pandas as pd
import csv
import os
from datetime import datetime
from entrada_dados import obter_data, obter_quantia, obter_categoria, obter_descricao

class CSV:
    ARQUIVO_CSV ="dados_financeiros.csv"
    COLUNAS = ["data", "quantia", "categoria", "descricao"]

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.ARQUIVO_CSV)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUNAS)
            df.to_csv(cls.ARQUIVO_CSV, index=False)

    @classmethod
    def add_entrada(cls, data, quantia, categoria, descricao):
            nova_entrada = {
                "data": data,
                "quantia": quantia,
                "categoria": categoria,
                "descricao": descricao
            }
            with open(cls.ARQUIVO_CSV, "a", newline="") as csvfile:
                 escritos = csv.DictWriter(csvfile, fieldnames= cls.COLUNAS )
                 escritos.writerow(nova_entrada)
            print("Entrada adicionada com sucesso!")

def add():
     CSV.initialize_csv()
     data = obter_data("Informe a data da transação (dd-mm-aaaa)ou informe a data de hoje: ", permitir_padrao = True)
     quantia = obter_quantia()
     categoria = obter_categoria()
     descricao = obter_descricao()
     CSV.add_entrada(data, quantia, categoria, descricao)

CSV.initialize_csv()

add()