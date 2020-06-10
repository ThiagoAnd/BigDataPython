import pandas as pd
import xlrd

pd.set_option('display.max_columns', 26)
pd.set_option('display.width', 2000)
pd.set_option('display.max_rows', 500)

dados = pd.read_excel('Dados/0NMfcDpYXo_2018-05-31_2019-05-31.xlsx')

print(dados.rename(columns={'date': 'Data'}))

