import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file
df = pd.read_excel("data/HR_Employee_Analytics_Dataset.xlsx")

# -------------------------------
# PIE CHART - Employee Attrition
# -------------------------------
attrition_count = df["Attrition"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(attrition_count,
        labels=attrition_count.index,
        autopct="%1.1f%%",
        startangle=90)

plt.title("Employee Attrition")
plt.show()

# ------------------------------------
# BAR CHART - Average Salary by Department
# ------------------------------------
average_salary = df.groupby("Department")["Salary"].mean()

plt.figure(figsize=(8,5))
average_salary.plot(kind="bar")

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()