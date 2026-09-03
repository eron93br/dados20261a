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


random_x = np.random.randint(1,100,50)
random_y = np.random.randint(1,100,50)

fig1 = px.scatter(x=random_x, y=random_y, title="Meu Título",
                 labels={'x': 'Legenda do Eixo X', 'y': 'Legenda do Eixo Y'})
