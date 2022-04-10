import plotly.express as px
import pandas as pd


df = pd.read_csv('files/ex4_user_1.csv') # Для второго юзера используется полученный на выходе файл из второго задания
# output_2.txt
fig = px.scatter(df, x='Date', y='Status', color='Status',
                 color_discrete_sequence=["red", "green"],
                 title='Status online User_1')
fig.update_xaxes(rangeslider_visible=True)
fig.show()