# -*- python3/ utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException
import json
import getpass


def init_driver():
    """ Инициируется браузер через Selenium """
    chromedriver = ('geckodriver.exe')  # путь к драйверу хром

    ''' Если требуется запуск бе UI, то нужно раскомментировать "headless" '''
    options = webdriver.FirefoxOptions()
    options.add_argument('headless')  # для открытия headless-браузера
    driver = webdriver.Firefox(executable_path=chromedriver, firefox_options=options)
    return driver


def login_gos():
    ''' Вход пользователя, данные вводятся логин и пароль вводятся после запуска'''
    driver.get('https://esia.gosuslugi.ru/')
    time.sleep(1.5)
    try:
        driver.find_element(By.ID, "mobileOrEmail").send_keys(login)
        time.sleep(1.5)
        driver.find_element(By.ID, "password").send_keys(my_password)
        time.sleep(1.5)
        driver.find_element(By.CSS_SELECTOR, "button").click()
        time.sleep(1.5)
    except TimeoutException:
        print('Time Out')


def get_data():
    ''' Получаем страницу пользователя'''
    time.sleep(1.5)
    driver.get(
        'view-source:https://esia.gosuslugi.ru/profile/rs/prns/?embed=(documents.elements,addresses.elements,vehicles.elements,kids.elements)')

    ''' Разбираем страницу и получаем словарь, заключённый в теги, в формате Json '''
    required_html = driver.page_source
    soup = BeautifulSoup(required_html, 'lxml')
    res_js = soup.pre.text

    ''' Декодируем '''
    result = json.loads(res_js)

    ''' Выводим на печать в консоль '''
    print(type(result))
    for key, value in result.items():
        print("{0}: {1}".format(key, value))

    ''' Выводим на печать в файл '''
    with open('out.txt', 'w') as out:
      for key, val in result.items():
        out.write('{}:{}\n'.format(key, val))


if __name__ == '__main__':
    login = input('Please, enter phone or email: ').split()
    my_password = getpass.getpass('Please, enter password: ').split()
    driver = init_driver()
    login_gos()
    get_data()
    driver.quit()
