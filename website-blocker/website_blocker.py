import time
from datetime import datetime as dt

host_temp = "hosts"
hosts_path="/etc/hosts" # not using this as dont want to play around security issues
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "gmail.com", "mail.google.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print (" Working hours... ")
        with open(host_temp, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+ " " +website+"\n")
    else:
        with open(host_temp, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate()
        print("fun hours")
    time.sleep(5)
