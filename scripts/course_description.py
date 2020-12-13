# Load selenium components
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def course_desc():
# Establish chrome driver and go to report site URL
    url = "https://enr-apps.as.cmu.edu/open/SOC/SOCServlet/search"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    count = 0
    driver.find_element_by_xpath("/html/body/div/div[2]/form/div[3]/div/div/button[1]").click()
    tables = driver.find_elements_by_id("search-results-table")
    
    input_path = './course_description_1.txt'
    f = open(input_path,"a+")
    
    # Crawl course description through full x_path matching
    for tab_num in range(2,len(tables)):
        courses = tables[tab_num].find_elements_by_tag_name('tr') 
        
        for i in range(1,len(courses)):
            path = "/html/body/div/div[2]/table["+str(tab_num+1)+"]/tbody/tr["+str(i)+"]/td[1]/a"
            try:
                handler = driver.find_element_by_xpath(path)
                cID = handler.text
                driver.execute_script("arguments[0].scrollIntoView();", handler)
                handler.click()
            # If the row is a subrow of a specific course, skip it
            except:
                continue
            # Wait for the website to response
            time.sleep(3)
            description = driver.find_element_by_class_name("text-left").text
            f.write(cID+":"+description)
            f.write('\n')
            driver.find_element_by_class_name("close").click()
    f.close()  

