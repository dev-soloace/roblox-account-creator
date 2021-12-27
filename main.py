from selenium.webdriver.common import keys
from random_username.generate import generate_username
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time
import os

driver = webdriver.Chrome()
driver.get('https://roblox.com/')

def main():
    elem = driver.find_element_by_xpath('//*[@id="signup-username"]')
    elem.clear()

    birthmonth = driver.find_element_by_xpath('//*[@id="MonthDropdown"]')
    birthmonth.click()
    jan = driver.find_element_by_xpath('//*[@id="MonthDropdown"]/option[2]')
    jan.click()

    day = driver.find_element_by_xpath('//*[@id="DayDropdown"]')
    day.click()
    num = driver.find_element_by_xpath('//*[@id="DayDropdown"]/option[2]')
    num.click()

    year = driver.find_element_by_xpath('//*[@id="YearDropdown"]')
    year.click()
    num1 = driver.find_element_by_xpath('//*[@id="YearDropdown"]/option[38]')
    num1.click()


    name = generate_username(1)[0]
    elem.send_keys(name)

    time.sleep(2)

    # check if username valid
    checker = driver.find_element_by_id('signup-usernameInputValidation')
    text = checker.get_attribute('textContent')
    time.sleep(0.5)

    def check():
        if text == "This username is already in use.":
            elem.clear()
            elem.send_keys(generate_username(1)[0])
        elif text == "Username not appropriate for Roblox.":
            elem.clear()
            elem.send_keys(generate_username(1)[0])

    password = driver.find_element_by_xpath('//*[@id="signup-password"]')
    passs = generate_username(1)[0]
    password.send_keys(passs)

    # double check again
    if len(text) > 1:
        check()

    sign = driver.find_element_by_xpath('//*[@id="signup-button"]')
    sign.click()
    os.system('cls')


    try:
        # wait for captcha to finish and then log the cookie
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="FunCaptcha"]')))
        WebDriverWait(driver, 100).until_not(EC.presence_of_element_located((By.XPATH, '//*[@id="FunCaptcha"]')))
    except TimeoutException:
        pass

    open('cookies.txt', 'a')
    file = open('cookies.txt', 'a')
    time.sleep(1)
    file.write("{}:{}:{}\n".format(name, passs, driver.get_cookie('.ROBLOSECURITY')["value"]))
    file.close()
    driver.delete_cookie('.ROBLOSECURITY')
    driver.get('https://www.roblox.com/')
    time.sleep(1)
    main()

if __name__ == "__main__":
    main()
