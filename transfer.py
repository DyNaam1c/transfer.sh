import requests

loc = input("Enter file name: ")
transfer = "https://transfer.sh/"
with open(loc, "rb") as f:
    up = {"file": (f)}
    req = requests.post(transfer, files=up)
link = req.text.strip()
print('---------------------------------')
print("There is your url:\n" + link.replace(transfer, transfer + "get/"))
