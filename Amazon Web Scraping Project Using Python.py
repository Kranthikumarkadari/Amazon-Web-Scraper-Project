#!/usr/bin/env python
# coding: utf-8

# In[38]:


# import libraries 

from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib


# In[2]:


# Connect to Website and pull in data

URL = 'https://www.amazon.com/AmazonBasics-Wireless-Computer-Mouse-Receiver/dp/B005EJH6Z4/ref=sr_1_7_ffob_sspa?crid=23EOVZAG39K9O&keywords=mouse&qid=1679737567&sprefix=mouse%2Caps%2C324&sr=8-7-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzVTYwUk5RM1VTSVc3JmVuY3J5cHRlZElkPUEwNjEyMzczSDNINFgyOTdTQzBCJmVuY3J5cHRlZEFkSWQ9QTA0MzA4NzEzMldEMzIyTFlNN1dDJndpZGdldE5hbWU9c3BfbXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

print(soup1)


# In[3]:


# Connect to Website and pull in data

URL = 'https://www.amazon.com/AmazonBasics-Wireless-Computer-Mouse-Receiver/dp/B005EJH6Z4/ref=sr_1_7_ffob_sspa?crid=23EOVZAG39K9O&keywords=mouse&qid=1679737567&sprefix=mouse%2Caps%2C324&sr=8-7-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzVTYwUk5RM1VTSVc3JmVuY3J5cHRlZElkPUEwNjEyMzczSDNINFgyOTdTQzBCJmVuY3J5cHRlZEFkSWQ9QTA0MzA4NzEzMldEMzIyTFlNN1dDJndpZGdldE5hbWU9c3BfbXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

#Prettify is used to make things (i.e. html formatting )look better 

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

print(soup2)


# In[4]:



# Connect to Website and pull in data

URL = 'https://www.amazon.com/Apple-MacBook-Laptop-12%E2%80%91core-19%E2%80%91core/dp/B0BSHF7WHW/ref=sr_1_3?crid=D6994LPNDF9C&keywords=macbook+pro+m2+16+inch&qid=1679734433&sprefix=%2Caps%2C1662&sr=8-3'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

#Prettify is used to make things (i.e. html formatting )look better 

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

print(soup2)


# In[5]:


# Connect to Website and pull in data

URL = 'https://www.amazon.com/AmazonBasics-Wireless-Computer-Mouse-Receiver/dp/B005EJH6Z4/ref=sr_1_7_ffob_sspa?crid=23EOVZAG39K9O&keywords=mouse&qid=1679737567&sprefix=mouse%2Caps%2C324&sr=8-7-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzVTYwUk5RM1VTSVc3JmVuY3J5cHRlZElkPUEwNjEyMzczSDNINFgyOTdTQzBCJmVuY3J5cHRlZEFkSWQ9QTA0MzA4NzEzMldEMzIyTFlNN1dDJndpZGdldE5hbWU9c3BfbXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

#Prettify is used to make things (i.e. html formatting )look better 

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id='productTitle').get_text()

print(title)


# In[54]:


# Connect to Website and pull in data

URL = 'https://www.amazon.com/AmazonBasics-Wireless-Computer-Mouse-Receiver/dp/B005EJH6Z4/ref=sr_1_7_ffob_sspa?crid=23EOVZAG39K9O&keywords=mouse&qid=1679737567&sprefix=mouse%2Caps%2C324&sr=8-7-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzVTYwUk5RM1VTSVc3JmVuY3J5cHRlZElkPUEwNjEyMzczSDNINFgyOTdTQzBCJmVuY3J5cHRlZEFkSWQ9QTA0MzA4NzEzMldEMzIyTFlNN1dDJndpZGdldE5hbWU9c3BfbXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

#Prettify is used to make things (i.e. html formatting )look better 

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id='productTitle').get_text()

price = soup2.find(id='corePrice_desktop').get_text()

print(title)
print(price)


# In[56]:


# Clean up the data a little bit
price = price.strip()[25:]
title = title.strip()
print(title)
print(price)


# In[57]:


# Create a Timestamp for your output to track when data was collected

import datetime

today = datetime.date.today()

print(today)


# In[58]:


# Create CSV and write headers and data into the file

import csv 

header = ['Title', 'Price', 'Date']
data = [title, price, today]


with open('AmazonWebScraperDataset1.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


# In[65]:



import pandas as pd

df = pd.read_csv(r'C:\Users\kadar\AmazonWebScraperDataset1.csv')

print(df)


# In[64]:


#Now we are appending data to the csv

with open('AmazonWebScraperDataset1.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[78]:


#Combine all of the above code into one function


def check_price():
   
    URL = 'https://www.amazon.com/AmazonBasics-Wireless-Computer-Mouse-Receiver/dp/B005EJH6Z4/ref=sr_1_7_ffob_sspa?crid=23EOVZAG39K9O&keywords=mouse&qid=1679737567&sprefix=mouse%2Caps%2C324&sr=8-7-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzVTYwUk5RM1VTSVc3JmVuY3J5cHRlZElkPUEwNjEyMzczSDNINFgyOTdTQzBCJmVuY3J5cHRlZEFkSWQ9QTA0MzA4NzEzMldEMzIyTFlNN1dDJndpZGdldE5hbWU9c3BfbXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text()

    price = soup2.find(id='corePrice_desktop').get_text()

    price= price.strip()[25:]
    title = title.strip()

    import datetime

    today = datetime.date.today()
    
    import csv 

    header = ['Title', 'Price', 'Date']
    data = [title, price, today]

    with open('AmazonWebScraperDataset1.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    if int(price) < 6.00:
        send_mail()


# In[ ]:


def check_price():
    # some code to get the price as a string
    price_str = "" # example string
    
    try:
        price_int = int(float(price_str)) # convert the string to float first before converting to integer
        print(price_int)
    except ValueError:
        print("Error: could not convert price to integer")


# In[76]:


# Runs check_review after a set time and inputs data into your CSV

while(True):
    check_price()
    time.sleep(1)


# In[72]:


import pandas as pd

df = pd.read_csv(r'C:\Users\kadar\AmazonWebScraperDataset1.csv')

print(df)


# In[73]:


# If uou want to try sending yourself an email (just for fun) when a  hits below a certain level you can try it
# out with this script

def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('kadarikranthikumar0917@gmail.com','Nanipotti@143')
    
    subject = "The laptop you want is below 3000£! Now is your chance to buy!"
    body = "kranthi, This is the moment we have been waiting for. Now is your chance to pick up the best laptop of your dreams. Don't mess it up! Link here: https://www.amazon.com/AmazonBasics-Wireless-Computer-Mouse-Receiver/dp/B005EJH6Z4/ref=sr_1_7_ffob_sspa?crid=23EOVZAG39K9O&keywords=mouse&qid=1679737567&sprefix=mouse%2Caps%2C324&sr=8-7-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzVTYwUk5RM1VTSVc3JmVuY3J5cHRlZElkPUEwNjEyMzczSDNINFgyOTdTQzBCJmVuY3J5cHRlZEFkSWQ9QTA0MzA4NzEzMldEMzIyTFlNN1dDJndpZGdldE5hbWU9c3BfbXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'kadarikranthikumar0917@gmail.com',
        msg
     
    )

