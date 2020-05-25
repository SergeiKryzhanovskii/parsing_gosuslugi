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
required_html = driver.get('https://esia.gosuslugi.ru/profile/rs/prns/?embed=(documents.elements,addresses.elements,vehicles.elements,kids.elements)')
# получаем страницу
#required_html = driver.page_source
# передаем в конструктор BS
soup = BeautifulSoup(required_html.text, 'html.parser')

parameters_list = soup.find('div', {'class': 'col span_3 push_1 dt'})
parameters_list_items = parameters_list.find_all()
for parameters in parameters_list_items:
    print(parameters.prettify())



# first = soup.find_all('div', {'class': 'col span_3 push_1 dt'})
# second = soup.find_all('div', {'class': 'col span_6 dd'})


# парсим сайт





# закрыть окно



# press button
#driver.find_element(By.CSS_SELECTOR, "button").click()
# поиск элемента
#elements = driver.find_elements(By.TAG_NAME, 'p')

# добавить выход из аккаунта
# создать файл, если его еще нет и внести данные
