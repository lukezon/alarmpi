#Welcome to my version of the Alarm Pi code.

I have made a few ajustments and added some things to suit my needs.
There are still many extreme bugs with my code, please report any to me if you find them.

###Added
- Ivona Voice Support
- MTA Subway Alerts
- Customizable Alarm tone

##Setup
1. ```sudo apt-get install python-feedparser mpg123 festival```
2. ```sudo apt-get install libxml2-dev libxslt-dev python-dev```
3. ```sudo apt-get install python3-lxml```
4. ```sudo pip install pyvona```

####You *_MUST_* use ramfs to avoid wear on your card and to enable Google Voice/Ivona.

5. ```sudo mkdir -p /mnt/ram```
6. ```echo "ramfs /mnt/ram ramfs nodev,nosuid,noexec,nodiratime,size=64M 0 0" | sudo tee -a /etc/fstab``` 


###Alarm Time Setup
- Use [Ubuntu CronHowto to help set up timing](https://help.ubuntu.com/community/CronHowto)
1. ```crontab -e```
2. ```%MINUTE %HOUR %DAY %MONTH %DAYOFWEEK sudo python /home/pi/sound_the_alarm.pi```
