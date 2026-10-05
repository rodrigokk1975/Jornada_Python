[← Voltar para todos os projetos](../README.md)

# 🤖 Automação de Cadastro de Produtos com Python

Projeto desenvolvido durante o curso "Jornada Python" da "Hashtag Programaçao".

O script automatiza o login em um sistema web e o cadastro em massa de produtos a partir de uma planilha CSV, simulando as ações de um usuário (cliques e digitação no teclado).

## 📋 O que o projeto faz

1. Abre o Google Chrome
2. Acessa a página de login do sistema
3. Preenche e-mail e senha e realiza o login
4. Fecha o aviso de alteração de senha
5. Lê a base de produtos do arquivo `produtos.csv`
6. Percorre cada linha da tabela e cadastra o produto no sistema, preenchendo os campos:
   - Código
   - Marca
   - Tipo
   - Categoria
   - Preço unitário
   - Custo
   - Observações (opcional)

## 🛠️ Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [PyAutoGUI](https://pyautogui.readthedocs.io/): automação de mouse e teclado
- [Pandas](https://pandas.pydata.org/): leitura e manipulação da base de dados

## ⚙️ Como executar

1. Clone o repositório e entre na pasta do projeto:
```bash
   git clone https://github.com/rodrigokk1975/Jornada_Python.git
   cd Jornada_Python/01-automacao-cadastro-produtos
```

2. Instale as dependências:
```bash
   pip install pyautogui pandas
```

3. O arquivo `produtos.csv` já está incluído na pasta.

4. No código, substitua `"sua senha"` pela sua senha de acesso (nesse caso o site nao tem senha por servir apenas para testes).

5. Execute o script:
```bash
   python main.py
```

> ⚠️ **Importante:** as posições de clique (`x` e `y`) foram definidas para a resolução da minha tela. Se a sua for diferente, use `pyautogui.position()` para descobrir as coordenadas corretas e ajuste no código.

> ⚠️ **Atenção:** durante a execução, não mexa no mouse nem no teclado, pois o script controla ambos. Para interromper em caso de emergência, mova o mouse para o canto superior esquerdo da tela (fail-safe do PyAutoGUI).

## 📁 Estrutura do projeto

```
├── main.py         # Código da automação
├── produtos.csv    # Base de produtos a serem cadastrados
└── README.md       # Documentação do projeto
```

## 📚 Aprendizados

- Automação de tarefas repetitivas com PyAutoGUI
- Leitura de arquivos CSV com Pandas
- Uso de laços `for` para percorrer tabelas
- Tratamento de valores vazios com `pd.isna()`
