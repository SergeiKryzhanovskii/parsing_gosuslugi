# Сode for receiving user data from the [gosuslugi.ru](https://www.gosuslugi.ru/ "gosuslugi.ru")
### Main stack
- [Python](https://www.python.org/downloads/ "Python") v3.8.3;
- [Selenium](https://www.selenium.dev/downloads/ "Selenium") v3.141;
- [Webdrivers](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/ "Webdrivers") for Selenium:
	-  [Chromedriver ](https://chromedriver.storage.googleapis.com/index.html "Chromedriver ") v83.0.4103.39;
	- [Geckodriver for Firefox ](https://github.com/mozilla/geckodriver/releases "Geckodriver for Firefox ") v0.26.0;
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/ "beautifulsoup4") v4.9.1;
- json;
- Windows 10.

------------

### Task:
1. Emulate user browser;
2. Parse user data;
3. Output data to a file.

------------
### Result
1. Using Selenium to emulate browser and error handling;
2. Parse data:
	1.  Go to your personal account to download data;
	2. Go to web page with personal data (previously obtained through developer mode in browser);
	3. Parsim using beautifulsoup4;
	4. Decode with json.
3.  At the end of the program, the variable is assigned data in the Python dictionary format and `out.txt`.

------------

### Program feature
#### Headless for Chrome
In the repository, this option is commented out.
This means that the browser starts with a graphical interface.
To work in the background you need to uncomment this line:
```python
options.add_argument('headless')
```
#### Headless for Firefox
In the repository, this option is commented out.
This means that the browser starts with a graphical interface.
To work in the background you need to uncomment this line:
```python
options.headless = True
```

------------

### Command line & PyCharm
When you run the program in command line - it's Ok.
When you run the programm in PyCharm - she may stop at the password entry step. 
This is a feature of the library`getpass`.
To run in PyCharm you need to uncomment the line:
```python
my_password = input('Please, enter password: ').split()
```
and comment out the line:

```python
my_password = getpass.getpass('Please, enter password: ').split()
```

------------

### Warning
- A different version `chromedriver` and `geckodriver` of drivers may be required to emulate the browser (I attach links at the beginning).
- The version depends on the operating system and build of your browser.
- The repository comes with drivers for Windows 10.
- It is important to indicate the correct path in the program to the driver files.
