import pyautogui
import time

# Aguarde alguns segundos
time.sleep(5)


pyautogui.press('win')
pyautogui.write('bloco de notas')
pyautogui.press('enter')

# Aguarde alguns segundos 
time.sleep(2)


mensagem = "Olá, essa é uma automação em Python :)"
pyautogui.write(mensagem)

# Salve o arquivo (opcional)
pyautogui.hotkey('ctrl', 's')
time.sleep(1)
pyautogui.write('automacao.txt')
pyautogui.press('enter')


pyautogui.hotkey('alt', 'f4')
