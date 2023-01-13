import streamlit as st
import pandas as pd
import os
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

st.title('米の食味試験　結果')
st.write('学部3年生15名に対して精白米の食味試験を行なった。')
st.write('ななつぼしを基準米として、相対評価を行なった。')
#CSVファイルの読み込み
#os.chdir("")
df = pd.read_csv("Rice_Taste_Test_result.csv")
st.dataframe(df)

st.header("米の食味評価結果のグラフ")

import statistics

df_1 = df[df['品種'].isin(['ななつぼし'])]
data_1 =[]
theta=["精白米外観", "外観", "香り","硬さ","粘り","総合評価"]

for i in range(len(theta)):
  df_mean = statistics.mean(df_1[theta[i]])
  data_1.append(df_mean)

df_1 = pd.DataFrame(dict(
    r=data_1,
    theta=["精白米外観", "外観", "香り","硬さ","粘り","総合評価"]))
fig_rader_1 = px.line_polar(df_1, r='r', theta='theta', line_close=True, range_r=[-5,5], labels="ななつぼし", title="ななつぼし",height=400,width=400)
fig_rader_1.update_traces(fill='toself')


df_2 = df[df['品種'].isin(['こしひかり'])]
data_2 =[]
theta=["精白米外観", "外観", "香り","硬さ","粘り","総合評価"]

for i in range(len(theta)):
  df_mean = statistics.mean(df_2[theta[i]])
  data_2.append(df_mean)

df_2 = pd.DataFrame(dict(
    r=data_2,
    theta=["精白米外観", "外観", "香り","硬さ","粘り","総合評価"]))
fig_rader_2 = px.line_polar(df_2, r='r', theta='theta', line_close=True, range_r=[-5,5], labels="こしひかり", title="こしひかり",height=400,width=400)
fig_rader_2.update_traces(fill='toself')


df_3 = df[df['品種'].isin(['雪若丸'])]
data_3 =[]
theta=["精白米外観", "外観", "香り","硬さ","粘り","総合評価"]

for i in range(len(theta)):
  df_mean = statistics.mean(df_3[theta[i]])
  data_3.append(df_mean)

df_3 = pd.DataFrame(dict(
    r=data_3,
    theta=["精白米外観", "外観", "香り","硬さ","粘り","総合評価"]))
fig_rader_3 = px.line_polar(df_3, r='r', theta='theta', line_close=True, range_r=[-5,5], labels="雪若丸", title="雪若丸",height=400,width=400)
fig_rader_3.update_traces(fill='toself')


df_4 = df[df['品種'].isin(['ゆめぴりか'])]
data_4 =[]
theta=["精白米外観", "外観", "香り","硬さ","粘り","総合評価"]


for i in range(len(theta)):
  df_mean = statistics.mean(df_4[theta[i]])
  data_4.append(df_mean)

df_4 = pd.DataFrame(dict(
    r=data_4,
    theta=["精白米外観", "外観", "香り","硬さ","粘り","総合評価"]))
fig_rader_4 = px.line_polar(df_4, r='r', theta='theta', line_close=True, range_r=[-5,5], labels="ゆめぴりか", title="ゆめぴりか",height=400,width=400)
fig_rader_4.update_traces(fill='toself')

col1, col2 = st.columns(2)
with col1:
	st.write(fig_rader_1)
	st.write(fig_rader_2)
with col2:
	st.write(fig_rader_3)
	st.write(fig_rader_4)

st.header("各評価項目の結果")
data_bar_1 = [data_1[0], data_2[0], data_3[0], data_4[0]]
label=["ななつぼし", "こしひかり", "雪若丸","ゆめぴりか"]
fig_bar_1 = px.bar(
    x=label,
    y=data_bar_1
    )
fig_bar_1.update_layout(height=300,width=300,
                  xaxis=dict(title='精白米外観'),
                  yaxis=dict(title='value', range=[-3,3])
)


data_bar_2 = [data_1[1], data_2[1], data_3[1], data_4[1]]
label=["ななつぼし", "こしひかり", "雪若丸","ゆめぴりか"]
fig_bar_2 = px.bar(
    x=label,
    y=data_bar_2
    )
fig_bar_2.update_layout(height=300,width=300,
                  xaxis=dict(title='外観'),
                  yaxis=dict(title='value', range=[-3,3])
)


data_bar_3 = [data_1[2], data_2[2], data_3[2], data_4[2]]
label=["ななつぼし", "こしひかり", "雪若丸","ゆめぴりか"]
fig_bar_3 = px.bar(
    x=label,
    y=data_bar_3
    )
fig_bar_3.update_layout(height=300,width=300,
                  xaxis=dict(title='香り'),
                  yaxis=dict(title='value', range=[-3,3])
)


data_bar_4 = [data_1[3], data_2[3], data_3[3], data_4[3]]
label=["ななつぼし", "こしひかり", "雪若丸","ゆめぴりか"]
fig_bar_4 = px.bar(height=300,width=300,
    x=label,
    y=data_bar_4
    )
fig_bar_4.update_layout(
                  xaxis=dict(title='硬さ'),
                  yaxis=dict(title='value', range=[-3,3])
)


data_bar_5 = [data_1[4], data_2[4], data_3[4], data_4[4]]
label=["ななつぼし", "こしひかり", "雪若丸","ゆめぴりか"]
fig_bar_5 = px.bar(height=300,width=300,
    x=label,
    y=data_bar_5
    )
fig_bar_5.update_layout(
                  xaxis=dict(title='粘り'),
                  yaxis=dict(title='value', range=[-3,3])
)


data_bar_6 = [data_1[5], data_2[5], data_3[5], data_4[5]]
label=["ななつぼし", "こしひかり", "雪若丸","ゆめぴりか"]
fig_bar_6 = px.bar(height=300,width=300,
    x=label,
    y=data_bar_6
    )
fig_bar_6.update_layout(
                  xaxis=dict(title='総合評価'),
                  yaxis=dict(title='value', range=[-3,3])
)
col1, col2, col3 = st.columns(3)
with col1:
	st.write(fig_bar_1)
	st.write(fig_bar_4)
with col2:
	st.write(fig_bar_2)
	st.write(fig_bar_5)
with col3:
	st.write(fig_bar_3)
	st.write(fig_bar_6)

st.write("有意差")
st.write("外観品質：こしひかり<ゆめぴりか")
st.write("外観品質：ななつぼし< ゆめぴりか ")
st.write("外観品質：雪若丸<ゆめぴりか")
st.write('硬さ：こしひかり＜ゆめぴりか')
st.write('硬さ：雪若丸＜ゆめぴりか')
st.write('総合評価：こしひかり＜ゆめぴりか')


st.header("各評価項目の関係")


data_scatter_1 = df['精白米外観']
data_scatter_2 = df['外観']

fig_scatter_1 = px.scatter(height=300,width=300,x=data_scatter_1, y=data_scatter_2)
fig_scatter_1.update_layout(
                  xaxis=dict(title='精白米外観', range=[-4,4]),
                  yaxis=dict(title='外観', range=[-4,4])
)



data_scatter_1 = df['精白米外観']
data_scatter_3 = df['香り']

fig_scatter_2 = px.scatter(height=300,width=300,x=data_scatter_1, y=data_scatter_3)
fig_scatter_2.update_layout(
                  xaxis=dict(title='精白米外観', range=[-4,4]),
                  yaxis=dict(title='香り', range=[-4,4])
)



data_scatter_1 = df['精白米外観']
data_scatter_3 = df['硬さ']

fig_scatter_3 = px.scatter(height=300,width=300,x=data_scatter_1, y=data_scatter_3)
fig_scatter_3.update_layout(
                  xaxis=dict(title='精白米外観', range=[-4,4]),
                  yaxis=dict(title='硬さ', range=[-4,4])
)



data_scatter_1 = df['精白米外観']
data_scatter_4 = df['粘り']

fig_scatter_4 = px.scatter(height=300,width=300,x=data_scatter_1, y=data_scatter_4)
fig_scatter_4.update_layout(
                  xaxis=dict(title='精白米外観', range=[-4,4]),
                  yaxis=dict(title='粘り', range=[-4,4])
)



data_scatter_1 = df['精白米外観']
data_scatter_5 = df['総合評価']

fig_scatter_5 = px.scatter(height=300,width=300,x=data_scatter_1, y=data_scatter_5)
fig_scatter_5.update_layout(
                  xaxis=dict(title='精白米外観', range=[-4,4]),
                  yaxis=dict(title='総合評価', range=[-4,4])
)



data_scatter_3 = df['香り']
data_scatter_2 = df['外観']

fig_scatter_6 = px.scatter(height=300,width=300,x=data_scatter_3, y=data_scatter_2)
fig_scatter_6.update_layout(
                  xaxis=dict(title='香り', range=[-4,4]),
                  yaxis=dict(title='外観', range=[-4,4])
)



data_scatter_4 = df['硬さ']
data_scatter_2 = df['外観']

fig_scatter_7 = px.scatter(height=300,width=300,x=data_scatter_4, y=data_scatter_2)
fig_scatter_7.update_layout(
                  xaxis=dict(title='硬さ', range=[-4,4]),
                  yaxis=dict(title='外観', range=[-4,4])
)



data_scatter_5 = df['粘り']
data_scatter_2 = df['外観']

fig_scatter_8 = px.scatter(height=300,width=300,x=data_scatter_5, y=data_scatter_2)
fig_scatter_8.update_layout(
                  xaxis=dict(title='粘り', range=[-4,4]),
                  yaxis=dict(title='外観', range=[-4,4])
)



data_scatter_6 = df['総合評価']
data_scatter_2 = df['外観']

fig_scatter_9 = px.scatter(height=300,width=300,x=data_scatter_6, y=data_scatter_2)
fig_scatter_9.update_layout(
                  xaxis=dict(title='総合評価', range=[-4,4]),
                  yaxis=dict(title='外観', range=[-4,4])
)



data_scatter_3 = df['香り']
data_scatter_4 = df['硬さ']

fig_scatter_10 = px.scatter(height=300,width=300,x=data_scatter_3, y=data_scatter_4)
fig_scatter_10.update_layout(
                  xaxis=dict(title='香り', range=[-4,4]),
                  yaxis=dict(title='硬さ', range=[-4,4])
)



data_scatter_3 = df['香り']
data_scatter_5 = df['粘り']

fig_scatter_11 = px.scatter(height=300,width=300,x=data_scatter_3, y=data_scatter_5)
fig_scatter_11.update_layout(
                  xaxis=dict(title='香り', range=[-4,4]),
                  yaxis=dict(title='粘り', range=[-4,4])
)



data_scatter_3 = df['香り']
data_scatter_6 = df['総合評価']

fig_scatter_12 = px.scatter(height=300,width=300,x=data_scatter_3, y=data_scatter_6)
fig_scatter_12.update_layout(
                  xaxis=dict(title='香り', range=[-4,4]),
                  yaxis=dict(title='総合評価', range=[-4,4])
)



data_scatter_4 = df['硬さ']
data_scatter_5 = df['粘り']

fig_scatter_13 = px.scatter(height=300,width=300,x=data_scatter_3, y=data_scatter_5)
fig_scatter_13.update_layout(
                  xaxis=dict(title='硬さ', range=[-4,4]),
                  yaxis=dict(title='粘り', range=[-4,4])
)



data_scatter_4 = df['硬さ']
data_scatter_6 = df['総合評価']

fig_scatter_14 = px.scatter(height=300,width=300,x=data_scatter_3, y=data_scatter_6)
fig_scatter_14.update_layout(
                  xaxis=dict(title='硬さ', range=[-4,4]),
                  yaxis=dict(title='総合評価', range=[-4,4])
)



data_scatter_6 = df['総合評価']
data_scatter_5 = df['粘り']

fig_scatter_15 = px.scatter(height=300,width=300,x=data_scatter_6, y=data_scatter_5)
fig_scatter_15.update_layout(
                  xaxis=dict(title='総合評価', range=[-4,4]),
                  yaxis=dict(title='粘り', range=[-4,4])
)



col1, col2, col3, col4 = st.columns(4)
with col1:
	st.write(fig_scatter_1)
	st.write(fig_scatter_5)
	st.write(fig_scatter_9)
	st.write(fig_scatter_13)
with col2:
	st.write(fig_scatter_2)
	st.write(fig_scatter_6)
	st.write(fig_scatter_10)
	st.write(fig_scatter_14)
with col3:
	st.write(fig_scatter_3)
	st.write(fig_scatter_7)
	st.write(fig_scatter_11)
	st.write(fig_scatter_15)
with col4:
	st.write(fig_scatter_4)
	st.write(fig_scatter_8)
	st.write(fig_scatter_12)
	st.write(fig_scatter_14)