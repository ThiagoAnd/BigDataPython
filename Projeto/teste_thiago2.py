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
    print(dados)
