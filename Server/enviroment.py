import os, sys
import requests
import time

create_grafana_datasource = 0
create_grafana_dashboard = 0
datasources = open("datasource.json", "r")
dashboard = open("dashboard.json", "r")
datasources_info = datasources.read()
dashboard_info = dashboard.read()
print(datasources_info)
print(dashboard_info)

# python3-install
os.system("apt-get install -y python3-dev python3-pip libmysqlclient-dev")
os.system("apt-get install build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev")
os.system("pip3 install flask")
os.system("pip3 install request")
os.system("pip3 install requests")
os.system("pip3 install mysqlclient")

# grafana-install
'''
os.system("apt-get install -y apt-transport-https")
os.system("apt-get install -y software-properties-common wget")
os.system('add-apt-repository "deb https://packages.grafana.com/oss/deb stable main"')
os.system("wget -q -O - https://packages.grafana.com/gpg.key | apt-key add -")
os.system("apt-get update")
os.system("apt-get install grafana")
os.system("systemctl daemon-reload")
os.system("systemctl start grafana-server")
'''

print("wait for system check")
time.sleep(10)

while (not (create_grafana_datasource and create_grafana_dashboard))
    if (requests.get("http://127.0.0.1:3000").status_code == 200):
        try:
            if(requests.get("http://admin:admin@127.0.0.1:3000/api/datasources/name/librenms-cloud-mysql").status_code == 200)
                print("datasource exist")
                create_grafana_datasource = 1
        except:
            print("datasource not exist")
        try:
            if(requests.get("http://admin:admin@127.0.0.1:3000/api/dashboard/name/Librenms").status_code)
            print("dashboard exist")
            create_grafana_dashboard = 1
        except:
            print("dashboard not exist")
        
        if (create_grafana_datasource == 0):
            try:
                requests.post("http://admin:admin@127.0.0.1:3000/api/datasources", json=datasources_info)
                create_grafana_datasource = 1
            except:
                print("add datasource error")
        if (create_grafana_dashboard == 0):
            try:
                requests.post("http://admin:admin@127.0.0.1:3000/api/dashboard", json=dashboard_info)
                create_grafana_dashboard = 1
            except:
                print("add dashboard error")
    else:
        try:
            os.system("service grafana-server start")
        except:
            print("grafana_service error")
time.sleep(10)