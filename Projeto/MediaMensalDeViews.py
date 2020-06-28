#Faz a media de todos os dias de cada mes e monta um grafico
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

dadosMaster['mes'] = dadosMaster['date'].astype('str').str[:7]

output = dadosMaster[['mes', 'views']].groupby('mes').mean()
output.reset_index(inplace=True)
print("Construção da informaçaõ finalizada")
print("Iniciando construção do grafico")
df = output
px.defaults.color_continuous_scale = px.colors.sequential.Blackbody
fig = px.bar(df, x="mes", y="views", color="mes",

             title="Media mensal de views 2018 - 2019")

fig.update_layout(
    title={
        # 'text': "Media mensal de views 2018 - 2019",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},

    xaxis_title="Meses",
    yaxis_title="Quantidade de views",
    legend_title_text='Meses',
    xaxis=dict(

       type='category'
    ),

    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#297554"

    )
)

fig.write_html('../Output/first_figure.html', auto_open=True)
print("Gravação do grafico finalizada")
fig.show()
