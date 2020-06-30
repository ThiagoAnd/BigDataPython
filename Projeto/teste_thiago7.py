import pandas as pd
import xlrd
import os
import plotly.express as px

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

# print(dados[dados['views'] == dados['views'].max()])
# print(dados.rename(columns={'date': 'Data', 'watch_time_minutes': 'Minutos assistidos', 'views': 'visualizacoes'}))
# print(dados['likes'].value_counts())
# #print(filename)

# print(dados['date'])
# print(dados.describe())
# print(dados.loc[dados['date'] == "2019-05-30"])

# print(dadosMaster.sort_values(by=['date']))
# print(dadosMaster.loc[dados['date'] == "2018-05-31"])


# dadosMaster['novo'] = dadosMaster['date'].str[:7]
# dadosMaster['novo'] = dadosMaster['date'].astype('str').str[:7]

# cats = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# df['Day of Week'] = df['Day of Week'].astype('category', categories=cats, ordered=True)

# Criando nova coluna
# dadosMaster['new'] = dadosMaster['date'].astype('str').str[:7]
# dadosMaster['Dia'] = dadosMaster['date'].astype('date').dt.day_name()


somaDF = dadosMaster.groupby('date').sum()
somaDF['Aproveitamento_End_Element'] = (somaDF['end_screen_element_clicks']/somaDF['end_screen_elements_shown'])*100
somaDF['Aproveitamento_End_Element'] = somaDF['Aproveitamento_End_Element'].round(1)
somaDF.reset_index(inplace=True)


mediaDF = dadosMaster.groupby('date').mean()
mediaDF.reset_index(inplace=True)
mediaDF['Aproveitamento_End_Element']  = somaDF['Aproveitamento_End_Element']
#mediaDF['horas'] = pd.to_datetime(mediaDF['watch_time_minutes'],unit='m').dt.strftime('%H:%M')
#mediaDF['horas'] = pd.to_datetime(mediaDF['watch_time_minutes'],unit='m').dt.strftime('%H:%M:%S')
#mediaDF = mediaDF.round(1)
print(mediaDF)





import plotly.graph_objects as go

#size = [20, 40, 60, 80, 100, 80, 60, 40, 20, 40]
fig = go.Figure(data=[go.Scatter(
    x=mediaDF['watch_time_minutes'].values,
    y=mediaDF['Aproveitamento_End_Element'].values,
    mode='markers',
    marker=dict(
        size=20,
        #sizemode='area',
        #sizeref=2.*max(size)/(40.**2),
        #sizemin=4
    )
)])

fig.update_layout(
    title={
        'text': "Relação do aproveitamento do uso de telas finais por minutos de video assistidos",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},

    xaxis_title="Tempo assistido em geral (Minutes)",
    yaxis_title="Aproveitamento de telas finais no video (%)",



    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#297554"

    )
)

fig.write_html('../Output/bublesTemplate.html', auto_open=True)

#fig.show()

