from selenium import webdriver
from getpass import getpass

import time

useremail = input("Enter your email: ")
password = input("Enter your password: ")
# usermicrosoft = input("Enter your microsoft email: ")

driver = webdriver.Chrome("C:\\Dev\Webdrivers\\chromedriver.exe")
driver.get("https://login.tailscale.com/login?next_url=/admin/authkeys")

useremail_textbox = driver.find_element_by_id("user")
useremail_textbox.send_keys(useremail)

time.sleep(0.5)

nextbtn = driver.find_element_by_name("submitbtn")
nextbtn.click()


# usermicrosoft_textbox = driver.find_element_by_id(
#     "i0116.form-control.ltr_override.input.ext-input.text-box.ext-text-box")
# usermicrosoft_textbox.send_keys(usermicrosoft)

# nextbtn = driver.find_element_by_id(
#     "idSIButton9.button.ext-button.primary.ext-primary")
# nextbtn.submit()
time.sleep(3)

password_textbox = driver.find_element_by_id("i0118")
password_textbox.send_keys(password)

signinbtn = driver.find_element_by_id("idSIButton9")
signinbtn.submit()
# # +

# driver.get("https://login.tailscale.com/admin/machines")
