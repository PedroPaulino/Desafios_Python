# Documentação: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_html.html

import pandas as pd

url = 'https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/'
dfs = pd.read_html(url)

print(type(dfs))
print(len(dfs))


df_bancos = dfs[0]

print(df_bancos.shape)
print(df_bancos.dtypes)

print("Bancos Fálidos desde 2000: ", df_bancos[:(len(df_bancos)-10):-1])
df_bancos.to_csv(r'G:\Meu Drive\001_Documentos_W10\Documentos\1_Faculdade\01_Anhanguera\004_Cursos Extracurriculares\01_Análise de Dados Com Python\03_Análise de Dados com Python\Unidade 1 Seção 1\bancos_falidos_dataframe.xlsx', index= False, header=True)