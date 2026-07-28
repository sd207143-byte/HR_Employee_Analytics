import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="HR Employee Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)


# ---------------- LOAD DATA ----------------

@st.cache_data
def load_data():
    return pd.read_excel(
        "data/HR_Employee_Analytics_Dataset.xlsx"
    )


df = load_data()


# ---------------- TITLE ----------------

st.title("📊 HR Employee Analytics Dashboard")

st.markdown(
    """
    ### Employee Workforce Insights & Business Intelligence Dashboard
    Analyze employee demographics, salary trends, performance,
    departments and workforce patterns.
    """
)


st.divider()


# ---------------- SIDEBAR FILTERS ----------------

st.sidebar.title("🔎 Dashboard Filters")


department = st.sidebar.multiselect(
    "Select Department",
    df["Department"].unique(),
    default=df["Department"].unique()
)


gender = st.sidebar.multiselect(
    "Select Gender",
    df["Gender"].unique(),
    default=df["Gender"].unique()
)


job_role = st.sidebar.multiselect(
    "Select Job Role",
    df["Job_Role"].unique(),
    default=df["Job_Role"].unique()
)


search = st.sidebar.text_input(
    "Employee Search"
)


filtered_df = df[
    (df["Department"].isin(department)) &
    (df["Gender"].isin(gender)) &
    (df["Job_Role"].isin(job_role))
]


if search:
    filtered_df = filtered_df[
        filtered_df.astype(str)
        .apply(
            lambda row:
            row.str.contains(
                search,
                case=False
            ).any(),
            axis=1
        )
    ]


# ---------------- KPI CARDS ----------------


total_employee = len(filtered_df)

avg_salary = filtered_df["Salary"].mean()

avg_exp = filtered_df[
    "Years_at_Company"
].mean()


col1,col2,col3,col4 = st.columns(4)


col1.metric(
    "👥 Total Employees",
    total_employee
)


col2.metric(
    "🏢 Departments",
    filtered_df["Department"].nunique()
)


col3.metric(
    "💰 Average Salary",
    f"£{avg_salary:,.0f}"
)


col4.metric(
    "⭐ Avg Experience",
    f"{avg_exp:.1f} Years"
)



st.divider()



# ==================================================
# CHART 1
# Employees by Department
# ==================================================

st.subheader(
    "🏢 Employees by Department"
)


dept = (
    filtered_df["Department"]
    .value_counts()
    .reset_index()
)

dept.columns=[
    "Department",
    "Employees"
]


fig1 = px.bar(
    dept,
    x="Department",
    y="Employees",
    text="Employees",
    color="Department",
    template="plotly_white"
)


st.plotly_chart(
    fig1,
    use_container_width=True
)



# ==================================================
# CHART 2
# Gender Distribution
# ==================================================


st.subheader(
    "👨‍💼 Gender Distribution"
)


gender_df = (
    filtered_df["Gender"]
    .value_counts()
    .reset_index()
)


gender_df.columns=[
    "Gender",
    "Count"
]


fig2 = px.pie(
    gender_df,
    names="Gender",
    values="Count",
    hole=0.4
)


st.plotly_chart(
    fig2,
    use_container_width=True
)



# ==================================================
# CHART 3
# Salary Distribution
# ==================================================

st.subheader(
    "💰 Salary Distribution"
)


fig3 = px.histogram(
    filtered_df,
    x="Salary",
    nbins=30,
    color="Department",
    template="plotly_white"
)


st.plotly_chart(
    fig3,
    use_container_width=True
)



# ==================================================
# CHART 4
# Job Role Analysis
# ==================================================


st.subheader(
    "💼 Employees by Job Role"
)


role = (
    filtered_df["Job_Role"]
    .value_counts()
    .reset_index()
)


role.columns=[
    "Job Role",
    "Employees"
]


fig4 = px.bar(
    role,
    x="Employees",
    y="Job Role",
    orientation="h",
    color="Employees"
)


st.plotly_chart(
    fig4,
    use_container_width=True
)



# ==================================================
# CHART 5
# Experience Analysis
# ==================================================


st.subheader(
    "📈 Years at Company Analysis"
)


fig5 = px.histogram(
    filtered_df,
    x="Years_at_Company",
    color="Department",
    template="plotly_white"
)


st.plotly_chart(
    fig5,
    use_container_width=True
)



# ==================================================
# CHART 6
# Performance Rating
# ==================================================


if "Performance_Rating" in filtered_df.columns:


    st.subheader(
        "⭐ Employee Performance Rating"
    )


    performance = (
        filtered_df[
            "Performance_Rating"
        ]
        .value_counts()
        .reset_index()
    )


    performance.columns=[
        "Rating",
        "Employees"
    ]


    fig6 = px.bar(
        performance,
        x="Rating",
        y="Employees",
        color="Rating"
    )


    st.plotly_chart(
        fig6,
        use_container_width=True
    )



# ==================================================
# CHART 7
# Salary vs Experience
# ==================================================


st.subheader(
    "💵 Salary vs Experience"
)


fig7 = px.scatter(
    filtered_df,
    x="Years_at_Company",
    y="Salary",
    color="Department",
    hover_data=[
        "Job_Role"
    ]
)


st.plotly_chart(
    fig7,
    use_container_width=True
)



# ==================================================
# CHART 8
# Department Salary
# ==================================================


st.subheader(
    "🏢 Department Average Salary"
)


salary_department = (
    filtered_df
    .groupby(
        "Department"
    )["Salary"]
    .mean()
    .reset_index()
)


fig8 = px.bar(
    salary_department,
    x="Department",
    y="Salary",
    color="Salary"
)


st.plotly_chart(
    fig8,
    use_container_width=True
)



# ==================================================
# CHART 9
# Age Analysis
# ==================================================


if "Age" in filtered_df.columns:


    st.subheader(
        "🎂 Employee Age Analysis"
    )


    fig9 = px.histogram(
        filtered_df,
        x="Age",
        color="Gender"
    )


    st.plotly_chart(
        fig9,
        use_container_width=True
    )



# ==================================================
# CHART 10
# Employee Table
# ==================================================


st.subheader(
    "📋 Employee Details"
)


st.dataframe(
    filtered_df,
    use_container_width=True
)



# ==================================================
# DOWNLOAD BUTTON
# ==================================================


csv = filtered_df.to_csv(
    index=False
)


st.download_button(
    label="⬇ Download Filtered Employee Data",
    data=csv,
    file_name="HR_Filtered_Data.csv",
    mime="text/csv"
)



st.success(
    "Dashboard Loaded Successfully 🚀"
)