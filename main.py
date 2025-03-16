import pandas as pd
import csv
import os
from datetime import datetime
from entrada_dados import obter_data, obter_quantia, obter_categoria, obter_descricao
import matplotlib.pyplot as plt

class CSV:
    ARQUIVO_CSV ="dados_financeiros.csv"
    COLUNAS = ["data","quantia","categoria","descricao"]
    FORMATO = "%d-%m-%Y"

# inicilizando o arquivo csv
    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.ARQUIVO_CSV, encoding="latin1")
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUNAS)
            df.to_csv(cls.ARQUIVO_CSV, index=False)

# Adiciona os dados da leitura/ as entradas
    @classmethod
    def add_entrada(cls, data, quantia, categoria, descricao):
            nova_entrada = {
                "data": data,
                "quantia": quantia,
                "categoria": categoria,
                "descricao": descricao
            }
            with open(cls.ARQUIVO_CSV, "a", newline="", encoding="latin1") as csvfile:
                 escritos = csv.DictWriter(csvfile, fieldnames= cls.COLUNAS )
                 escritos.writerow(nova_entrada)
            print("Entrada adicionada com sucesso!")

# Obtém todas as transações dentro de um intervalo de datas
    @classmethod
    def obter_transacoes(cls, inicio_data, final_data):
            df = pd.read_csv(cls.ARQUIVO_CSV)
            df["data"] = pd.to_datetime(df["data"], format=CSV.FORMATO)
            inicio_data = datetime.strptime(inicio_data, CSV.FORMATO)
            final_data = datetime.strptime(final_data, CSV.FORMATO)

            mask = (df["data"] >= inicio_data) & (df["data"] <= final_data)
            df_filtrado = df.loc[mask]

            if df_filtrado.empty:
                print("Nenhum transação foi econtrada no intervalo de datas fornecido.")
            else:
                print(f"Transações de {inicio_data.strftime(CSV.FORMATO)} até {final_data.strftime(CSV.FORMATO)}")  
                print(df_filtrado.to_string(index=False, formatters={"data": lambda x: x.strftime(CSV.FORMATO)}))  

                total_entrada = df_filtrado[df_filtrado["categoria"] == "Entrada"] ["quantia"].sum()
                total_gasto = df_filtrado[df_filtrado["categoria"] == "Despesas"] ["quantia"].sum()
                print("\nResumo: ")
                print(f"Total de entrada: ${total_entrada:.2f}")
                print(f"Total gasto: ${total_gasto:.2f}")
                print(f"Economia líquida: ${(total_entrada - total_gasto):.2f}")
            return df_filtrado

def add():
     CSV.initialize_csv()
     data = obter_data("Informe a data da transação (dd-mm-aaaa)ou informe a data de hoje: ", permitir_padrao = True)
     quantia = obter_quantia()
     categoria = obter_categoria()
     descricao = obter_descricao()
     CSV.add_entrada(data, quantia, categoria, descricao)

def plot_transacoes(df):
    df.set_index('date', inplace=True)

    df_entrada = ( 
        df[df["categoria"] == "Entrada"]
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
    )

    df_despesa = (
        df[df["categoria"] == "Despesa"]
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
    )

   

def main():
     while True:
          print("\n1. Adicionar nova transação")
          print("2. Ver transações e resumo dentro de um intervalo de datas")
          print("3. Sair")
          escolha = input("Digite o nº da sua escolha (1-3): ")

          if escolha == "1":
               add()
          elif escolha == "2":
               inicio_data = obter_data("Informe a data incial (dd-mm-aaaa): ")
               final_data = obter_data("Informe a data final do intervalo (dd-mm-aaaa): ")
               CSV.obter_transacoes(inicio_data, final_data)
          elif escolha == "3":
               print("Saindo...")
               break
          else:
               print("Escolha inválida. Digite 1, 2 ou 3.")

if __name__ == "__main__":
    main()
