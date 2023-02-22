#!/usr/bin/env/python3
#python programs to create lists
#Name : Anita Sofia 
#Email : anitasofia254@gmail.com
#Date : 21st Feb 2023
#File : assignment.py

#Create an empty list of favourite musicians.
#Using for loop add 5 new musicans.
#Copy the list to a new list called celebs.
#Sort the list
#Pop out two celebs from the list
#Count the remaining number of celebs

my_favourite_musicians = []
n = int(input("Enter the number of musicians: "))
for i in range(0,n):
    element = input("Enter the musicians: ")
    my_favourite_musicians.append(element)

print(my_favourite_musicians)

celebs = my_favourite_musicians.copy()
print(celebs)

celebs.sort()
print(celebs)

celebs.pop()
celebs.pop()

print(celebs)
print(len(celebs))