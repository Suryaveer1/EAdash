import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Page configuration
st.set_page_config(page_title="HR Attrition Dashboard", layout="wide")

# Load dataset
@st.cache_data

def load_data():
    df = pd.read_csv("EA.csv")
    return df

df = load_data()

# Sidebar filters
st.sidebar.title("Filter Options")

dept_filter = st.sidebar.multiselect("Select Department:", df['Department'].unique(), default=df['Department'].unique())
gender_filter = st.sidebar.multiselect("Select Gender:", df['Gender'].unique(), default=df['Gender'].unique())
overtime_filter = st.sidebar.multiselect("OverTime Status:", df['OverTime'].unique(), default=df['OverTime'].unique())

filtered_df = df[(df['Department'].isin(dept_filter)) &
                 (df['Gender'].isin(gender_filter)) &
                 (df['OverTime'].isin(overtime_filter))]

st.title("📊 HR Analytics Dashboard - Employee Attrition")
st.markdown("""
This dashboard provides HR leaders and stakeholders with key insights into employee attrition patterns using various demographic and job-related factors.
""")

# --- Charts ---
st.markdown("### 1. Attrition by Age")
fig1 = px.histogram(filtered_df, x="Age", color="Attrition", barmode="group")
st.plotly_chart(fig1)

st.markdown("### 2. Gender Distribution and Attrition")
fig2 = px.histogram(filtered_df, x="Gender", color="Attrition", barmode="group")
st.plotly_chart(fig2)

st.markdown("### 3. Department vs Attrition")
fig3 = px.histogram(filtered_df, x="Department", color="Attrition", barmode="group")
st.plotly_chart(fig3)

st.markdown("### 4. Monthly Income Distribution")
fig4 = px.box(filtered_df, x="Attrition", y="MonthlyIncome", color="Attrition")
st.plotly_chart(fig4)

st.markdown("### 5. Attrition by Marital Status")
fig5 = px.histogram(filtered_df, x="MaritalStatus", color="Attrition", barmode="group")
st.plotly_chart(fig5)

st.markdown("### 6. Job Role vs Attrition")
fig6 = px.histogram(filtered_df, x="JobRole", color="Attrition", barmode="group")
st.plotly_chart(fig6)

st.markdown("### 7. Overtime Impact on Attrition")
fig7 = px.histogram(filtered_df, x="OverTime", color="Attrition", barmode="group")
st.plotly_chart(fig7)

st.markdown("### 8. Performance Rating vs Attrition")
fig8 = px.histogram(filtered_df, x="PerformanceRating", color="Attrition", barmode="group")
st.plotly_chart(fig8)

st.markdown("### 9. Attrition by Work-Life Balance")
fig9 = px.histogram(filtered_df, x="WorkLifeBalance", color="Attrition", barmode="group")
st.plotly_chart(fig9)

st.markdown("### 10. Years at Company vs Attrition")
fig10 = px.box(filtered_df, x="Attrition", y="YearsAtCompany", color="Attrition")
st.plotly_chart(fig10)

st.markdown("### 11. Education Field vs Attrition")
fig11 = px.histogram(filtered_df, x="EducationField", color="Attrition", barmode="group")
st.plotly_chart(fig11)

st.markdown("### 12. Environment Satisfaction vs Attrition")
fig12 = px.histogram(filtered_df, x="EnvironmentSatisfaction", color="Attrition", barmode="group")
st.plotly_chart(fig12)

st.markdown("### 13. Attrition by Job Involvement")
fig13 = px.histogram(filtered_df, x="JobInvolvement", color="Attrition", barmode="group")
st.plotly_chart(fig13)

st.markdown("### 14. Job Level vs Attrition")
fig14 = px.histogram(filtered_df, x="JobLevel", color="Attrition", barmode="group")
st.plotly_chart(fig14)

st.markdown("### 15. Training Times Last Year")
fig15 = px.histogram(filtered_df, x="TrainingTimesLastYear", color="Attrition", barmode="group")
st.plotly_chart(fig15)

st.markdown("### 16. Correlation Heatmap")
plt.figure(figsize=(12, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, fmt=".1f", cmap="coolwarm")
st.pyplot(plt)

st.markdown("### 17. Age vs Monthly Income Scatterplot")
fig17 = px.scatter(filtered_df, x="Age", y="MonthlyIncome", color="Attrition")
st.plotly_chart(fig17)

st.markdown("### 18. Years with Current Manager vs Attrition")
fig18 = px.box(filtered_df, x="Attrition", y="YearsWithCurrManager", color="Attrition")
st.plotly_chart(fig18)

st.markdown("### 19. Total Working Years vs Attrition")
fig19 = px.box(filtered_df, x="Attrition", y="TotalWorkingYears", color="Attrition")
st.plotly_chart(fig19)

st.markdown("### 20. Interactive Table View")
st.dataframe(filtered_df)

# Download button
st.download_button("Download Filtered Data", data=filtered_df.to_csv(index=False), file_name='filtered_data.csv')
