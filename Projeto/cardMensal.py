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

dadosMaster['diasSemanas'] = pd.to_datetime(dadosMaster['date']).dt.day_name()
'''
print(dadosMaster[['mes', 'cards_shown']].groupby('mes').sum())
print(dadosMaster[['mes', 'card_clicks']].groupby('mes').sum())
print(dadosMaster[['mes', 'card_teasers_shown']].groupby('mes').sum())
print( dadosMaster[['mes', 'card_teaser_clicks']].groupby('mes').sum())
'''

numShows = dadosMaster[['mes', 'cards_shown']].groupby('mes').sum()
numShows.reset_index(inplace=True)

numCliks = dadosMaster[['mes', 'card_clicks']].groupby('mes').sum()
numCliks.reset_index(inplace=True)

numTeaserShows = dadosMaster[['mes', 'card_teasers_shown']].groupby('mes').sum()
numTeaserShows.reset_index(inplace=True)

numTeaserCliks = dadosMaster[['mes', 'card_teaser_clicks']].groupby('mes').sum()
numTeaserCliks.reset_index(inplace=True)

fig = go.Figure()

fig.add_trace(go.Bar(x = numShows['mes'].values, y=numShows['cards_shown'].values,
                    marker={'color': '#1E90FF'},
                    name='Card Shows'))

fig.add_trace(go.Bar(x=numCliks['mes'].values, y = numCliks['card_clicks'].values,
                     marker={'color': '#00FF00'},
                    name='Card Clicks'))

fig.add_trace(go.Bar(x = numTeaserShows['mes'].values, y=numTeaserShows['card_teasers_shown'].values,
                    marker={'color': '#1E90FF'},
                    name='Card Shows'))

fig.add_trace(go.Bar(x=numTeaserCliks['mes'].values, y = numTeaserCliks['card_teaser_clicks'].values,
                     marker={'color': '#ADFF2F'},
                    name='Card Clicks'))

fig.update_layout(
    title={
        'text': "Media mensal de Cards de 2018 - 2019",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},

    xaxis_title="Meses",
    yaxis_title="Quantidade de clicks/shows",
    legend_title_text='Dias',
    xaxis=dict(

       type='category'
    ),

    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#297554"

    )
)

fig.write_html('../Output/MediaCardMensal.html', auto_open=True)
#fig.show()



'''
fig = go.Figure(data=go.Bar(x = ['=', 'Maçã', 'Uva'],
                y = [10, 20, 30],
                name = 'Gráfico 1',
                marker = {'color': '#feca57'}))'''