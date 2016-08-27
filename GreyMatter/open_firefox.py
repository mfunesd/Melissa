from selenium import webdriver
from SenseCells.tts import tts

def open_firefox():
    #tts('Aye aye captain, opening Firefox')
    tts('De acuerdo capitan, abriendo Firefox')
    webdriver.Firefox()
