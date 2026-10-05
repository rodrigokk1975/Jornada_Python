import pyautogui
import time

pyautogui.PAUSE = 0.3
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)

# entrar no link 
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)

# selecionar o campo de email
pyautogui.click(x=779, y=370)
# escrever o seu email
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("sua senha")
pyautogui.click(x=950, y=539)
pyautogui.click(x=950, y=539) # clique no botao de login
time.sleep(3)

pyautogui.click(x=1122, y=363)#fecha o aviso de mudar a senha

# importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv")

# cadastrar produtos
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=827, y=257)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)