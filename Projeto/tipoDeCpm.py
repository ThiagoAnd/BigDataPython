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
dadosMaster.reset_index(drop=True)


numTeaserShows = dadosMaster[['mes', 'cpm']].groupby('mes').sum()
numTeaserShows.reset_index(inplace=True)

numTeaserCliks = dadosMaster[['mes', 'playback_based_cpm']].groupby('mes').sum()
numTeaserCliks.reset_index(inplace=True)

fig = go.Figure()


fig.add_trace(go.Bar(x = numTeaserShows['mes'].values, y=numTeaserShows['cpm'].values,
                    marker={'color': '#1E90FF'},
                    name='Custo por visualização'))

fig.add_trace(go.Bar(x=numTeaserCliks['mes'].values, y = numTeaserCliks['playback_based_cpm'].values,
                     marker={'color': '#ADFF2F'},
                    name='Custo por clicks'))

fig.update_layout(
    title={
        'text': "Comparaçõee mensal de Custo por clique vs Custo por visualização",
        'y': 0.9,
        'x': 0.4,
        'xanchor': 'center',
        'yanchor': 'top'},

    xaxis_title="Meses",
    yaxis_title="Valores Arrecadado",
    legend_title_text='Valor',
    xaxis=dict(

       type='category'
    ),

    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#297554"

    )
)

fig.write_html('../Output/tipoDeCpmValeApena.html', auto_open=True)
#fig.show()



'''
fig = go.Figure(data=go.Bar(x = ['=', 'Maçã', 'Uva'],
                y = [10, 20, 30],
                name = 'Gráfico 1',
                marker = {'color': '#feca57'}))'''