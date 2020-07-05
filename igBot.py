from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random



class InstagramBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path="C:\geckodriver\geckodriver.exe")

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com')
        time.sleep(10)
        conect = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        conect.click()
        time.sleep(5)
        campo_email = driver.find_element_by_xpath("//input[@name='username']")
        campo_email.click()
        # campo_email.clear()
        campo_email.send_keys(self.username)
        campo_senha = driver.find_element_by_xpath("//input[@name='password']")
        campo_senha.click()
        # campo_senha.clear()
        campo_senha.send_keys(self.password)
        campo_senha.send_keys(Keys.RETURN)
        time.sleep(5)
        self.comenta_nas_fotos_com_a_hastag('***')

    @staticmethod
    def digite_como_uma_pessoa(frase,onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)

    def comenta_nas_fotos_com_a_hastag(self,hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/"+ hashtag +"/")
        time.sleep(3)

        for i in range(1,3):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(5)

        hrefs= driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in pic_hrefs if hashtag in href]
        print(hashtag +' fotos ' + str(len(pic_hrefs)))

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            try:
                #driver.find_element_by_xpath('//button[@class="dCJp8 afkep"]').click()
                comentarios = ["tudo bem","tudo bem","tudo bem","tudo bem","tudo bem"]
                driver.find_element_by_class_name('Ypffh').click()
                campo_comentario = driver.find_element_by_class_name('Ypffh')
                self.digite_como_uma_pessoa(random.choice(comentarios),campo_comentario)
                driver.find_element_by_xpath('//button[@class="dCJp8 afkep"]').click()
                time.sleep(3)
                driver.find_element_by_xpath("//button[contains(text(),'Publicar')]").click()
                time.sleep(5)
            except Exception as e:
                print(e)
                time.sleep(5)

loginRaffael = InstagramBot("****","*****")
loginRaffael.login()
