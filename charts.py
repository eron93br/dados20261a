import numpy as np
import streamlit as st
import seaborn as sns
import plotly.express as px
from utils import IMG_CESAR
import matplotlib.pyplot as plt
from numpy.random import default_rng as rng

arr = rng(0).normal(1, 1, size=100)
fig3, ax = plt.subplots()
ax.hist(arr, bins=20)



def rotina_plot_dispersao_titanic(df, x1, x2):
    # Passo 1 - Operação de filtrar por idade
    df = df[(df['age'] > x1) & (df['age'] < x2)]

    # Passo 2 - Criar o gráfico de dispersão da idade por preço da passagem
    fig1 = px.scatter(x=df['fare'], y=df['age'], title="Gráfico de Correlação - Titanic Dataset",
                 labels={'x': 'Preço da passagem', 'y': 'Idade'})

    # passo 3 - atualizar estilização
    fig1.update_traces(marker=dict(
        size=10,
        color="#91bd3a",  # cor do marcador
        symbol="square",  # formato do scatter plot
        line=dict(width=2)  # largura do contorno
    ))

    # retorna a figura
    return fig1

