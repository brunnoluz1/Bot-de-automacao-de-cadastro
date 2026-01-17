# LÓGICA DA PROGRAMAÇÃO 

import pyautogui
import time
pyautogui.PAUSE = 0.5 # Pausa de segurança entre comandos

# Passo 1: Entrar no sistema da empresa
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" # Seu link aqui
pyautogui.press("Win")
pyautogui.write("Chrome")
pyautogui.press("enter")

pyautogui.write(link) 
pyautogui.press("enter")
time.sleep(3) # Tempo de espera para carregar a página


# Passo 2: Fazer **login**
email = "portifólio@gmail.com"
pyautogui.click(x=826, y=374) #clica no campo e-mail
pyautogui.write(email)
pyautogui.press("tab")
pyautogui.write("sua senha muito dificil dificilima")
pyautogui.press("enter")
time.sleep(5)

# Passo 3: Abrir a base de dados
import pandas 
import openpyxl

tabela = pandas.read_csv("produtos.csv")

# Passo 4: Cadastrar os produtos

for linha in tabela.index:
    # Código
    pyautogui.click(x=904, y=259)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # Marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")
    # Tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")
    # Categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    # Preço
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")
    # Custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    # OBS
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000) 

# Passo 5: Repetir o passo 4 até acabar a lista de produtos

