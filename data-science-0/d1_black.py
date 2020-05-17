# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Objetivo
# O objetivo deste desafio é extrair algumas informações quantitativas que nos ajudem a compreender a natureza dos dados à disposição e ganhar alguns insights sobre o data set.
# 
# Para isso, utilizaremos o data set Black Friday disponibilizado originalmente pela Analytics Vidhya e acessível publicamente através do Kaggle. O data set traz algumas variáveis relativas à transações comerciais realizadas durante a Black Friday em uma determinada loja de varejo. Cada observação é relativa a um determinado item comprado por um usuário e um usuário pode ter comprado mais de um item.

# %%
import pandas as pd 
import os


# %%
os.getcwd()


# %%
os.chdir('/home/lucas/codenation/data-science-0')


# %%
os.listdir()


# %%
df = pd.read_csv('black_friday.csv')


# %%
df.describe()


# %%
df.info()


# %%



# %%
df.isna().mean()
df.Age

# %%
df.Agex


# %%
import seaborn as sns


# %%
sns.countplot(df.Product_Category_1)


# %%
sns.countplot(df.Product_Category_2)

