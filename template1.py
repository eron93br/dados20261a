import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px


# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# CSS — apenas para dar aparência de dashboard
# ============================================================

st.markdown(
    """
    <style>
        /* Fundo principal */
        .stApp {
            background-color: #f7f7f7;
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #fff7c7;
        }

        /* Cards */
        .metric-card {
            background-color: white;
            border: 1px solid #dddddd;
            border-radius: 14px;
            padding: 20px;
            min-height: 120px;
        }

        .metric-title {
            font-size: 15px;
            color: #555555;
        }

        .metric-value {
            font-size: 32px;
            font-weight: 700;
            margin-top: 5px;
        }

        .metric-positive {
            color: #25a244;
            font-size: 13px;
            margin-top: 8px;
        }

        /* Containers de visualização */
        .figure-container {
            background-color: white;
            border: 1px solid #dddddd;
            border-radius: 12px;
            padding: 15px;
        }

        /* Footer */
        .footer {
            text-align: center;
            color: #555555;
            padding: 20px;
            font-size: 14px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    # Mock de logo
    st.markdown(
        """
        <div style="
            height:130px;
            border:4px solid #6c89c9;
            border-radius:50%;
            background:#dce6fa;
            display:flex;
            align-items:center;
            justify-content:center;
            margin:10px 10px 40px 10px;
        ">
            <strong>LOGO</strong>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.button("Visão Geral", use_container_width=True)
    st.button("Análises", use_container_width=True)
    st.button("Configurações", use_container_width=True)


# ============================================================
# ÁREA PRINCIPAL
# ============================================================

# ------------------------------------------------------------
# 1. CARDS SUPERIORES
# ------------------------------------------------------------

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-title">Métrica 1</div>
            <div class="metric-value">1.234</div>
            <div class="metric-positive">↑ 12,5% vs período anterior</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c2:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-title">Métrica 2</div>
            <div class="metric-value">5.678</div>
            <div class="metric-positive">↑ 8,2% vs período anterior</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c3:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-title">Métrica 3</div>
            <div class="metric-value">9.101</div>
            <div class="metric-positive">↑ 15,3% vs período anterior</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


st.write("")


# ============================================================
# 2. FIG1 + FIG2
# ============================================================

fig1_col, fig2_col = st.columns(2)


# Dados mock
df = pd.DataFrame(
    {
        "Categoria": ["A", "B", "C", "D", "E"],
        "Valor": [20, 35, 28, 50, 42],
    }
)

fig1 = px.bar(
    df,
    x="Categoria",
    y="Valor",
    title="FIG1 - Título da Visualização",
)

fig1.update_layout(
    margin=dict(l=20, r=20, t=60, b=20),
    height=350,
)


df2 = pd.DataFrame(
    {
        "Categoria": ["A", "B", "C", "D", "E"],
        "Valor": [15, 25, 45, 30, 55],
    }
)

fig2 = px.line(
    df2,
    x="Categoria",
    y="Valor",
    markers=True,
    title="FIG2 - Título da Visualização",
)

fig2.update_layout(
    margin=dict(l=20, r=20, t=60, b=20),
    height=350,
)


with fig1_col:
    st.markdown('<div class="figure-container">', unsafe_allow_html=True)
    st.plotly_chart(fig1, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)


with fig2_col:
    st.markdown('<div class="figure-container">', unsafe_allow_html=True)
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# 3. FIG3 — LARGURA TOTAL
# ============================================================

st.write("")

fig3_data = pd.DataFrame(
    {
        "Período": np.arange(1, 21),
        "Valor": np.random.randn(20).cumsum(),
    }
)

fig3 = px.area(
    fig3_data,
    x="Período",
    y="Valor",
    title="FIG3 - Título da Visualização",
)

fig3.update_layout(
    margin=dict(l=20, r=20, t=60, b=20),
    height=400,
)

st.markdown('<div class="figure-container">', unsafe_allow_html=True)
st.plotly_chart(fig3, use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        Desenvolvido por fulano de tal
    </div>
    """,
    unsafe_allow_html=True,
)
