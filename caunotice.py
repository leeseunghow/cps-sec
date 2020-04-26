from selenium import webdriver
from bs4 import BeautifulSoup
import os
import time

path = os.getcwd() + "/6th/chromedriver"

driver = webdriver.Chrome(path)

try :
    driver.get("https://www.cau.ac.kr/cms/FR_CON/index.do?MENU_ID=100#page1")
    time.sleep(1)

    html = driver.page_source
    bs = BeautifulSoup(html, "html.parser")

    pages = bs.find("div", class_ = "pagination").find_all("a")[-1]["href"].split("page")[1]
    pages = int(pages)
    print(pages)

    title = []
    for i in range(3) :
        driver.get("https://www.cau.ac.kr/cms/FR_CON/i^0ndex.do?MENU_ID=100#page" + str(i + 1))
        time.sleep(3)

        html = driver.page_source
        bs = BeautifulSoup(html, "html.parser")

        conts = bs.find_all("div", class_ = "txtL")
        title.append("page" + str(i + 1))
        for c in conts :
            print(c.find("a").text)


finally:
    #time.sleep(3)
    for t in title :
        if t.find("page") != -1 :
            print()
            print(t)
        else :
            print(t)
    driver.quit()
