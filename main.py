from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# url = input("Enter URL: ")
# no_of_views = int(input("Enter no of Views: "))
# duration = float(input("Enter duration for each view (in seconds): "))
url = "https://www.iu2frl.it"
no_of_views = 5
duration = 5
print("Running")

for i in range(0,no_of_views):
    browser = webdriver.Chrome()

    browser.get(url)
    browser.find_element(By.ID, "av-body").send_keys(Keys.SPACE)
    
    time.sleep(duration)
    
    print(str(i+1) + " iterations done")
    
    browser.quit()