[← Voltar para todos os projetos](../README.md)

# 🛒 Sistema de Vendas com Dashboard usando Python e Streamlit

Projeto desenvolvido durante o curso **Python Impressionador (Intensivão de Python)** da **Hashtag Treinamentos**.

Aplicação web para **cadastrar vendas** e **acompanhar os resultados em um dashboard**. As vendas são salvas em um arquivo CSV e os gráficos são atualizados com os dados cadastrados.

## 📋 Funcionalidades

- **Formulário de cadastro** na barra lateral, com data, vendedor, produto, quantidade e valor
- **Gravação automática** da nova venda no arquivo `vendas.csv`
- **Tabela de vendas** cadastradas, exibida na tela
- **Dashboard** com:
  - Faturamento total (métrica)
  - Gráfico de barras: valor vendido por vendedor, separado por produto
  - Gráfico de pizza: participação de cada produto no faturamento

## 🛠️ Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [Streamlit](https://streamlit.io/): criação da interface web
- [Pandas](https://pandas.pydata.org/): leitura e gravação da base de vendas
- [Plotly Express](https://plotly.com/python/plotly-express/): gráficos interativos

## ⚙️ Como executar

1. Clone o repositório e entre na pasta do projeto:
   ```bash
   git clone https://github.com/seu-usuario/projetos-python-hashtag.git
   cd projetos-python-hashtag/04-sistema-vendas-streamlit
   ```

2. Instale as dependências:
   ```bash
   pip install streamlit pandas plotly
   ```

3. Confira se o arquivo `vendas.csv` está na mesma pasta do script, com as colunas:
   ```
   data,vendedor,produto,quantidade,valor
   ```

4. Execute a aplicação:
   ```bash
   streamlit run main.py
   ```

5. O navegador abrirá automaticamente em `http://localhost:8501`.

## 🧠 Como funciona

1. O `pandas` lê a base de vendas do arquivo `vendas.csv`
2. O usuário preenche o formulário na barra lateral e clica em **Cadastrar venda**
3. A nova venda é adicionada como uma linha na tabela e o CSV é salvo novamente
4. A tabela e os gráficos são recalculados e exibidos com os dados atualizados

## 📁 Estrutura do projeto

```
├── main.py         # Código da aplicação
├── vendas.csv      # Base de dados de vendas
└── README.md       # Documentação do projeto
```

## 📚 Aprendizados

- Criação de formulários e componentes de entrada no Streamlit (`selectbox`, `date_input`, `number_input`, `button`)
- Uso da barra lateral (`st.sidebar`) para organizar a interface
- Leitura e gravação de dados em CSV com Pandas
- Criação de métricas e gráficos interativos com Plotly (barras e pizza)
- Construção de um pequeno sistema completo: entrada de dados, armazenamento e dashboard

## 🚀 Próximos passos

- Formatar o faturamento no padrão brasileiro (R$ 1.234,50)
- Adicionar filtros por vendedor, produto e período
- Validar o formulário (impedir quantidade ou valor zerados)
- Trocar o CSV por um banco de dados (SQLite, por exemplo) para que os dados não se percam em um deploy na nuvem
