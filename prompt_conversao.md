Você é um especialista em **Python, Streamlit, visualização de dados e Plotly**.

Analise o código Python abaixo, que utiliza **Matplotlib e/ou Seaborn**, e converta suas visualizações para **Plotly Express (`plotly.express`)**, tendo como objetivo final utilizar os gráficos em um **dashboard desenvolvido com Streamlit**.

### Objetivo principal

Transformar os gráficos estáticos de Matplotlib/Seaborn em gráficos **interativos, limpos, responsivos e adequados para aplicações Streamlit**, mantendo a mesma finalidade analítica dos gráficos originais.

### Regras de conversão

1. Substitua visualizações de `matplotlib.pyplot` e `seaborn` por equivalentes em `plotly.express`.

2. Dê preferência a:

   ```python
   import plotly.express as px
   ```

   Utilize `plotly.graph_objects` somente quando não existir uma solução adequada com Plotly Express.

3. O código final deve ser adequado para **Streamlit**. Para exibir os gráficos, utilize:

   ```python
   st.plotly_chart(fig, use_container_width=True)
   ```

4. Preserve a intenção e a informação dos gráficos originais:

   * título;
   * rótulos dos eixos;
   * legendas;
   * categorias;
   * cores;
   * agrupamentos;
   * filtros;
   * escalas;
   * ordem das categorias;
   * informações estatísticas relevantes.

5. Faça a correspondência entre os parâmetros das bibliotecas:

   | Seaborn/Matplotlib | Plotly                  |
   | ------------------ | ----------------------- |
   | `hue`              | `color`                 |
   | `style`            | `symbol` ou `line_dash` |
   | `size`             | `size`                  |
   | `col`              | `facet_col`             |
   | `row`              | `facet_row`             |
   | `x`                | `x`                     |
   | `y`                | `y`                     |

6. Utilize as funções equivalentes do Plotly Express sempre que possível:

   * `sns.scatterplot` → `px.scatter`
   * `sns.lineplot` → `px.line`
   * `sns.barplot` → `px.bar`
   * `sns.histplot` → `px.histogram`
   * `sns.boxplot` → `px.box`
   * `sns.violinplot` → `px.violin`
   * `sns.stripplot` → `px.strip`
   * `sns.scatterplot` com tendência → `px.scatter(..., trendline=...)`
   * `sns.heatmap` → avaliar `px.imshow`
   * `plt.pie` → `px.pie`

7. Caso exista `subplot`, tente utilizar os recursos de facet do Plotly Express, como:

   ```python
   facet_row=
   facet_col=
   ```

   Só utilize `make_subplots` quando `plotly.express` não for suficiente.

8. Aproveite a interatividade nativa do Plotly:

   * hover;
   * zoom;
   * pan;
   * seleção;
   * legenda interativa;
   * filtros quando fizer sentido.

9. O gráfico deve ocupar adequadamente a largura disponível no Streamlit:

   ```python
   st.plotly_chart(fig, use_container_width=True)
   ```

10. Utilize `fig.update_layout()` apenas para ajustes realmente necessários, evitando configurações excessivamente complexas.

11. Prefira uma estética simples e profissional para dashboard:

* fundo limpo;
* títulos objetivos;
* legendas claras;
* boa utilização do espaço;
* sem elementos visuais desnecessários.

12. Não altere o DataFrame original sem necessidade.

13. Evite criar classes, funções ou abstrações desnecessárias. O código deve permanecer **simples, legível e didático**.

14. Remova os imports de Matplotlib e Seaborn que deixarem de ser necessários.

15. Se houver código específico de Matplotlib, como:

```python
plt.figure()
plt.subplots()
plt.xlabel()
plt.ylabel()
plt.title()
plt.legend()
plt.xticks()
plt.yticks()
plt.grid()
```

converta sua finalidade para os mecanismos equivalentes do Plotly.

16. Se houver configuração de cores do Seaborn, tente reproduzir a intenção visual utilizando os recursos de `color_discrete_sequence`, `color_discrete_map` ou equivalentes do Plotly.

17. Se houver `figsize`, não tente reproduzir literalmente o tamanho. Adapte o gráfico ao modelo responsivo do Streamlit.

18. Se houver histogramas, distribuições ou gráficos estatísticos, preserve a interpretação estatística original.

19. Não transforme automaticamente todo gráfico em `graph_objects`. **Plotly Express deve ser a primeira opção.**

### Arquitetura Streamlit

Sempre que fizer sentido, organize o código seguindo esta lógica:

```text
Carregamento dos dados
        ↓
Filtros / parâmetros do usuário
        ↓
Preparação dos dados
        ↓
Criação do gráfico com Plotly Express
        ↓
Configuração mínima do layout
        ↓
st.plotly_chart()
```

Caso existam filtros no código original, considere transformá-los em componentes interativos do Streamlit, como:

```python
st.selectbox()
st.multiselect()
st.slider()
st.checkbox()
st.radio()
```

Mas **não crie filtros que não sejam necessários para a finalidade do código original**.

### Entrega

Forneça a resposta nesta ordem:

#### 1. Código convertido

Entregue o código completo, pronto para ser executado em um aplicativo Streamlit.

#### 2. O que foi convertido

Explique brevemente as principais conversões realizadas.

#### 3. Equivalências

Apresente uma tabela:

| Original           | Plotly/Streamlit    |
| ------------------ | ------------------- |
| Matplotlib/Seaborn | Plotly Express      |
| `hue`              | `color`             |
| `plt.show()`       | `st.plotly_chart()` |
| etc.               | etc.                |

#### 4. Melhorias para dashboard

Liste brevemente melhorias que poderiam ser feitas posteriormente, sem implementá-las automaticamente.

### Código original

```python
# COLE O CÓDIGO MATPLOTLIB/SEABORN AQUI
```

### Resultado esperado

O resultado final deve ser **código Streamlit funcional**, utilizando **Plotly Express como biblioteca principal de visualização**, com gráficos interativos, responsivos e adequados para um dashboard moderno, sem adicionar complexidade desnecessária.

Gere um arquivo chamados graphs.py para ele ser anexado facilmente a um dashboard Streamlit.
