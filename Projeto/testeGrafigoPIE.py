import pandas as pd
import xlrd
import os
import plotly.graph_objects as go

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


dadosMaster['dia'] = pd.to_datetime(dadosMaster['date'])
dadosMaster['dia'] = dadosMaster['dia'].dt.day_name()

dadosMaster['mes'] = dadosMaster['date'].astype('str').str[:7]
#dadosMaster.reset_index(drop=True)


# Criando gráfico
# ordem do maior valor para o menor:
cores = ['#96D38C','#FEBFB3','#E1396C']


trace = go.Pie(labels = ['teste1','teste2', 'teste3'],
               values = [5, 10, 15],
               marker = {'colors': cores,
                         'line' : {'color':'#000000','width':2}
                        },
               hoverinfo='label+percent+value',
               pull=[0.001,0.001,0.001],
               direction='clockwise'
              )

# Armazenando gráfico em uma lista:
data = [trace]

# Criando Layout:
layout = go.Layout(title='Classificação de Clientes sobre Pedidos')

# Criando figura que será exibida:
fig = go.Figure(data=data, layout=layout)

fig.write_html('../Output/testePie.html', auto_open=True)
#py.plot(fig)
#fig.show()


