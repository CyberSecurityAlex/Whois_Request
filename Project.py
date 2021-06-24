#!/usr/bin/env python3
import re
import whois
import yaml
import json
import filecmp
import smtplib
import ezgmail
import datetime
import filecmp
import schedule
import time
#Send Email Function
def send_email():
    smtp_server = "smtp.mailtrap.io"
    login = ""
    password = ""
    Subject = 'There is an update!'
    msg = MIMEMultipart('alternative')
    msg['From'] = ''
    msg['To'] = ''
    msg['Subject'] =  Subject
    main = "Check log files in thiw day and the previous one!"
    msg.attach(MIMEText(main, 'plain'))
    attachment = MIMEText(json.dumps(data))
    attachment.add_header('Content-Disposition' , 'attachment' , filename = "Updated_info.json")
    msg.attach(attachment)
    mail = smtplib.SMTP('smtp.mailtrap.io", 2525')
    mail.send_message(msg)
    mail.quit()
#Example of three Domains
Domains = [{'Link': 'https://whois.whoisxmlapi.com/'},
           {'Link': 'https://webscraping.com/'},
           {'Link': 'https://www.cvedetails.com/'}]
#Create Domains.Yaml
new = open('Domains.yaml', "w")
new.write(str(Domains))
new.close()
#Read Domains.Yaml and isolate the Urls
new = open('Domains.yaml' , "r")
read = new.read()
url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', read)
new.close()
#Whois requests:whoisxmlapi = url[0] , webscraping = url [1] , cvedetails = url[2]
r = whois.whois(url[0])
initial_data_from_whoisxmlapi = r
r = whois.whois(url[1])
initial_data_from_webscraping = r
r = whois.whois(url[2])
initial_data_from_cvedetails = r
#Daily_Task Function
def Task():
    #Initialization
    initial_data_from_whoisxmlapi.creation_date
    initial_data_from_whoisxmlapi.updated_date
    initial_data_from_whoisxmlapi.expiration_date
    initial_data_from_whoisxmlapi.emails
    initial_data_from_webscraping.creation_date
    initial_data_from_webscraping.updated_date
    initial_data_from_webscraping.expiration_date
    initial_data_from_webscraping.emails
    initial_data_from_cvedetails.creation_date
    initial_data_from_cvedetails.updated_date
    initial_data_from_cvedetails.expiration_date
    initial_data_from_cvedetails.emails
    #With every loop, .json file is called as a different name(identifier->date)
    Present = datetime.datetime.now()
    print (Present.strftime("%Y-%m-%d %H:%M:%S"))
    Date = Present.strftime("%d-%m-%Y %H:%M:%S")
    Record = open(Date + '.json' , "w")
    r = whois.whois(url[0])
    update_from_whoisxmlapi = r
    r = whois.whois(url[1])
    update_from_webscraping = r
    r = whois.whois(url[2])
    update_from_cvedetails = r
    data = str(update_from_whoisxmlapi.creation_date) + str(update_from_whoisxmlapi.updated_date) + str(update_from_whoisxmlapi.expiration_date) + str(update_from_whoisxmlapi.emails) + str(update_from_webscraping.creation_date) + str(update_from_webscraping.updated_date) +  str(update_from_webscraping.expiration_date) + str(update_from_webscraping.emails) + str(update_from_cvedetails.creation_date) + str(update_from_cvedetails.updated_date) + str(update_from_cvedetails.expiration_date) + str(update_from_cvedetails.emails)
    Record.write(data)
    #Get Params of whois requests(Update)
    update_from_whoisxmlapi.creation_date
    update_from_whoisxmlapi.updated_date
    update_from_whoisxmlapi.expiration_date
    update_from_whoisxmlapi.emails
    update_from_webscraping.creation_date
    update_from_webscraping.updated_date
    update_from_webscraping.expiration_date
    update_from_webscraping.emails
    update_from_cvedetails.creation_date
    update_from_cvedetails.updated_date
    update_from_cvedetails.expiration_date
    update_from_cvedetails.emails
    #Create email attachment as "Updated_info.json and write any changes from requests day by day
    File2= open('Updated_info.json' , "w")
    if initial_data_from_whoisxmlapi.creation_date != update_from_whoisxmlapi.creation_date:
        File2.write(update_from_whoisxmlapi.creation_date)
    if initial_data_from_whoisxmlapi.updated_date != update_from_whoisxmlapi.updated_date:
        File2.write(update_from_whoisxmlapi.updated_date)
    if initial_data_from_whoisxmlapi.expiration_date != update_from_whoisxmlapi.expiration_date:
        File2.write(update_from_whoisxmlapi.expiration_date)
    if initial_data_from_whoisxmlapi.emails != update_from_whoisxmlapi.emails:
        File2.write(update_from_whoisxmlapi.emails)
    if initial_data_from_webscraping.creation_date != update_from_webscraping.creation_date:
        File2.write(update_from_webscraping.creation_date)
    if initial_data_from_webscraping.updated_date != update_from_webscraping.updated_date:
        File2.write(str(update_from_webscraping.updated_date))
    if initial_data_from_webscraping.expiration_date != update_from_webscraping.expiration_date:
        File2.write(update_from_webscraping.expiration_date)
    if initial_data_from_webscraping.emails != update_from_webscraping.emails:
        File2.write(update_from_webscraping.emails)
    if initial_data_from_cvedetails.creation_date != update_from_cvedetails.creation_date:
        File2.write(update_from_cvedetails.creation_date)
    if initial_data_from_cvedetails.updated_date !=  update_from_cvedetails.updated_date:
        File2.write(update_from_cvedetails.updated_date)
    if initial_data_from_cvedetails.expiration_date != update_from_cvedetails.expiration_date:
        File2.write(update_from_cvedetails.expiration_date)
    if initial_data_from_cvedetails.emails != update_from_cvedetails.emails:
        File2.write(update_from_cvedetails.emails)
        File2.close()
        
    Record = open(Date + '.json' , "r")
    File2= open('Updated_info.json' , "r")
    Comparison = filecmp.cmp(Date + '.json' , 'Updated_info.json')
    if True:
        print("NO CHANGES TODAY...")
    else:
        send_email()
        
        initial_data_from_whoisxmlapi.creation_date = update_from_whoisxmlapi.creation_date
        initial_data_from_whoisxmlapi.updated_date = update_from_whoisxmlapi.updated_date
        initial_data_from_whoisxmlapi.expiration_date =update_from_whoisxmlapi.expiration_date
        initial_data_from_whoisxmlapi.emails = update_from_whoisxmlapi.emails
        initial_data_from_webscraping.creation_date = update_from_webscraping.creation_date
        initial_data_from_webscraping.updated_date = update_from_webscraping.updated_date
        initial_data_from_webscraping.expiration_date = update_from_webscraping.expiration_date
        initial_data_from_webscraping.emails = update_from_webscraping.emails
        initial_data_from_cvedetails.creation_date = update_from_cvedetails.creation_date
        initial_data_from_cvedetails.updated_date = update_from_cvedetails.updated_date
        initial_data_from_cvedetails.expiration_date = update_from_cvedetails.expiration_date
        initial_data_from_cvedetails.emails = update_from_cvedetails.emails

schedule.every(24).hours.do(Task)
while 1:
    schedule.run_pending()
    time.sleep(1)
