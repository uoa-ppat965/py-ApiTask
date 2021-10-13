#technical task for Multiudes
#This code should use the github API extraction tool and takes the required info and print the number of pull requests
#Author: uoa-ppat965

#Required packages
import requests
from requests.models import parse_url
from requests.packages.urllib3.util import url

print("Kia Ora, welcome to the to this program!")

print("Let's process some Github data")
print(" ")
owner = input("Who is the repo owner? ")

repo = input("What is the repo name? ")
query = "https://api.github.com/repos/" + owner + "/" + repo + "/pulls"
print("Great sending a query for open Pull requests")
r = requests.get(query) #goest to internet and grabs the stuff
stuff =r.links 
lastpageurl = str(stuff['last']['url'])
setofUrl = lastpageurl.partition("=")
maxpage = setofUrl[2]

query = query + "?page=" + maxpage
r = requests.get(query) #goes to internet and grabs the stuff
otherpages = 30*(int(maxpage)-1)
number = otherpages + len(r.json())
print(" ")
print("Data Found! The number of open PRS is: ", number)
print(" ")
print("Great! Bye for now")
