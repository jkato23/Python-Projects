#! /usr/bin/env python3

import subprocess

svc = "sshd"
check_cmd = ["ps", "-C", svc]

service_check = subprocess.call(check_cmd)

if service_check == 0:
     print("The service is running.")
else:
     print("The service is NOT running.")
     print("Startint it...")
     subprocess.call(["systemctl", "start", "sshd"])
     subprocess.call(check_cmd)
