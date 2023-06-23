import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

options=webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
service_obj=Service(r"C:/Users/Abhishek/Downloads/chromedriver.exe")
driver = webdriver.Chrome(options=options,service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys('ber')
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,".search-button").click()
Elist=['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
AList=[]
items=driver.find_elements(By.XPATH, "//div[@class='products']/div")
count=len(items)
assert count > 0
for i in items:
    AList.append(i.find_element(By.XPATH, "h4").text)
    i.find_element(By.XPATH,"div/button").click()
assert Elist==AList

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[normalize-space()='PROCEED TO CHECKOUT']").click()

prices=driver.find_elements(By.XPATH,"//td[5]/p")
sum=0
for p in prices:
    sum=sum+int(p.text)
print(sum)
total=driver.find_element(By.CSS_SELECTOR,".totAmt").text
assert sum==int(total)



driver.find_element(By.XPATH,"//input[@placeholder='Enter promo code']").send_keys("rahulshettyacademy")
#driver.find_element(By.CSS_SELECTOR," .promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR," .promoBtn").click()

wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoInfo")))
discountAmt=driver.find_element(By.CSS_SELECTOR,".discountAmt").text
print(discountAmt)
assert int(total) > float(discountAmt)

m=driver.find_element(By.CLASS_NAME,"promoInfo").text
assert 'applied' in m
driver.find_element(By.XPATH,"//button[normalize-space()='Place Order']").click()
driver.find_element(By.CLASS_NAME,"chkAgree").click()
