from bs4 import BeautifulSoup
import os
import datetime
try:
    f = open(str(datetime.datetime.utcnow().date()))
except FileNotFoundError:
    with open(str(datetime.datetime.utcnow().date()), "w") as f:
        f.write(f"IP Address, VirtualAccount")
for file in os.listdir("searchfiles"):
    with open('searchfiles/'+file) as f:
        soup = BeautifulSoup(f.read(), "xml")
    logs = soup.findAll("log")
    with open("searchfrom.txt") as f:
        lines = f.readlines()
        for l in logs:
            log = l.event.session
            for ip in lines:
                ip = ip.strip()
                if ip in log["remoteAddress"]:
                    with open(str(datetime.datetime.utcnow().date()), "a") as f:
                        f.write(f"\n{ip}, {log['virtualAccount']}")
