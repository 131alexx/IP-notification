#!/usr/bin/python

import json
import requests
import smtplib
import datetime

def ipChangeFunction(oldIP, newIP):
    print oldIP+"->"+newIP
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('user', 'pass')
    now = datetime.datetime.now()
    msg = "\n The IP change detected on "+now.strftime("%a, %d/%m/%y  %H:%M")+" to IP: "+newIP
    server.sendmail('from@mail.com', 'to@mail.com', msg)

def main():
    #Get the actual IP
    ipJSON = requests.get('http://api.ipify.org/?format=json').text
    myTempIP = str(json.loads(ipJSON)['ip'])
    
    #Read the last IP from file
    file = open('ip.txt', 'rw+')
    #Replace the \x00 char of hte file
    myOldIP =  file.read().replace('\x00','')
    logs = open('ip.log', 'a+')
    now = datetime.datetime.now()
    if(myTempIP != myOldIP):
        #If the IP changed -> replace it for the new one
        #Write on start of the file
        file.truncate(0)
        file.write(myTempIP)

        logs.write(now.strftime("%a, %d/%m/%y  %H:%M")+' | IP changed from '+myOldIP.replace('\n','')+' to '+myTempIP+'\n')     
        ipChangeFunction(myOldIP, myTempIP)
    else:

        logs.write(now.strftime("%a, %d/%m/%y  %H:%M")+' | IP checked '+myTempIP+'\n')     

    file.close()



if __name__ == '__main__':
    main()
