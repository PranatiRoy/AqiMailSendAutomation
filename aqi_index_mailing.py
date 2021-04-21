cd="C:\\Users\\Pranati\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe"
import time
import pandas as pd
from bs4 import BeautifulSoup # for the beautiful soup we have to send the source code for the page.
from selenium import webdriver
import smtplib
browser=webdriver.Chrome(cd)

browser.get("https://www.aqi.in/dashboard/india/west-bengal/kolkata")


time.sleep(5)
a=browser.find_element_by_xpath('//div[@class="sectot-box-left"]')
aqi=a.find_element_by_xpath('//h2[@style="color:#d4cc0f"]').text
print(aqi)
aqi=int(aqi)

if aqi>100 and aqi<200:
	messege="The AQI is Poor"
elif aqi>=200 and aqi<300:
	messege="The AQI is Unhealthy"
elif aqi>=300 and aqi<400:
	messege="The AQI is Severe"
elif aqi>=400 and aqi<500:
	messege="The AQI is Hazardous"
else:
	messege="The AQI is Healthy"

subject='AQI Informtion Alert'

def send_email(subject,msg):
	server=smtplib.SMTP('smtp.gmail.com' , 587)
	print(1)
	server.starttls()
	print(2)
	server.login('Enter gmail id','Enter Password')
	print(3)
	messege='Subject:{}\n\n{}'.format(subject,msg)
	server.sendmail('sender mail id','receiving end mail id',messege)
	print(4)
	server.quit()
	print('Success:Email Sent')


	
send_email(subject,messege)
