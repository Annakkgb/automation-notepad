import pyautogui
import time

# Aguarde alguns segundos antes de começar :)
time.sleep(5)

# Abra o programa (Bloco de Notas do Windows)
pyautogui.press('win')
pyautogui.write('bloco de notas')
pyautogui.press('enter')

# Aguarde alguns segundos para o Bloco de Notas abrir
time.sleep(2)

# Digite uma mensagem no Bloco de Notas
mensagem = "Olá, essa é uma automação em Python :)"
pyautogui.write(mensagem)

# Salve o arquivo (opcional)
pyautogui.hotkey('ctrl', 's')
time.sleep(1)
pyautogui.write('automacao.txt')
pyautogui.press('enter')

# Feche o Bloco de Notas
pyautogui.hotkey('alt', 'f4')
