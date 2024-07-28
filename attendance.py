import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

email = input("Enter your email: \n")

password = input("Enter your password: \n")

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://academia.srmist.edu.in/")

time.sleep(3)

driver.switch_to.frame("zohoiam")

email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='login_id']")))

email_input.send_keys(email)

nextBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='nextbtn']")))

nextBtn.click()

time.sleep(3)

password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='password']")))

password_input.send_keys(password)

submitBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='nextbtn']")))

submitBtn.click()

driver.switch_to.default_content()

WebDriverWait(driver, 10).until(EC.url_contains("WELCOME"))

time.sleep(3)

menu = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='hiddendMenu']"))).click()

myTimeTableBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='hiddendMenu']/div/ul/li[2]"))).click()

attendanceBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='hiddendMenu']/div/ul/li[2]/div/ul/li[2]"))).click()

WebDriverWait(driver, 10).until(EC.url_contains("My_Attendance"))

time.sleep(3)

subjects = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='zc-viewcontainer_My_Attendance']/div/div[4]/div/table[3]/tbody/tr[1]/following-sibling::tr")))

# print(subjects)

print("Subject Code     Subject Name    Faculty     Conducted    Absent     Attendance%")

for sub in subjects:
    print(sub.text)