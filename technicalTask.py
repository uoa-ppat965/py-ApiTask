#technical task for Multiudes
#This code should use the github API extraction tool and takes the required info and print the number of pull requests
#Author: uoa-ppat965

#Required packages
import requests

#Printing ascii art
f = open('octocat.txt', 'r')
print(''.join([line for line in f]))
print(" ")

#Greetings
print("Kia Ora, welcome to the to this program!")
print(" ")
print("Let's process some Github data")
print(" ")

#Getting user inputs
owner = input("Who is the repo owner? ")
repo = input("What is the repo name? ")
print("Great sending the request query for " + owner, "and " + repo)
print(" ")
#Making the repo query
query = "https://api.github.com/repos/" + owner + "/" + repo + "/pulls"
r = requests.get(query) #goes to internet and grabs the stuff

#Checking if conditional is valid
if str(r)== "<Response [404]>":
    print("Sorry the repo or owner doesn't exist")
else: 
    stuff =r.links 

    #Checking if pull requests span multiple pages i.e > 30
    if len(stuff) == 0:
        number = len(r.json()) #pull requests if <30
    else:
        lastpageurl = str(stuff['last']['url']) 
        setofUrl = lastpageurl.partition("=") #splits url based on where "page=" is
        maxpage = setofUrl[2] #grabbing the number
        query = query + "?page=" + maxpage #creating lastpage url
        r = requests.get(query) 
        otherpages = 30*(int(maxpage)-1) #adds pull request to existing
        number = otherpages + len(r.json()) #final calculation

    print(" ")
    print("Data Found! The number of open pull requests is: ", number)
print(" ")
print("Great! Bye for now")
