import os
import time
from extract import *
import random
import webbrowser
import pyautogui
import pyperclip
def sleepy(*_,**__):#sleep for 2second+param and few millisecond
    return time.sleep(2+sum(_)+random.uniform(0,1))

webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://www.ebay.fr/sl/vendre?sr=wnstart")
sleepy()
sleepy()

nbproduit=len(product)
print("je vais déposer "+str(nbproduit)+" produit")
Announcenumber=5
trace=Announcenumber
def MyDescription(annonce):
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press('del')
    pyautogui.typewrite('Bonjour,')
    pyautogui.typewrite('\n')
    pyperclip.copy('Je vend cet montre '+str(annonce['Marque'])+' à '+str(annonce['Prix'])+' elle est vendu '+str(annonce['prix officiel'])+' par la maison officiel (voir photos 2)')
    pyautogui.hotkey("ctrl", "v")
    pyautogui.typewrite('\n')
    pyperclip.copy('-La montre est biensûr authentique (N° de série+facture)')
    pyautogui.hotkey("ctrl", "v")
    pyautogui.typewrite('\n')
    pyperclip.copy('-Possibilités de livraison ou retrait en magasin')
    pyautogui.hotkey("ctrl", "v")
    pyautogui.typewrite('\n')
    pyperclip.copy('-voir la description de la montre ici '+annonce['ref'][:])
    pyautogui.hotkey("ctrl", "v")
    pyautogui.typewrite('\n')
    pyperclip.copy('-50 Autres montres disponible en cliquant sur mon profil Ebay')
    pyautogui.hotkey("ctrl", "v")
    pyautogui.typewrite('\n')
    pyperclip.copy('Sur ceux je vous souhaite une bonne début/fin de journée , salut')
    pyautogui.hotkey("ctrl", "v")
def CaracObjet(annonce):
    for i in range(9):
        pyautogui.press('tab')
    pyautogui.typewrite('\n')
    pyperclip.copy(annonce['Marque'])
    pyautogui.hotkey("ctrl", "v")
    pyautogui.typewrite('\n')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.typewrite('\n')
    pyperclip.copy('Montre bracelet')
    pyautogui.hotkey("ctrl", "v")
    pyautogui.typewrite('\n')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.typewrite('\n')
    pyperclip.copy("Adulte unisexe")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.typewrite('\n')
def deposephoto(annonce):
    choisir= pyautogui.locateOnScreen('img/addphoto.png')
    formx, formy = pyautogui.center(choisir)
    pyautogui.click(formx, formy)
    sleepy(-1)
    pyperclip.copy(str(annonce['Photos0']))
    pyautogui.hotkey("ctrl", "v")
    pyautogui.typewrite('\n')
    sleepy()
    for i in range(5):
        pyautogui.press('tab')
    pyautogui.typewrite('\n')
    sleepy()
    pyperclip.copy(annonce['Photos1'])
    pyautogui.hotkey("ctrl", "v")
    pyautogui.typewrite('\n')
def deposite():
    
    global Announcenumber
    annonce=chget(Announcenumber)
    #Type the title
    pyperclip.copy(annonce['Titre'])
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press('tab')
    pyautogui.typewrite('\n')
    sleepy()
    pyautogui.typewrite('\n')
    sleepy()
    #Type crée une annonce
    for i in range(5):
        pyautogui.press('tab')
    pyautogui.typewrite('\n')
    sleepy(-1)
    pyautogui.typewrite('\n')
    sleepy(3)

    #Type neuf avec étiquette
    CaracObjet(annonce)
    sleepy()
    #deposer photo
    for i in range(20):
        pyautogui.press("down")
    sleepy(-1)
    deposephoto(annonce)
    #modifier description
    modify= pyautogui.locateOnScreen('img/modify.png')
    formx, formy = pyautogui.center(modify)
    pyautogui.click(formx, formy)
    sleepy()
    for i in range(5):
        pyautogui.press('tab')
   
    MyDescription(annonce)
    #decoher enchère
    pyautogui.press('tab')
    pyautogui.typewrite(' ')
    sleepy(-1)
    pyautogui.typewrite(' ')
    sleepy(2)
    #type price
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyperclip.copy(str(annonce['Prix']))
    pyautogui.hotkey("ctrl", "v")
    sleepy()
    #type Livraison
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.typewrite('\n')
    sleepy(-1)
    pyautogui.press("down")
    sleepy(-1.5)
    pyautogui.press('tab')
    pyautogui.press("down")
    pyautogui.typewrite('\n')
    sleepy()
    jpaye= pyautogui.locateOnScreen('img/jpaye.png')
    formx, formy = pyautogui.center(jpaye)
    pyautogui.click(formx, formy)
    #PUSH
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.typewrite(' ')
    sleepy()
    for i in range(8):
        pyautogui.press('tab')
    pyautogui.typewrite('\n')
    Announcenumber=Announcenumber+1







if __name__=="__main__":
 
    while (nbproduit-trace)!=0:
        print(" je vais déposer le produit N°: "+str(Announcenumber+1))
        deposite()
        nbproduit=nbproduit-1
        sleepy(5)
        for i in range(15):
            pyautogui.press('tab')
        