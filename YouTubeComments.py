from numpy import False_
import pandas as pd   
import time
import spacy
import os
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
data=[]
iterations = 3
delay = 3


with Chrome(executable_path=r'C:\Users\SHAHARYAR\Documents\chromedriver.exe',chrome_options=options) as driver:
    wait = WebDriverWait(driver,15)
    driver.get(input("Please Enter the YouTube URL: "))

    for item in range(iterations): 
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(delay)
    
    buttons = wait.until(EC.presence_of_all_elements_located((By.ID, "more-replies")))

    for elements in buttons:
        try: 
            elements.click()
        except:
            pass

    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content-text"))):
        if len(comment.text) > 5:
            data.append(comment.text)
    j = 0
    count = 0
    TotalCount = len(data)
    processedComm = []
    nlp = spacy.load("en_core_web_lg")
    threshold = 0.99
    os.system('cls||clear')


    for i in range(len(data)):
        j = i+1

        while(j < len(data) - 1):
            doc1 = nlp(data[i])
            doc2 = nlp(data[j])
            
            if doc1.similarity(doc2) >= threshold and i!=j and (i not in processedComm) and (j not in processedComm):

                print(f"{i}: ", data[i])
                print(f"{j}: ", data[j])
                processedComm.append(i)
                processedComm.append(j)
                count+=1
                break
            
            j = j + 1
            
    print(f"Total Comments: {TotalCount}")
    print(f"Spam Comments: {count}")

    



