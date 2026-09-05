# Dashboard da Turma 2026.1

Códigos da disciplina **Análise e Visualização de Dados — 2026.1**.

Dashboard construído com [Streamlit](https://streamlit.io) sobre o dataset **Titanic** (carregado direto do `seaborn`), com gráficos em Plotly e Matplotlib.

---

## Estrutura do projeto

```
dados20261a/
├── app.py                # aplicação principal do Streamlit
├── charts.py             # funções e figuras dos gráficos (Plotly + Matplotlib)
├── utils.py              # constantes auxiliares (ex.: IMG_CESAR)
├── template1.py          # template de apoio das aulas
├── template2.py          # template de apoio das aulas
├── prompt_conversao.md   # anotações/prompt de conversão
├── requirements.txt      # dependências
└── assets/               # imagens e recursos estáticos
```

---

## Pré-requisitos

- **Python 3.9 ou superior** (`python --version` para conferir)
- `pip` e, de preferência, um ambiente virtual

---

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/eron93br/dados20261a.git
cd dados20261a
```

### 2. Crie e ative um ambiente virtual

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell)**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Instale as dependências

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Dependências do projeto: `pandas`, `numpy`, `seaborn`, `streamlit`, `plotly`, `plotly-express`.
O `matplotlib` é usado em `charts.py` e vem junto como dependência do `seaborn`. Se por algum motivo faltar:

```bash
pip install matplotlib
```

---

## Como rodar

Com o ambiente virtual ativo, na raiz do projeto:

```bash
streamlit run app.py
```

O terminal vai exibir algo como:

```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.0.10:8501
```

O navegador abre sozinho. Se não abrir, acesse **http://localhost:8501** manualmente.

Para encerrar, use `Ctrl + C` no terminal.

### Opções úteis

```bash
# rodar em outra porta
streamlit run app.py --server.port 8502

# não abrir o navegador automaticamente
streamlit run app.py --server.headless true

# expor na rede local (para o pessoal da turma acessar)
streamlit run app.py --server.address 0.0.0.0
```

### Rodando os templates das aulas

```bash
streamlit run template1.py
streamlit run template2.py
```

---

## O que o dashboard faz

- **Sidebar** com `selectbox` e `radio` de exemplo
- **Upload de CSV** via `st.file_uploader`, exibido em `st.dataframe`
- **Slider de intervalo de idade** (`st.select_slider`) que filtra o dataset Titanic
- **Gráfico de dispersão** idade × preço da passagem (Plotly, em `charts.py`)
- **Heatmap de correlação** entre `survived`, `pclass`, `sibsp`, `parch` e `fare`
- **Editor de Markdown** ao vivo com `st.text_area` + `st.markdown`
- **Histograma** em Matplotlib renderizado com `st.pyplot`

O app faz *hot reload*: ao salvar qualquer arquivo `.py`, o Streamlit oferece recarregar a página. Ative **"Always rerun"** no menu do canto superior direito para atualizar automaticamente.

---

## Problemas comuns

**`StreamlitAPIException: set_page_config() can only be called once...`**
`st.set_page_config()` precisa ser o **primeiro** comando Streamlit do script, antes de qualquer `st.title()`, `st.write()` etc. Em `app.py`, mova a chamada para logo depois dos imports.

**`ModuleNotFoundError: No module named 'streamlit'`**
O ambiente virtual não está ativo ou as dependências não foram instaladas. Rode `source .venv/bin/activate` (ou o equivalente no Windows) e `pip install -r requirements.txt`.

**`Port 8501 is already in use`**
Já existe um Streamlit rodando. Feche-o ou use `--server.port 8502`.

**Erro ao carregar o dataset do Titanic**
`sns.load_dataset("titanic")` baixa os dados da internet na primeira execução. Verifique a conexão — depois disso fica em cache local.

**`command not found: streamlit`**
Use `python -m streamlit run app.py` como alternativa.

---

## Publicar no Streamlit Community Cloud

1. Faça push do projeto para o GitHub (com o `requirements.txt` na raiz)
2. Acesse [share.streamlit.io](https://share.streamlit.io) e entre com sua conta GitHub
3. Clique em **New app**, selecione o repositório `eron93br/dados20261a`, branch `main`
4. Em *Main file path*, informe `app.py`
5. Clique em **Deploy**

---

## Licença

Material didático de uso educacional da disciplina.
