import pandas as pd
import xlrd
import os
import matplotlib.pyplot

pd.set_option('display.max_columns', 26)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 5000)


'''
source = "Dados"

dir_list = os.listdir(source)

os.chdir(source)




for i in range(len(dir_list)):
    filename = dir_list[i]
   # book = pd.ExcelFile(filename)
    dados = pd.read_excel(filename)

    #print(dados.describe())
'''



#dados = pd.read_excel('Dados/0NMfcDpYXo_2018-05-31_2019-05-31.xlsx')
#df = pd.DataFrame(dados.date,dados.likes)

#matplotlib.pyplot.plot(dados['views'], dados['likes'])
#matplotlib.pyplot.show()

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
valores = [105235, 107697, 110256, 109236, 108859, 109986]
matplotlib.pyplot.plot(meses, valores)

matplotlib.pyplot.show()

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
#print(dados.head(dados.likes == 2)) # true / false

# print(dados['likes'].value_counts())  fazer contagem
#print(dados['likes'].value_counts(normalize = True)) contgem por porcentagem

# print(dados.groupby("date").mean() ["date"].sort_values())  agrupa e organizar os dados

'''
    def truncar(bairro):
        return bairro[:2]
    print(dados["date"].apply(truncar))
'''
# print(dados["views"].value_counts().plot.pie())
# dados.plot.hist(bins=30, edgecolor='black')
# print(dados["views"].value_counts().plot.barh())