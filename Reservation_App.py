# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 21:38:20 2024

@author: mcing
"""

    
#I need to create a program that will be fore people who want to,
# book  a reservation at a restaurant.    
responses={}
active=True
while active:
    print(" Welcome to the Ballito!"+"\n")
    date=input("Please choose your reservation date!\n")
    d=str(int(date))+" " +"April 2024"
    guests=input("How many guests are you expecting?\n")
    g="Number of guests:" + str(int(guests))
    responses[d]=g
    continuation=input("Do you have any special requests? (yes/no)\n")
    if (continuation == "yes"):
        extra=input(" Please enter your special requests:\n")
        #Stores special requests with the date as the key
        responses[d]=(g,extra)
    elif continuation == "no":
        pass #this when we do not want any action to take place here.
    with open("Reservation_2.txt","a") as file:
     for date,details in responses.items():
         file.write(f"{date} :{details}\n")   
    repeat=input("Would you like to make another reservation? (yes/no)\n")
    if (repeat == "no"):
        print("Thank you for booking with us, see you on the"+ " "+ d +"\n")
        break
    elif  repeat == "yes":
       pass
 