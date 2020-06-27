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

#dadosMaster['novo'] = dadosMaster['date'].str[:7]
#dadosMaster['novo'] = dadosMaster['date'].astype('str').str[:7]

#cats = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

#df['Day of Week'] = df['Day of Week'].astype('category', categories=cats, ordered=True)

#Criando nova coluna
#dadosMaster['new'] = dadosMaster['date'].astype('str').str[:7]
#dadosMaster['Dia'] = dadosMaster['date'].astype('date').dt.day_name()
#dadosMaster['dia'] = pd.to_datetime(dadosMaster['date'])
#dadosMaster['dia'] = dadosMaster['dia'].dt.day_name()

#dadosMaster['Dia'] = dadosMaster
#print(dadosMaster)
print(dadosMaster[['date','datinha']])
#dadosMaster['new'] = dadosMaster['date'].astype('str').str[:7]


dadosMaster[['new','views']].groupby('new').mean()
#output.reset_index(inplace=True)
#print(output['views'].values)

