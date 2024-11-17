"""
This module performs data analysis on the Delhi Climate dataset from 2013 to 2017.
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use('Agg')

sns.set_theme(style="whitegrid")
plt.style.use("fivethirtyeight")

df = pd.read_csv('data_sets\\DailyDelhiClimateTrain.csv')

print(df.head())

print(f"Number of rows: {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}")

print(df.dtypes)

print(df.describe())

missing_values = df.isnull().sum()
print(missing_values)

numeric_columns = df.select_dtypes(include=[np.number]).columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

meantemp_std = df['meantemp'].std()
print(f"Desvio padrão da coluna 'meantemp': {meantemp_std}")

df.hist(bins=30, figsize=(15, 10))
plt.suptitle("Distribuição das Variáveis")
plt.savefig('histogram.png') 

plt.figure(figsize=(10, 6))

correlation_matrix = df.drop(columns=['date']).corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Mapa de Calor das Correlações")
plt.savefig('heatmap.png') 

plt.figure(figsize=(15, 10))
for i, column in enumerate(df.select_dtypes(include=[np.number]).columns, 1):
    plt.subplot(2, 2, i)
    sns.boxplot(df[column])
    plt.title(f"Boxplot de {column}")
plt.tight_layout()
plt.savefig('boxplots.png') 
