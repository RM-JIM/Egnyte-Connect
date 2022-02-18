#!/usr/bin/python
import os

min_os = 10.15
current_os = os.system("sw_vers -productVersion")

if current_os >= min_os:
    print("Current installed OS is newer than Mojave, so is compatible for install")
    exit(0)
elif current_os < min_os:
    print("Current installed OS is older than Catalina, so is not compatible for Egnyte install")
    exit(1)
else:
    print("Error has occured, exiting script and install")
    exit(1)
