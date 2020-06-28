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


domingoDF = dadosMaster.loc[dadosMaster['dia'] == "Sunday"]
domingoDF = domingoDF[['mes', 'views']].groupby('mes').mean()
domingoDF.reset_index(inplace=True)

segundaDF = dadosMaster.loc[dadosMaster['dia'] == "Monday"]
segundaDF = segundaDF[['mes', 'views']].groupby('mes').mean()
segundaDF.reset_index(inplace=True)

tercaDF = dadosMaster.loc[dadosMaster['dia'] == "Tursday"]
tercaDF = tercaDF[['mes', 'views']].groupby('mes').mean()
tercaDF.reset_index(inplace=True)

quartaDF = dadosMaster.loc[dadosMaster['dia'] == "Wednesday"]
quartaDF = quartaDF[['mes', 'views']].groupby('mes').mean()
quartaDF.reset_index(inplace=True)

quintaDF = dadosMaster.loc[dadosMaster['dia'] == "Thursday"]
quintaDF = quintaDF[['mes', 'views']].groupby('mes').mean()
quintaDF.reset_index(inplace=True)

sextaDF = dadosMaster.loc[dadosMaster['dia'] == "Friday"]
sextaDF = sextaDF[['mes', 'views']].groupby('mes').mean()
sextaDF.reset_index(inplace=True)


sabadoDF = dadosMaster.loc[dadosMaster['dia'] == "Saturday"]
sabadoDF = sabadoDF[['mes', 'views']].groupby('mes').mean()
sabadoDF.reset_index(inplace=True)

fig = go.Figure()
fig.add_trace(go.Scatter(x=domingoDF['mes'].values, y=domingoDF['views'].values,
                    mode='lines+markers',
                    name='Domingo'))

fig.add_trace(go.Scatter(x=segundaDF['mes'].values, y=segundaDF['views'].values,
                    mode='lines+markers',
                    name='Segunda'))

fig.add_trace(go.Scatter(x=segundaDF['mes'].values, y=tercaDF['views'].values,
                    mode='lines+markers',
                    name='Terça'))

fig.add_trace(go.Scatter(x=segundaDF['mes'].values, y=quartaDF['views'].values,
                    mode='lines+markers',
                    name='Quarta'))

fig.add_trace(go.Scatter(x=segundaDF['mes'].values, y=quintaDF['views'].values,
                    mode='lines+markers',
                    name='Quinta'))

fig.add_trace(go.Scatter(x=segundaDF['mes'].values, y=sextaDF['views'].values,
                    mode='lines+markers',
                    name='Sexta'))

fig.add_trace(go.Scatter(x=segundaDF['mes'].values, y=sabadoDF['views'].values,
                    mode='lines+markers',
                    name='Sabado'))

fig.write_html('./Output/MediaSemanalMensalDeViews.html', auto_open=True)
#fig.show()


