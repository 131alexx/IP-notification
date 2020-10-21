#!/usr/bin/env bash
#Pick current IP
myTempIP="$(curl https://api.ipify.org)"
#Pick saved IP
myOldIP="$(head -n 1 /home/alex/myIPproject/myip.txt)"


if [ "$myTempIP" != "$myOldIP" ]
then
#if are different, save the new IP and send a mail
echo "$myTempIP" > /path/to/ip/myip.txt
echo "IP: $myTempIP Date: $(date)" | mail -s "La IP ha cambiado" "user@mail.com"
fi



#save a log of the current check
echo "IP: $myTempIP Date: $(date)" >>/path/to/logs/myip.log

