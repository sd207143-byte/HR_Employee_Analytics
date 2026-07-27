import streamlit as st

# ----------------------------
# Page Settings
# ----------------------------
st.set_page_config(
    page_title="HR Employee Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# ----------------------------
# Dashboard Title
# ----------------------------
st.title("📊 HR Employee Analytics Dashboard")

st.success("Welcome to the HR Employee Analytics Project!")

st.write("---")

# ----------------------------
# Project Overview
# ----------------------------
st.header("📖 Project Overview")

st.write("""
This project analyses employee information using Data Analytics.

The dashboard helps the HR department understand:

• Employee Performance

• Salary Analysis

• Attrition Analysis

• Department Analysis

• Employee Reports
""")

st.write("---")

# ----------------------------
# Technologies Used
# ----------------------------
st.header("🛠 Technologies Used")

st.write("""
✅ Python

✅ Pandas

✅ Matplotlib

✅ Streamlit

✅ Excel
""")

st.write("---")

# ----------------------------
# Project Features
# ----------------------------
st.header("🚀 Project Features")

st.write("""
📊 Dashboard

📋 Reports

📈 Charts

📉 Analytics

👨 Employee Details

💰 Salary Insights

🏢 Department Insights
""")

st.write("---")

# ----------------------------
# Footer
# ----------------------------
st.info(" Data Analytics Project - HR Employee Analytics")
