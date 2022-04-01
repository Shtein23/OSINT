import plotly.express as px
import pandas as pd

# Взять данные из первых двух заданий и построить два графика, которые наиболее наглядно (на ваш взгляд) будут
# визуализировать онлайн статус
# Построение по точкам, чтобы точнее определить статус.
# Для построения используется библиотеки plotly и pandas. Для них достаточно подгрузить размеченный .csv файл.


df = pd.read_csv('files/ex4_user_1.csv') # Для второго юзера используется полученный на выходе файл из второго задания
# output_2.txt
fig = px.scatter(df, x='Date', y='Status', color='Status',
                 color_discrete_sequence=["red", "green"],
                 title='Status online User_1')
fig.update_xaxes(rangeslider_visible=True)
fig.show()