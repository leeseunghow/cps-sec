from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os
import time

path = os.getcwd() + "/6th/chromedriver"
driver = webdriver.Chrome(path)

try :
    driver.get("https://ticket.melon.com/main/index.htm")
    time.sleep(1)

    searchIndex = "뮤지컬"
    element = driver.find_element_by_class_name("placeholder")
    element.send_keys(searchIndex)
    driver.find_element_by_class_name("btn_comm").click()

    driver.find_element_by_xpath('//*[@id="conts"]/div/div/ul/li[1]/div/div[1]/div/a').click()
    time.sleep(1)


    html = driver.page_source
    bs = BeautifulSoup(html, "html.parser")

    pages = int(bs.find("em", class_= "link_page").text)
    print(pages)
    


    title = []
    page_count = 1

    while True :
        html = driver.page_source
        bs = BeautifulSoup(html, "html.parser")
        now_pages = bs.find_all("a", class_ = "link_page")
        print("현재 페이지 갯수 = ", (len(now_pages) + 1))

        for i in range(len(now_pages) + 1) :
            html = driver.page_source
            bs = BeautifulSoup(html, "html.parser")

            conts = bs.find("div", class_ = "box_movie tapping on").find_all("div", class_ = "show_infor")

            title.append("page" + str(page_count))
            page_count += 1
            for c in conts :
                title.append(c.find("p", class_ = "infor_text").find("span", class_ = "show_title").text)

            
            if driver.find_element_by_xpath('//*[@id="drawPerformanceNavgation"]/div/a[' + str(i + 3) + ']') != None :
                driver.find_element_by_xpath('//*[@id="drawPerformanceNavgation"]/div/a[' + str(i + 3) + ']').click()

        if (i != 9) :
            break

finally :
    for t in title :
        if t.find("page") != -1 :
            print()
            print(t)
        else :
            print(t)

    driver.quit()