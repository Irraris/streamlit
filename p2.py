import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
tips = pd.read_csv(path)

st.write("""
# Tips at the restaurant
""")

st.write("""
The first 10 dataset records
""")
st.dataframe(tips.head(10))

st.write("""
Total Bill Histogram
""")
fig, ax = plt.subplots()
sns.histplot(data=tips, x='total_bill')
st.pyplot(fig)

st.write("""
Scatterplot - coherence between total_bill and tips
""")
fig, ax = plt.subplots()
sns.scatterplot(data=tips, x='total_bill', y='tip')
st.pyplot(fig)

st.write("""
Scatterplot - coherence between total_bill and tips and size
""")
fix, ax = plt.subplots()
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="size", size="size")
st.pyplot(fix)

st.write("""
Scatterplot - coherence between day and size of bill
""")
fig, ax = plt.subplots()
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="day")
st.pyplot(fig)

st.write("""
Scatterplot - coherence between day - y and tip - x, color - sex
""")
fig, ax = plt.subplots()
sns.scatterplot(data=tips, x="day", y="tip", hue="sex")
st.pyplot(fig)

st.write("""
Boxplot with the sum of all bills for each day, broken down by time (Dinner/Lunch)
""")
fig, ax = plt.subplots()
sns.boxplot(data=tips, x='day', y='total_bill', hue='time')
st.pyplot(fig)

st.write("""
Hists for lunch and dinner by tips
""")
fig, ax = plt.subplots(1, 2, figsize=(12, 6))
ax[0] = sns.histplot(data=tips[tips['time'] == 'Lunch'], x='tip', ax=ax[0])
ax[0].set_xlabel('Tip')
ax[0].set_ylabel('Frequency')
ax[0].set_title('Histogram of Tips (Lunch Time)')
ax[1] = sns.histplot(data=tips[tips['time'] == 'Dinner'], x='tip', ax=ax[1])
ax[1].set_xlabel('Tip')
ax[1].set_ylabel('Frequency')
ax[1].set_title('Histogram of Tips (Dinner Time)')
st.pyplot(fig)

st.write("""
2 scatterplots (for men and women), showing the relationship between bill size and tips, further broken down by smokers/non-smokers. Arrange them horizontally.
""")
fig, ax = plt.subplots(1, 2)
sns.scatterplot(data=tips[tips['sex'] == 'Male'], x='total_bill', y='tip', hue='smoker', ax=ax[0])
sns.scatterplot(data=tips[tips['sex'] == 'Female'], x='total_bill', y='tip', hue='smoker', ax=ax[1])
ax[0].set_title('Scatterplot for Men')
ax[1].set_title('Scatterplot for Women')
st.pyplot(fig)