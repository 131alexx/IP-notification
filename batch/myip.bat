
@echo off
::It reads the current ip from the command curl
FOR /f %%i in ('curl https://api.ipify.org/') do ( 
	SET mytempIP=%%i
	)
FOR /f %%a in (myip.txt) do (
	SET myoldIP=%%a
	)

IF NOT %mytempIP% == %myoldIP% (
	
	ECHO %mytempIP% > "myip.txt"
	
	::Here you send a mail
	blat myip.txt -to sender\@domain.com -f receiver\@domain.com -subject "Subject of the mail "%date%-%time% -server 127.0.0.1 -port 25 -u user -pw password -pu user -ppw password -debug
	)
ECHO IP: %mytempIP% TIME: %date%-%time% >> "myip.log"
