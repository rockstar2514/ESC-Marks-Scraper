from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
driver = webdriver.Firefox()
driver.get("http://srivalab.cse.iitk.ac.in:3004/")
inputElement = driver.find_element_by_id("rollno")
inputElement.send_keys("190253")
button=driver.find_element_by_tag_name("button")
button.click()
time.sleep(2)
here=driver.find_element_by_id("total")
print(here.text)
with open('marks.csv','a',encoding="utf-8",newline='') as csv_file:
    writer = csv.writer(csv_file)
    for i in range (19000,190100):
        try:
            inputElement.clear()
            inputElement.send_keys(str(i)) 
            button.click()
            WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                       'Timed out waiting for PA creation ' +
                                       'confirmation popup to appear.')

            alert = driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            here=str(i)
            here1=driver.find_element_by_id("name")
            here2=driver.find_element_by_id("section")
            here3=driver.find_element_by_id("mqsum")
            here4=driver.find_element_by_id("lasum")
            here5=driver.find_element_by_id("MQ")
            here6=driver.find_element_by_id("midsemlab")
            here7=driver.find_element_by_id("midsem")
            here8=driver.find_element_by_id("total")
            writer.writerow([here,here1.text,here2.text,here3.text,here4.text,here5.text,here6.text,here7.text,here8.text])
            
            
            
        
