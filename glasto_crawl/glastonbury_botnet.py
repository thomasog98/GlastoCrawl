# Author: Thomas OGrady
# Filename: glastonbury_botnet.py
import csv
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import glastonbury as glasto
import time
import os
from datetime import datetime


#glastonbury_url="https://glastonbury.seetickets.com/content/extras"
#glastonbury_url="https://glastonbury.seetickets.com/event/glastonbury-2024/worthy-farm/2400000"
#glastonbury_url="https://glastonbury.seetickets.com/event/glastonbury-2024-deposits/worthy-farm/2400000"
glastonbury_url="https://glastonbury.seetickets.com/event/glastonbury-2024-deposits/worthy-farm/3500000"
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

    try: 

        time_date = datetime.now()
        print(time_date,"Populating form with registration details\n")
        page_cnt=0
        # Added 0.5 second delay before attempting reg publishing allows the webpage to load fully 
        time.sleep(0.5)
        for reg_cnt in reg_details:
            browser.find_element(By.ID, "registrations_"+str(page_cnt)+"__RegistrationId").send_keys(reg_details[reg_cnt][0])
            browser.find_element(By.ID, "registrations_"+str(page_cnt)+"__PostCode").send_keys(reg_details[reg_cnt][1])
            page_cnt+=1

        # Submit after populating
        # Tthis needs some work add_registrations does not exist. 
        time_date = datetime.now()
        print(time_date,"Submitting registration details\n")
        add_reg = browser.find_element(By.ID, "add_registrations")
        browser.execute_script("arguments[0].scrollIntoView();", add_reg)
        browser.execute_script("arguments[0].click();", add_reg)
       # browser.find_element(By.ID, "add_registrations").Click()
        time_date = datetime.now()
        print(time_date,"Sucessfully added reg details\n")

    except Exception as e:
        print("Issue posting, sleeping for a while",e)
        time.sleep(1000000)
    #Prevent the script from exiting while paying for the stuff
    time_date = datetime.now()
    print(time_date,"Please now enter your card details to pay, entering sleep timer\n")
    time.sleep(1000000)
    time.sleep(1000000)

print("Welcome to Glastonbury Botnet for 2024")
print("If you need to kill the refreshes, place kill in C directory\n")
print("Please ensure you are using the correct chromedriver/Chrome version, Good Luck!\n")

try:
    try:
        celenium_srv = glasto.srv(path)
        browser = webdriver.Chrome(service = celenium_srv.chrome_services,options=celenium_srv.chrome_options)
        
    except Exception as ex:
        print("Unable to start Chromedriver application, exiting application in 10 ", ex)
        time.sleep(10)

    browser.get(glastonbury_url)
    time_date = datetime.now()

    print("\n"+str(time_date)+" Browser connection established")
except:
    time_date = datetime.now()
    print("\n"+str(time_date)+" Failed to connect to website")
    print("\n"+str(time_date)+" Retrying url")
    try:
        browser.get(glastonbury_url)
        time_date = datetime.now()
        print("\n"+str(time_date)+" Browser connection established")
    except:
        try:
            time_date = datetime.now()
            print("\n"+str(time_date)+" Failed to connect to website")
            print("\n"+str(time_date)+" Retrying url #2")
            browser.get(glastonbury_url)
            time_date = datetime.now()
            print("\n"+str(time_date)+" Browser connection established")
        except:
            try:
                time_date = datetime.now()
                print("\n"+str(time_date)+" Failed to connect to website")
                print("\n"+str(time_date)+" Retrying url #3")
                browser.get(glastonbury_url)
                time_date = datetime.now()
                print("\n"+str(time_date)+" Browser connection established")
            except:
                time_date = datetime.now()
                print("\n"+str(time_date)+" Failed to connect to website, exiting in 5 seconds \n")
                time.sleep(5)
                exit()

while True:
    page = browser.page_source
    for phrase in kill_phrases:
        if (phrase in page):
            time_date = datetime.now()
            print("\n"+str(time_date)+" You should now be on the booking site at this point\n")

            populate_form()
            break  
        else:
            time.sleep(refresh_rate)
            time_date = datetime.now()
            print(time_date,"Refreshing...")
            if(os.path.isfile(r"C:\kill")):
                print("Killing auto refresh")
                break
            browser.refresh()
        
#Catch all in case the script does happen to get to the booking page but fails to post 
time.sleep(1000000)
