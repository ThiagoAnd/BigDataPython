import pandas as pd
import xlrd
import os

pd.set_option('display.max_columns', 30)
pd.set_option('display.width', 20000)
pd.set_option('display.max_rows', 50000)

source = "Dados"

dir_list = os.listdir(source)

os.chdir(source)
dadosMaster = pd.DataFrame([])
for i in range(len(dir_list)):
    filename = dir_list[i]
    dados = pd.read_excel(filename)
    dadosMaster = dadosMaster.append(dados)

#print(dados[dados['views'] == dados['views'].max()])
# print(dados.rename(columns={'date': 'Data', 'watch_time_minutes': 'Minutos assistidos', 'views': 'visualizacoes'}))
# print(dados['likes'].value_counts())
# #print(filename)

# print(dados['date'])
# print(dados.describe())
# print(dados.loc[dados['date'] == "2019-05-30"])

#print(dadosMaster.sort_values(by=['date']))
#print(dadosMaster.loc[dados['date'] == "2018-05-31"])


dadosMaster['NOVO'] = dadosMaster.views.max()
#print(dadosMaster[['date', 'views', 'NOVO']].sort_values(by=['date']))
#1564
print(dadosMaster.groupby(['date']).mean())

#print(dadosMaster.groupby(date))