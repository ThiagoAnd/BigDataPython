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
dadosMaster['dia'] = pd.to_datetime(dadosMaster['date'])
dadosMaster['dia'] = dadosMaster['dia'].dt.day_name()

dadosMaster['mes'] = dadosMaster['date'].astype('str').str[:7]
dadosMaster.reset_index(drop=True)
# print(dadosMaster.head())
# print(dadosMaster['dia'])
sextaDF = dadosMaster.loc[dadosMaster['dia'] == "Friday"]
# print(sextaDF.head())

sextaDF = sextaDF[['mes', 'views']].groupby('mes').mean()
sextaDF.reset_index(inplace=True)

print(sextaDF)


iris = px.data.iris()
fig = px.scatter(iris, x="sepal_width", y="sepal_length", color="species")
df = pd.DataFrame({
    'x':[1,2,3,4],
    'y':[5,6,7,8],})
fig2 = px.bar(df, x="x", y="y")
fig.add_trace(fig2.data[0])
fig.write_html('./Output/TemplateTrace.html', auto_open=True)

fig.show()

# output = dadosMaster[['mes', 'views']].groupby('mes').mean()

# print(Sexta)
# print(Sexta['dia'])
# dadosMaster['Dia'] = dadosMaster
# print(dadosMaster)
# print(dadosMaster[['date','datinha']])
# print(dadosMaster.groupby('datinha').max())
# dadosMaster['new'] = dadosMaster['date'].astype('str').str[:7]


# output = dadosMaster[['new','views']].groupby('new').mean()
# output.reset_index(inplace=True)
# print(output['views'].values)


'''

import plotly.graph_objs as go

fig = go.Figure(data=go.Bar(x = output['new'].values,
                y = output['views'].values,
                name = 'Gráfico 1',
                marker = {'color': '#297554'}))

fig.update_layout(
    title={
        'text': "Media mensal de views 2018 - 2019",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},

    xaxis_title="Meses",
    yaxis_title="Quantidade de views",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#297554"
    )
)

fig.show()
#fig.write_html('../first_figure.html', auto_open=True)




#print(output)
#Show this way:
#           views
#   new
#print(output.columns.values) #


#print(output.columns.values) # Só mostra a coluna Views



'''
