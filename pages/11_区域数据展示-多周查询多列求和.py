import streamlit as st
import pandas as pd
from streamlit_extras.add_vertical_space import add_vertical_space
import seaborn as sns
import numpy as np
import altair as alt
from matplotlib import  pyplot as plt
from streamlit_extras.dataframe_explorer import dataframe_explorer

st.title("北京分公司区域数据统计:thumbsup:")
# df = pd.read_csv("pages/北京分公司营销周报汇总2023.csv",encoding="utf-8")
df = pd.read_excel("pages/北京分公司营销周报汇总2023.xlsx")

add_vertical_space(3)
st.subheader("查看一段时期的区域数据",divider="rainbow")
add_vertical_space(3)

# 创建两个滑块用于选择开始周数和结束周数
start_week = st.slider("选择开始周数", min_value=df["第几周"].min(), max_value=df["第几周"].max(), value=10)
end_week = st.slider("选择结束周数", min_value=df["第几周"].min(), max_value=df["第几周"].max(), value=df["第几周"].max())

# Convert the column "第几周" to strings
df["第几周"] = df["第几周"].astype(str)

st.error("你选择的范围是："+ str(start_week) + " 到 " + str(end_week)+"周")
# 数据范围
df2=df[(df["第几周"] >= str(start_week))& (df["第几周"] <= str(end_week))]
add_vertical_space(3)
# st.dataframe(df2)
with st.expander("过滤excel数据"):
    filtered_df=dataframe_explorer(df2,case=False)
    st.dataframe(filtered_df,use_container_width=True)

st.write("以下是当前期间的统计数据：")
a1,a2,a3 = st.columns(3)
with a1:  #本周新增市值
    st.write("新增市值(万元)",divider="rainbow") #彩虹分割线
    source=pd.DataFrame({
        "新增市值(万元)":df2["本周新增市值"],
        "部门":df2["部门"],
    })
    bar_chart = alt.Chart(source).mark_bar().encode(  # mark_bar条形图  mark_area 区域  mark_boxplot mark_boxplot
        x=alt.X("sum(新增市值(万元)):Q", axis=alt.Axis(format=".2f")), #小数点保留两位
        y=alt.Y("部门:N", sort="-x"))
    st.altair_chart(bar_chart, use_container_width=True)

with a2:  #本周净佣金收入（万）
    st.write("含两融净佣金收入（万）",divider="rainbow") #彩虹分割线
    source=pd.DataFrame({
        "净佣金收入（万）":df2["本周净佣金收入（万）"],
        "部门":df2["部门"],
    })
    bar_chart = alt.Chart(source).mark_bar().encode(  # mark_bar条形图  mark_area 区域  mark_boxplot mark_boxplot
        # x="sum(当前期间净佣金收入（万）):Q",
        x=alt.X("sum(净佣金收入（万）):Q", axis=alt.Axis(format=".2f")), #小数点保留两位
        y=alt.Y("部门:N", sort="-x"))
    st.altair_chart(bar_chart, use_container_width=True)

with a3:  #本周净佣金收入（万）
    st.write("事业和财富净佣金收入(万元)",divider="rainbow") #彩虹分割线
    source=pd.DataFrame({
        "两个部门本周净佣金收入（万）": df2["两个部门本周净佣金收入（万）"],
        "部门": df2["部门"],
    })
    bar_chart = alt.Chart(source).mark_bar().encode(  # mark_bar条形图  mark_area 区域  mark_boxplot mark_boxplot
        # x="sum(当前期间净佣金收入（万）):Q",
        x=alt.X("sum(两个部门本周净佣金收入（万）):Q", axis=alt.Axis(format=".2f")), #小数点保留两位
        y=alt.Y("部门:N", sort="-x"))
    st.altair_chart(bar_chart, use_container_width=True)


st.subheader("统计期间数据矩阵",divider='rainbow')
from streamlit_extras.metric_cards import style_metric_cards
col1,col2,col3=st.columns(3)

col1.metric(label="新开户",value=f"{df2.本周新开户.sum():,.0f}",delta=int(df2['本周新开户'].median()))  #median()表示中位数
col2.metric(label="新增市值(万元)",value=f"{df2.本周新增市值.sum():,.2f}",delta=f"{df2['本周新增市值'].median():,.2f}")
col3.metric(label="净佣金收入(万元)",value=f"{df2['本周净佣金收入（万）'].sum():,.2f}",delta=f"{df2['本周净佣金收入（万）'].median():,.2f}")
style_metric_cards(background_color="#3c4d66",border_left_color="#e6200e",border_color="#00060a")

add_vertical_space(2)
# st.subheader("统计期间新开户最多营业部的详细情况：",divider='rainbow')
# max_value = df2.loc[df2['本周新开户'].idxmax()]
# st.write(max_value)

st.subheader("各个部门 每周佣金收入的对比", divider="rainbow")  # 彩虹分割线
energy_source = pd.DataFrame({
    "部门": df2["部门"],
    "本周净佣金收入（万）": df2["本周净佣金收入（万）"],
    "第几周": df2["第几周"]
})

bar_chart = alt.Chart(energy_source).mark_bar().encode(  # mark_bar条形图  mark_area 区域  mark_boxplot mark_boxplot
    x="第几周:O",
    y="sum(本周净佣金收入（万）):Q",
    color="部门:N"
)
st.altair_chart(bar_chart, use_container_width=True)



# ======================

st.subheader("各个部门 每周新增市值的对比", divider="rainbow")  # 彩虹分割线
energy_source = pd.DataFrame({
    "部门": df2["部门"],
    "本周新增市值": df2["本周新增市值"],
    "第几周": df2["第几周"]
})

bar_chart = alt.Chart(energy_source).mark_bar().encode(  # mark_bar条形图  mark_area 区域  mark_boxplot mark_boxplot
    x="第几周:O",
    y="sum(本周新增市值):Q",
    color="部门:N"
)
st.altair_chart(bar_chart, use_container_width=True)