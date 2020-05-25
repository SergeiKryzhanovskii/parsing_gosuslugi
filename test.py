import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import html5lib
import json




# путь к драйверу хром
chromedriver = ('chromedriver.exe')
options = webdriver.ChromeOptions()
# запуск в хроме
driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
# переход на страницу входа
driver.get('https://esia.gosuslugi.ru/')
time.sleep(1.5)
# учетка
phone = ''
my_password = ''
# поиск тегов по имени, ввод
driver.find_element(By.ID, "mobileOrEmail").send_keys(phone)
time.sleep(1.5)
driver.find_element(By.ID, "password").send_keys(my_password)
time.sleep(1.5)
# вход
driver.find_element(By.CSS_SELECTOR, "button").click()
# переход на страницу с данными в обход предполагаемых сообщений
driver.get('https://esia.gosuslugi.ru/profile/user/personal')
driver.get('https://esia.gosuslugi.ru/profile/rs/prns/?embed=(documents.elements,addresses.elements,vehicles.elements,kids.elements)')
# получаем страницу
required_html = driver.page_source

# передаем в конструктор BS
soup = BeautifulSoup(required_html, 'lxml')
res = soup.pre.text
print(res)
r = json.loads(res)
print(type(r))
for key, value in r.items():
  print("{0}: {1}".format(key, value))

# парсим сайт


# закрыть окно


# press button
# driver.find_element(By.CSS_SELECTOR, "button").click()
# поиск элемента
# elements = driver.find_elements(By.TAG_NAME, 'p')

# добавить выход из аккаунта
# создать файл, если его еще нет и внести данные
