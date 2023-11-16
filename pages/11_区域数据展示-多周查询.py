import streamlit as st
import pandas as pd
from streamlit_extras.add_vertical_space import add_vertical_space

st.title("北京分公司区域数据统计:thumbsup:")
data = pd.read_csv("pages/北京分公司营销周报汇总2023.csv",encoding="utf-8")
# data = pd.read_excel("pages/test.xlsx")
add_vertical_space(3)
st.subheader("查看一段时期的区域数据")

# 创建两个滑块用于选择开始周数和结束周数
start_week = st.slider("选择开始周数", min_value=data["第几周"].min(), max_value=data["第几周"].max(), value=data["第几周"].min())
end_week = st.slider("选择结束周数", min_value=data["第几周"].min(), max_value=data["第几周"].max(), value=data["第几周"].max())

# 将 "总计" 和 "第几周" 列的数据类型转换为字符串
data["第几周"] = data["第几周"].astype(str)

# 获取所有部门的列表
all_departments = data["部门"].unique()

# 创建多选框来选择部门
selected_departments = st.multiselect("选择部门", all_departments, all_departments)


# 根据滑块的值和所选部门过滤数据
filtered_data = data[(data["第几周"] >= str(start_week)) & (data["第几周"] <= str(end_week)) & (data["部门"].isin(selected_departments))]

# 将带有"-"字符的列转换为数值
numeric_cols = filtered_data.columns[3:]
for col in numeric_cols:
    filtered_data.loc[:, col] = pd.to_numeric(filtered_data[col], errors='coerce')

summary_row = filtered_data[numeric_cols].sum()
# Round numeric columns and handle non-numeric types
summary_row = summary_row.apply(lambda x: round(x, 2) if pd.api.types.is_numeric_dtype(x) else x)
summary_row["部门"] = "总计"

# 将空值替换为0
filtered_data = filtered_data.fillna(0)
# 根据"本年新增市值"字段从大到小进行排序
filtered_data = filtered_data.sort_values(by="本年新增市值", ascending=False)

# 将汇总行添加到过滤后的数据中
filtered_data = pd.concat([filtered_data, summary_row.to_frame().T], ignore_index=True)
# 使用 apply 方法来保留小数点后两位
filtered_data = filtered_data.apply(lambda x: round(x, 2) if pd.api.types.is_numeric_dtype(x) else x)

add_vertical_space(2)
# 显示过滤后的数据和汇总行
st.write(f"过滤后的数据，从第{start_week}周到第{end_week}周的数据按本年新增市值排序：")
st.write(filtered_data)
