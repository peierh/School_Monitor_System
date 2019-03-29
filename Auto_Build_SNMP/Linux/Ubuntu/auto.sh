#!/bin/bash 

sudo apt update -y 
sudo apt upgrade -y
sudo apt install net-tools -y
sudo apt install snmpd snmp-mibs-downloader -y
sudo sed -i '5c #export MIBS=' /etc/default/snmpd
sudo sed -i '11c SNMPDOPTS="'"-Lsd -Lf /dev/null -u snmp -g snmp -I -smux, -p /run/snmpd.pid"'"' /etc/default/snmpd


##get IP
#MY_IP=$(hostname -I) or 
#IP=$(ifconfig  | grep 'inet addr:'| grep -v '127.0.0.1' |cut -d: -f2 | awk '{ print $1}')
#echo $MY_IP

sudo sed -i '15c agentAddress  udp:0.0.0.0:161' /etc/snmp/snmdp.conf
sudo sed -i '49c rocommunity public  localhost ' /etc/snmp/snmpd.conf

                                     #librenmsIP
sudo sed -i '50c rocommunity imac-iot 172.3.0.3' /etc/snmp/snmpd.conf

sudo service snmpd restart

