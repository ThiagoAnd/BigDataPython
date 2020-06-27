import pandas as pd

import plotly.express as px
iris = px.data.iris()
fig = px.scatter(iris, x="sepal_width", y="sepal_length", color="species")
df = pd.DataFrame({
    'x':[1,2,3,4],
    'y':[5,6,7,8],})
fig2 = px.bar(df, x="x", y="y")
fig.add_trace(fig2.data[0])
fig.write_html('../Output/TemplateTrace.html', auto_open=True)

fig.show()
