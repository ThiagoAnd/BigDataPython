import pandas as pd
import xlrd
import os
import matplotlib.pyplot


dados = pd.read_excel('Dados/0NMfcDpYXo_2018-05-31_2019-05-31.xlsx')

matplotlib.pyplot
#matplotlib.pyplot.scatter(dados['likes'], dados['views'], dados['likes'])
#dados['likes'].plot.hist(bins=30, edgecolor='black', title="Número de likes" ) # barra horizontal
#dados['likes'].value_counts().plot.bar()      #barras vertica
#dados['likes'].value_counts().plot.barh()     #barras Horiental
#dados['date'].value_counts().plot.barh(title="Número de likes")   #barras Horiental com titulos
#dados.plot.scatter(x='views', y='likes', s=.5)
#dados.sample(frac=.1).plot.scatter(x='views', y='likes')   #grafico de area
#dados.plot.hist(bins=30, edgecolor='black')      #grafico de area
#matplotlib.pyplot.plot(dados.likes, dados.date)

matplotlib.pyplot.show()

'''
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
valores = [105235, 107697, 110256, 109236, 108859, 109986]
matplotlib.pyplot.plot(meses, valores)

matplotlib.pyplot.show()
'''