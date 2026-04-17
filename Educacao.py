import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

#Lendo a Base de Dados
Base_Dados = pd.read_csv('StudentsPerformance.csv')

#dimensão
Base_Dados.shape

#Head
Base_Dados.head()

#Campos Nulos
Nulos = Base_Dados.isnull()

plt.figure(figsize=(16,5))
plt.title('Analise campos nulos')
sns.heatmap(Nulos, cbar=False)

#Unicos
Base_Dados.nunique()

#Campos Duplicados
Base_Dados.duplicated().sum()

#Estatistica
Base_Dados.describe()

#Info
Base_Dados.info()

#Calculando a porcentagem dos campos
Base_Dados['gender'].value_counts(normalize=True)*100

Base_Dados['race/ethnicity'].value_counts(normalize=True)*100

Base_Dados['parental level of education'].value_counts(normalize=True)*100

Base_Dados['lunch'].value_counts(normalize=True)*100

Base_Dados['test preparation course'].value_counts(normalize=True)*100


#Criando Grafico das medias de cada prova
plt.figure(figsize=(16,5))
sns.boxplot ( data=Base_Dados, x='math score', y='gender')

plt.figure(figsize=(16,5))
sns.boxplot ( data=Base_Dados, x='reading score', y='gender')

plt.figure(figsize=(16,5))
sns.boxplot ( data=Base_Dados, x='writing score', y='gender')

sns.pairplot(Base_Dados, hue='race/ethnicity')

sns.boxplot(data=Base_Dados, x='math score', y='race/ethnicity')

sns.boxplot(data=Base_Dados, x='math score', y='parental level of education')

sns.boxplot(data=Base_Dados, x='math score', y='test preparation course')

sns.scatterplot(data=Base_Dados, x='math score', y='writing score')

plt.show();

Base_Dados.groupby( by=['gender']).describe()['math score'].reset_index()

Base_Dados.groupby( by=['parental level of education']).describe()['math score'].reset_index()

Base_Dados.groupby( by=['test preparation course']).describe()['math score'].reset_index()