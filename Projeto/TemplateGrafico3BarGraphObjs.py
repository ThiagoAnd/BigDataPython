

import xlrd

import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go

fig = go.Figure(data=go.Bar(x = ['=', 'Maçã', 'Uva'],
                y = [10, 20, 30],
                name = 'Gráfico 1',
                marker = {'color': '#feca57'}))

fig.write_html('first_figure.html', auto_open=True)
