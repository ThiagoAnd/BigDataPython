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

somaDF = dadosMaster.groupby('date').sum()
somaDF['Aproveitamento_End_Element'] = (somaDF['end_screen_element_clicks'] / somaDF['end_screen_elements_shown']) * 100
somaDF['Aproveitamento_End_Element'] = somaDF['Aproveitamento_End_Element'].round(1)
somaDF.reset_index(inplace=True)

mediaDF = dadosMaster.groupby('date').mean()
mediaDF.reset_index(inplace=True)
mediaDF['Aproveitamento_End_Element'] = somaDF['Aproveitamento_End_Element']

fig = go.Figure(data=[go.Scatter(
    x=mediaDF['watch_time_minutes'].values,
    y=mediaDF['Aproveitamento_End_Element'].values,
    mode='markers',
    marker=dict(
        size=25,
    )
)])

fig.update_layout(
    title={
        'text': "Relação do aproveitamento do uso de telas finais por minutos de video assistidos",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},

    xaxis_title="Tempo assistido (Minutes)",
    yaxis_title="Aproveitamento de telas finais no video (%)",

    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#297554"

    )
)

fig.write_html('../Output/AproveitamentoTelasFinais.html', auto_open=True)
