from tkinter import font
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

#Load File
data = pd.read_csv('d:/pythondata/Mall_customers.csv')

#Line Plot
sns.set_style('darkgrid')
plt.subplot(311)
sns.lineplot(x='Age',y='Annual Income (k$)',data=data)
plt.title(" This is Seaborn for you ")

sns.set_style('whitegrid')
plt.subplot(312)
sns.lineplot(x='Age',y='Spending Score (1-100)',data=data)
sns.set_context(context='paper',font_scale=1)

palette = sns.color_palette()
sns.palplot(palette)
plt.show()

