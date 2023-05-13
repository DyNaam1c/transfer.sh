import requests
import pyperclip

loc = input("Enter file name: ")
transfer = "https://transfer.sh/"
with open(loc, "rb") as f:
    up = {"file": (f)}
    req = requests.post(transfer, files=up)
link = req.text.strip().replace(transfer, transfer + "get/")
pyperclip.copy(link)
print('---------------------------------')
print("Saved to your clipboard ;):\n" + link)
