# -*- python3/ utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
import json
import getpass


def init_driver():
    """ Emulate the user's browser """
    firefoxdriver = ('geckodriver.exe')  # path for a geckodriver
    options = Options()
    #options.headless = True # headless (browser starts without a graphical interface)
    driver = webdriver.Firefox(executable_path=firefoxdriver, firefox_options=options)
    return driver


def login_gos():
    """ Log in """
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
    """ Get a user's page """
    time.sleep(1.5)
    driver.get(
        'view-source:https://esia.gosuslugi.ru/profile/rs/prns/?embed=(documents.elements,addresses.elements,'
        'vehicles.elements,kids.elements)')

    ''' Parsing '''
    required_html = driver.page_source
    soup = BeautifulSoup(required_html, 'lxml')
    res_js = soup.pre.text

    ''' Decode '''
    result = json.loads(res_js)

    '''  Output data to a command line '''
    print(type(result))
    for key, value in result.items():
        print("{0}: {1}".format(key, value))

    '''  Output data to a file '''
    with open('out.txt', 'w', encoding='utf-8') as out:
      for key, val in result.items():
        out.write('{}:{}\n'.format(key, val))


if __name__ == '__main__':
    login = input('Please, enter phone or email: ').split()
    #my_password = input('Please, enter password: ').split() # read README.md ('Command line & PyCharm')
    my_password = getpass.getpass('Please, enter password: ').split()
    driver = init_driver()
    login_gos()
    get_data()
    driver.quit()
