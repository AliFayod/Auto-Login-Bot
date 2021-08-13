from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import os

###########################################################
import random

with open('Path For User.TXT') as openfileobject:
    for user in openfileobject:
        for i in range(4):
            number_txt = open("Path for Number.TXT", "r")
            m = number_txt.readlines()
            l = []
            for i in range(0, len(m) - 1):
                x = m[i]
                z = len(x)
                a = x[:z - 1]
                l.append(a)
            l.append(m[i + 1])
            number = random.choice(l)

            # enter the link to the website you want to automate login.
            browser = webdriver.Chrome(executable_path="chromedriver.exe")
            browser.get(('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmyaccount.google.com%2Fsigninoptions%2Ftwo-step-verification%2Fenroll&osid=1&rart=ANgoxceh8071YqOPaIMJ1nZqlIzaBo2Jl1xrU4PNeFTlJfZjqWyTj333Bqkv89jc0zI9GgSWDtdGbV_FWumqNKd7aWLnmRH5Jg&service=accountsettings&flowName=GlifWebSignIn&flowEntry=ServiceLogin'))
            # enter your login username
            username = user
            # enter your login password
            password = "Samo1995!"


            ###########################################################
            # enter the element for username input field
            element_for_username = '//*[@id="identifierId"]'
            # enter the element for password input field
            element_for_password = 'password'
            # enter the element for submit button
            element_for_submit = '//*[@id="identifierNext"]/div/button'
            element_for_submit_pass ='//*[@id="passwordNext"]/div/button'
            element_for_number ='//*[@id="yDmH0d"]/c-wiz/div/div[3]/c-wiz/div/div/div[3]/div[1]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/input'
            element_for_check_call ='//*[@id="yDmH0d"]/c-wiz/div/div[3]/c-wiz/div/div/div[3]/div[1]/div/div[1]/div/div[2]/div[2]/div[4]/div[2]/div/span/div/label[2]/div'
            element_for_check_submit ='//*[@id="yDmH0d"]/c-wiz/div/div[3]/c-wiz/div/div/div[3]/div[2]/div/div[3]/div[1]/span/span'
            ###########################################################

            username_element = browser.find_element_by_xpath(element_for_username)
            username_element.send_keys(username)
            signInButton = browser.find_element_by_xpath(element_for_submit)
            time.sleep(2)
            signInButton.click()
            time.sleep(10)
            password_element = browser.find_element_by_name(element_for_password)
            password_element.send_keys(password)
            signInButtonPass = browser.find_element_by_xpath(element_for_submit_pass)
            signInButtonPass.click()
            time.sleep(10)

            number_element = browser.find_element_by_xpath(element_for_number)
            number_element.send_keys(number)

            check_callkButton = browser.find_element_by_xpath(element_for_check_call)
            check_callkButton.click()
            nextCheckButton = browser.find_element_by_xpath(element_for_check_submit)
            nextCheckButton.click()





            # delete cookies
            browser.delete_all_cookies()
            #### to quit the browser uncomment the following lines ####
            time.sleep(10)
            browser.quit()
            ip_txt = open("Path for Ip.TXT", "r")
            m = number_txt.readlines()
            l = []
            for i in range(0, len(m) - 1):
                x = m[i]
                z = len(x)
                a = x[:z - 1]
                l.append(a)
            l.append(m[i + 1])
            ip = random.choice(l)
            options = Options()
            options.add_argument('--proxy-server=' + ip)
            browser = webdriver.Chrome(executable_path='ChromeDriverPath', chrome_options=options)

