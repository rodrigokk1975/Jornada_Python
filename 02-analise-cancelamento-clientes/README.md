[← Voltar para todos os projetos](../README.md)

# 📊 Análise de Cancelamento de Clientes com Python

Projeto desenvolvido durante o curso "Jornada Python" da "Hashtag Programacao", na área de **Análise de Dados**.

## 🎯 Contexto do problema

Uma empresa com mais de 800 mil clientes percebeu que a maior parte da sua base é composta por clientes inativos, ou seja, que já cancelaram o serviço. O objetivo deste projeto é **identificar os principais motivos dos cancelamentos** e **propor ações eficientes para reduzir esse número**.

## 🔍 O que foi feito

1. **Importação da base** de dados (`cancelamentos.csv`) com Pandas
2. **Tratamento dos dados**: remoção da coluna `CustomerID` (sem valor analítico) e exclusão de linhas com valores vazios (50.000 → 49.996 registros)
3. **Análise inicial dos cancelamentos**: quantidade e percentual de clientes que cancelaram
4. **Análise das causas**: criação de histogramas interativos com Plotly para cada coluna da base, separando clientes que cancelaram dos que não cancelaram
5. **Simulação de ações corretivas** e medição do impacto na taxa de cancelamento

## 📈 Principais resultados

**Situação inicial:** 56,8% dos clientes cancelaram (28.393 de 49.996).

**Causas identificadas nos gráficos:**

| Padrão encontrado | Ação sugerida |
|---|---|
| Todos os clientes com contrato **mensal** cancelam | Oferecer descontos nos planos **anuais** e **trimestrais** |
| Clientes que ligam **mais de 4 vezes** para o call center cancelam | Criar um processo para resolver o problema do cliente em **no máximo 3 ligações** |
| Clientes com **mais de 20 dias de atraso** cancelam | Política para resolver atrasos em **até 10 dias** (equipe financeira) |

**Impacto simulado:** ao filtrar a base aplicando essas três regras (ou seja, simulando um cenário em que esses problemas fossem resolvidos), a taxa de cancelamento cai de **56,8% para 18,4%**.

## 🛠️ Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/): leitura, limpeza e análise dos dados
- [Plotly Express](https://plotly.com/python/plotly-express/): visualização interativa
- [Jupyter Notebook](https://jupyter.org/)

## ⚙️ Como executar

1. Clone o repositório e entre na pasta do projeto:
```bash
   git clone https://github.com/rodrigokk1975/Jornada_Python.git
   cd Jornada_Python/02-analise-cancelamento-clientes
```

2. Instale as dependências:
```bash
   pip install pandas plotly jupyter
```

3. A base `cancelamentos.csv` já está incluída na pasta. A base original também pode ser baixada [neste link](https://drive.google.com/drive/folders/1uDesZePdkhiraJmiyeZ-w5tfc8XsNYFZ?usp=drive_link).

4. Abra e execute o notebook:
```bash
   jupyter notebook analise.ipynb
```

## 📁 Estrutura do projeto

```
├── analise.ipynb        # Notebook com toda a análise
├── cancelamentos.csv    # Base de dados de clientes
└── README.md            # Documentação do projeto
```

## 📚 Aprendizados

- Importação e limpeza de dados com Pandas
- Tratamento de valores vazios (`dropna`)
- Análise exploratória com `value_counts` e histogramas
- Visualização interativa de dados com Plotly
- Transformar dados em **recomendações de negócio**
