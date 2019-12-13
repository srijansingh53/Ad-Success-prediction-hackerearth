import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dataset/Train.csv', encoding='latin-1')

df.head()

sns.countplot(df.netgain)
plt.xlabel('Gain?')
plt.ylabel('Number of user ratings')

sns.scatterplot(x="average_runtime(minutes_per_week)", y="ratings", hue = 'Pclass', data=df)
