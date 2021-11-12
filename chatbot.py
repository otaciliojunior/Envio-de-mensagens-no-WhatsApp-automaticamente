from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self):
        # enviar mensagem
        self.mensagem = " boa noite, essa é uma mensagem de teste "
        # nome do grupo 
        self.grupos = ["ESTAGIÁRIO"]
        # Parte 1 - mensagem que vai ser enviada 
        self.mensagem = "Hey, eu tenho novidades!"
        # Parte 2 - grupo que a mensagem vai ser enviada 
        self.grupos_ou_pessoas = ["ESTAGIÁRIO"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', chrome_options=options)
    def EnviarMensagens(self):
        self.driver.get('https://web.whatsapp.com')
        # tempo de 13 segundos para adicionar o codigo qr
        time.sleep(13)
        for grupo in self.grupos:
            # xpath do codigo html da pagina do sigaa 
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
        for grupo_ou_pessoa in self.grupos_ou_pessoas:
            campo_grupo = self.driver.find_element_by_xpath(
                f"//span[@title='{grupo_ou_pessoa}']")
            time.sleep(3)
            grupo.click()
            campo_grupo.click()
            # <div tabindex="-1" class="p3_M1">
            chat_box = self.driver.find_element_by_class_name('p3_M1')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)
bot = WhatsappBot()
bot.EnviarMensagens()
#<span dir="auto" title="ESTAGIÁRIO" class="_ccCW FqYAR i0jNr">ESTAGIÁRIO</span>


