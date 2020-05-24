import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import html5lib


# путь к драйверу хром
chromedriver = ('chromedriver.exe')
options = webdriver.ChromeOptions()
# запуск в хроме
driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
# pause
time.sleep(3)
# переход на страницу входа
driver.get('https://esia.gosuslugi.ru/')
time.sleep(3)
# учетка
phone = '89647289222'
my_password = 'EvRf1993:'
# поиск тегов по имени, ввод
driver.find_element(By.ID, "mobileOrEmail").send_keys(phone)
time.sleep(3)
driver.find_element(By.ID, "password").send_keys(my_password)
time.sleep(3)
# вход
driver.find_element(By.CSS_SELECTOR, "button").click()
# переход на страницу с данными в обход предполагаемых сообщений
driver.get('https://esia.gosuslugi.ru/profile/user/personal')
# получаем страницу
required_html = driver.page_source
# передаем в конструктор BS
soup = BeautifulSoup(required_html, 'html5lib')

result = []

first = soup.find('div', {'class': 'col span_3 push_1 dt'}).text
second = soup.find('div', {'class': 'col span_6 dd'}).text
print(first)
print(second)
# парсим сайт





# закрыть окно



# press button
driver.find_element(By.CSS_SELECTOR, "button").click()
# поиск элемента
elements = driver.find_elements(By.TAG_NAME, 'p')

# добавить выход из аккаунта
# создать файл, если его еще нет и внести данные