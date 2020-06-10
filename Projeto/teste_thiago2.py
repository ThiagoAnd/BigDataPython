import pandas as pd
import xlrd
import os

pd.set_option('display.max_columns', 26)
pd.set_option('display.width', 2000)
pd.set_option('display.max_rows', 500)

source = "Dados"

dir_list = os.listdir(source)

os.chdir(source)

for i in range(len(dir_list)):
    filename = dir_list[i]
    dados = pd.read_excel(filename)
    dadosMaster = pd.concat([dados])
# print(dados.rename(columns={'date': 'Data', 'watch_time_minutes': 'Minutos assistidos', 'views': 'visualizacoes'}))
# print(dados['likes'].value_counts())
# #print(filename)

# print(dados['date'])
# print(dados.describe())
# print(dados.loc[dados['date'] == "2019-05-30"])


print(dadosMaster)