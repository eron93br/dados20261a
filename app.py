# 06 etapas para construir dashboards com streamlit
import numpy as np
import streamlit as st
import seaborn as sns
import plotly.express as px
from utils import IMG_CESAR
from charts import fig1, fig3

# ------------- Carregar Dataset do Titanic ------------- 
df = sns.load_dataset("titanic")

st.title("Primeiro Dashboard")


# Seção #1 ------------------------------------------------------------------------------
st.header("Seção #1")

st.dataframe(df)

st.plotly_chart(fig1)

# Atualizar os marcadores
fig1.update_traces(marker=dict(
    size=10,
    color="#91bd3a",  # cor do marcador
    symbol="square",  # formato do scatter plot
    line=dict(width=2)  # largura do contorno
))

# Calcula matriz de correlação
titn = df.filter(['survived', 'pclass', 'sibsp', 'parch', 'fare'])
corr_matrix = titn.corr()

# Criar o gráfico de heatmap usando Plotly Express
fig2 = px.imshow(corr_matrix, x=corr_matrix.columns, y=corr_matrix.columns, color_continuous_scale='greens', text_auto=True) # se tirarmos text_auto, fica sem o número

# configura o título do gráfico
fig2.update_layout(title_text="Gráfico de Correlação - Titanic Dataset")

st.plotly_chart(fig2)

# Seção #3 ------------------------------------------------------------------------------
st.header("Seção #3")

md = st.text_area('Type in your markdown string (without outer quotes)',
                  "Happy Streamlit-ing! :balloon:")

st.code(f"""
import streamlit as st

st.markdown('''{md}''')
""")

st.markdown(md)

st.image(IMG_CESAR)

st.header("Seção #4 , nova!")

st.pyplot(fig3)