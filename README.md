Welcome to my version of the Alarm Pi code.

I have made a few ajustments and added some things to suit my needs.

Some Changes:
-Ivona Voice Support
-MTA Subway Alerts
-Customizable Alarm tone


*required packages INSTALL IN THIS ORDER:

  sudo apt-get install python-feedparser mpg123 festival
  
  sudo apt-get install libxml2-dev libxslt-dev python-dev

  sudo apt-get install python3-lxml


** YOU MUST USE RAMFS to avoid wear on your card and to enable Google Voice/Ivona.

  sudo mkdir -p /mnt/ram

  echo "ramfs       /mnt/ram ramfs   nodev,nosuid,noexec,nodiratime,size=64M   0 0" | sudo tee -a /etc/fstab 


*** and finally to set your alarm for 730AM Mon-Fri

  crontab -e 

  Then add this: 30 7 * * 1-5 sudo python /home/pi/sound_the_alarm.pi



There are still many extreme bugs with my code, please report any to me if you find them.