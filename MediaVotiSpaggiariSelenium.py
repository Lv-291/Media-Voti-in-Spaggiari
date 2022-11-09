import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


#INSERIRE ALL INTERNO DELLE VIRGOLETTE LE TUE CREDENZIALI DI SPAGGIARI  
Username = ""
Password = ""

#questa parte serve ad aprire chrome e il sito di classeviva
LINK = "https://web.spaggiari.eu/home/app/default/login.php"

chrome_driver = ChromeDriverManager().install()
driver = Chrome(service=Service(chrome_driver))
driver.get(LINK)

#vengono inserite le credenziali
sleep(1)
driver.find_element(By.ID, "login").send_keys(Username)
driver.find_element(By.ID, "password").send_keys(Password)
sleep(1)
driver.find_element(By.XPATH, "//*[@id=\"fform\"]/button").click()
sleep(1)
driver.find_element(By.XPATH, "//*[@id=\"data_table\"]/tbody/tr[13]/td[3]/a/p[1]").click()
sleep(1)
driver.find_element(By.XPATH, "//*[@id=\"data_table\"]/tbody/tr[7]/td[5]/a/button").click()
sleep(1)

#vengono raccolti i voti e messi in un vettore
y = []
summ = 0
for i in range(200):
    try:
        x = list("//*[@id=\"data_table\"]/tbody/tr[9]/td[3]/div[1]/p")
        x[31] = str(i + 9)
        x = "".join(x)
        y.append(driver.find_element(By.XPATH, x).text)
    except:
        pass


#viene calcolata la media di tutti i voti, i voti con il +, - o ½ vengono trasfomati in float 
for i in range(len(y)):
    x = list(y[i])
    if len(x) == 2:
        if x[1] == '½':
            x.remove('½')
            x[0] = int(x[0]) + 0.5

        elif x[1] == '-':
            x.remove('-')
            x[0] = int(x[0]) - 0.25

        elif x[1] == '+':
            x.remove('+')
            x[0] = int(x[0]) + 0.25
        elif x[1] == "0":
            x[0] = int(x[0] + x[1])
            x.remove("0")

        summ += x[0]
    else:
        summ += int(x[0])

#viene stampata la media 
print("Media totale:",summ / len(y))

#chiude la finestra 
driver.close()
