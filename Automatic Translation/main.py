import requests as requests
from selenium import webdriver
from tkinter.filedialog import askopenfilename
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import urllib
import tkinter as tk
import tkinter.filedialog as fd
import time
import os
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_experimental_option("excludeSwitches", ["enable-logging"])
root = tk.Tk()
root.withdraw()
filename = askopenfilename(title="Choose ChromeDriver", filetypes=[("Google Driver", ".exe")])
print("[🙀] Chemin du Driver Google : " + filename)
ImagessPATH = fd.askopenfilenames(parent=root, title='Séléctionner les photos', filetypes=[("Image Files", ".png .jfif, .jpg, .jpeg")])
print("[🤯] Importation des images réussi ! ")
folder_name = input("[❓] : Quelle est le nom du fichier dans lequel sauvegardé ? : ")

server = Service(executable_path=filename)
driver = webdriver.Chrome(service=server, options=options)
driver.get("https://touhou.ai/imgtrans/")
driver.maximize_window()

select = Select(driver.find_element(By.ID, "target-language"))
select.select_by_visible_text("français")

if not os.path.isdir(folder_name):
    os.makedirs(folder_name)

print("[⌛] Temps prévu : " + str((len(ImagessPATH) * 30) / 60 ) + " minutes.")
number = 0
for i in range(0, len(ImagessPATH)):
    number += 1
    driver.find_element(By.XPATH, '//*[@id="image-file"]').send_keys(ImagessPATH[i])
    driver.find_element(By.XPATH, '//*[@id="submit-button"]').click()
    print("")
    print("[🔧] Téléchargement de l'image " + str(number) + " ...")
    time.sleep(30)
    print("[🚀] Téléchargement de l'image " + str(number) + " terminé !")
    TranslatedImage = driver.find_element(By.ID, ("translated-image"))
    src = TranslatedImage.get_attribute('src')
    response = requests.get(src)
    TranslateName = str(folder_name) + "/imgTranslated" + str(number) + ".png"
    file = open(TranslateName, "wb")
    file.write(response.content)
    file.close()