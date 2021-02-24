from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import time

def document_initialised(driver):
    return driver.execute_script("return initialised")

useremail = input("Enter your email: ")
password = input("Enter your password: ")

driver = webdriver.Chrome("C:\\Dev\Webdrivers\\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=ffbad51a-97b4-452b-adba-e68c06bcc206&login_hint=&prompt=login&redirect_uri=https%3A%2F%2Flogin.tailscale.com%2Fa%2Foauth_response&response_type=code&scope=User.Read&state=tc-130cf4ba6e89db")

#Populate username field
useremail_textbox = driver.find_element_by_name("loginfmt")
useremail_textbox.send_keys(useremail)

driver.implicitly_wait(5)

#Submit to next page
nextbtn = driver.find_element_by_id("idSIButton9")
nextbtn.click()
driver.implicitly_wait(5)
# WebDriverWait(driver).until(document_initialised)

password_textbox = driver.find_element_by_id("i0118")
password_textbox.send_keys(password)


signinbtn = driver.find_element_by_id("idSIButton9")
driver.implicitly_wait(5)
signinbtn.click()
driver.implicitly_wait(5)

staysignin = driver.find_element_by_id("idSIButton9")
driver.implicitly_wait(10)
signinbtn.click()