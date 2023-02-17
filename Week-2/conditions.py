# !/usr/bin/env/python3
#python programs to illustrate conditions
#Name : Anita Sofia 
#Email : anitasofia254@gmail.com
#Date : 17th Feb 2023
#File : conditions.py

age = 16
gender = "male"

if(age < 18):
    print("You are still young ")
else:
    print("You should get an ID")

#compound / multiple conditions

if((age < 30) & (gender == "male")):
    print("You qualify to join")
else:
    print("Sorry, you cannot join")

fav_colour = "grey"
age = 23 

if((fav_colour == "grey") | (age <= 20)):
    print("Happy birthday to you")
else:
    print("No birthday present for you")
    
