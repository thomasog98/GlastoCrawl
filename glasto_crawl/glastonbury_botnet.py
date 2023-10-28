# Author: Thomas OGrady
# Filename: glastonbury_botnet.py
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import glastonbury as glasto
import time
import os

glastonbury_url="https://glastonbury.seetickets.com/content/extras"
#glastonbury_url="https://glastonbury.seetickets.com/event/glastonbury-2024/worthy-farm/2400000"
#glastonbury_url="https://glastonbury.seetickets.com/event/glastonbury-2024-deposits/worthy-farm/2400000"
#glastonbury_url="http://127.0.0.1:8080/"
refresh_phrases = ["You will be held at this page until there is a free space on the booking site"]
kill_phrases = ["Registration Number:","Postcode:"]
path = r"C:\chromedriver.exe"
refresh_rate=0.8
reg_1 = "reg_1"
reg_2 = "reg_2"
reg_3 = "reg_3"
reg_4 = "reg_4" 

reg_details = {reg_1:[],reg_2:[],reg_3:[],reg_4:[]}

csvfile = csv.reader(open(r"C:\glasto_crawl\reg-details.csv","r"))
cnt = 1
for row in csvfile:
    reg_num = "reg_" + str(cnt)
    reg_details[reg_num].append(row[0])
    reg_details[reg_num].append(row[1])
    cnt+=1

def populate_form():
    print("Population form")
    page_cnt=0
    try: 
        for reg_cnt in reg_details:
            browser.find_element(By.ID, "registrations_"+str(page_cnt)+"__RegistrationId").send_keys(reg_details[reg_cnt][0])
            browser.find_element(By.ID, "registrations_"+str(page_cnt)+"__PostCode").send_keys(reg_details[reg_cnt][1])
            page_cnt+=1
        #Submit after populating
        browser.find_element(By.ID, "add_registrations").click()
    except:
        print("Issue posting")
        time.sleep(1000000)
    #Prevent the script from exiting while paying for the stuff
    time.sleep(1000000)
    time.sleep(1000000)

celenium_srv = glasto.srv(path)
browser = webdriver.Chrome(service = celenium_srv.chrome_services,options=celenium_srv.chrome_options)
print("Welcome to Glastonbury Botnet for 2023")
try:
    browser.get(glastonbury_url)
except:
    print("Retrying url")
    try:
        browser.get(glastonbury_url)
    except:
        print("failed to connect to website")


while True:
    page = browser.page_source
    for phrase in kill_phrases:
        if (phrase in page):
            print("You should now be on the booking site at this point")
            populate_form()
            break  
        else:
            time.sleep(refresh_rate)
            print("Refreshing...")
            if(os.path.isfile(r"C:\kill")):
                print("Killing auto refresh")
                break
            browser.refresh()
        
#Catch all in case the script does happen to get to the booking page but fails to post 
time.sleep(1000000)