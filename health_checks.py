import psutil
import shutil
import socket
import time
import os

sender = "automation@example.com"
recipient = "{}@example.com".format(os.environ.get('USER'))
body =  "Please check your system and resolve the issue as soon as possible."
subject_line = ['Error - CPU usage is over 80%', 'Error - Available disk space is less than 20%', 'Error - Available memory is less than 500MB', 'Error - localhost cannot be resolved to 127.0.0.1']

def health():

    res = psutil.cpu_percent(interval=0.1)

    if res > 80:
        message = emails.generate_email(sender, receiver, subject_line[0], body)
        emails.send_email(message)

    mem = psutil.virtual_memory()

    if mem.available < 524,288,000:
        message = emails.generate_email(sender, receiver, subject_line[2], body)
        emails.send_email(message)

    disk = psutil.disk_usage('/')
    disk = disk.percent
    if disk < 20:
        message = emails.generate_email(sender, receiver, subject_line[1], body)
        emails.send_email(message)

    HOST = "localhost"
    POST = "127.0.0.1"
    val = socket.gethostbyname(HOST)

    if val is not POST:
        message = emails.generate_email(sender, receiver, subject_line[3], body)
        emails.send_email(message)

    time.sleep(60)

while True:
    health()
