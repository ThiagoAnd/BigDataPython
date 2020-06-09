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
   # book = pd.ExcelFile(filename)
    dados = pd.read_excel(filename)
    print(dados)








'''
def xlread(arq_xls):
    """
    Gerador que le arquivo .xls
    """
    # Abre o arquivo
    xls = xlrd.open_workbook(arq_xls)
    # Pega a primeira planilha do arquivo
    plan = xls.sheets()[0]

    # Para i de zero ao numero de linhas da planilha
    for i in range(plan.nrows):
        # Le os valores nas linhas da planilha
        yield plan.row_values(i)

for linha in xlread('Dados/0NMfcDpYXo_2018-05-31_2019-05-31.xlsx'):
    print (linha)


'''








'''
dados = pd.read_excel('Dados/0NMfcDpYXo_2018-05-31_2019-05-31.xlsx')
print(dados)
'''