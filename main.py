from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_web_driver = "C:\development\chromedriver_win32"
s = Service(chrome_web_driver)
driver = webdriver.Chrome(service=s)

driver.get("https://www.python.org/")
event_time = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_name = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
dates = []
names = []
index = [0,1,2,3,4]
for time in event_time:
    dates.append(time.text)

for name in event_name:
    names.append(name.text)
events = {key:{value1,value2} for (key,value1,value2) in zip(index,dates, names)}
print(events)