# Dynamic IP notification

This project was made with the intention of revieving the dynamic IP address on a change. 

## Execution of the programs

##### Bash scripting
The script is ready to be executed as a regular script.

`./myip.sh`

##### Batch scripting
The script is ready to be executed as a regular script.

`myip`

##### Python scripting
The script is ready to be executed as a regular script.

`./ip.py`

This uses a python library: if it throws you an error, install the module with pip:
~~~~
sudo apt install python-pip
pip install requests
~~~~

## Program the task

##### Linux
In Linux you can use cron daemon schedule jobs.
~~~~
crontab -e
~~~~
And introduce the next line to execute the script periodically.
This will execute the python script every 5 minutes:
~~~~
*/5 * * * * cd /path/to/repo/dynamic-IP-notification/python;./ip.py
~~~~


##### Windows


## Programming languages
- [x] Bash scripting
- [x] Batch scripting
- [X] Python
- [ ] C
