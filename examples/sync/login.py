import stationhead

email = "email@gmail.com" #account email
password = "password" #account password

client = stationhead.Client()
info = client.login(email=email, password=password)
print(info.json)