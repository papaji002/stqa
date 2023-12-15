import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
def main():
   options =Options()
   options.add_experimental_option("excludeSwitches" , ["enable-automation"])
   service = Service(r"C:\Users\ppro0\Downloads\chromedriver_win32\chromedriver.exe")
   driver = webdriver.Chrome(options=options ,service=service)
   url = 'https://www.linkedin.com/'
   driver.get(url)
   time.sleep(1)
   email = driver.find_element(By.ID, 'session_key')
   email.send_keys("ppro00012@gmail.com")
   time.sleep(1)
   password =driver.find_element(By.ID, "session_password")
   password.send_keys("Sam9033@")
   time.sleep(1)
   btn =driver.find_element(By.XPATH , '/html/body/main/section[1]/div/div/form/div[2]/button')
   btn.click()
   time.sleep(4)
main()


"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://linkedin.com/")
time.sleep(2)   
email = driver.find_element(By.ID , "session_key")
email.send_keys("uremail@gmail.com")
time.sleep(2)
password = driver.find_element(By.ID , "session_password")
password.send_keys("pass#69")
time.sleep(2)
btn = driver.find_element(By.XPATH , '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')
btn.click()
time.sleep(2)


"""