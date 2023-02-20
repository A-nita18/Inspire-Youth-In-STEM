# !/usr/bin/env/python3
#python programs to illustrate lists
#Name : Anita Sofia 
#Email : anitasofia254@gmail.com
#Date : 20th Feb 2023
#File : list-revised.py

myfavouritefruits = ["bananas","mangoes","kiwi","pawpaw","apples"]

#To access items in list use for loops

for fruit in myfavouritefruits:
    print(fruit)

#To get number of elements in list use len
print(len(fruit))

friends = ["Tungz","Mark","Adam","Tanui","Kev"]
print(friends)
friends[0] = "Rhoda"
print(friends)
print("-------------------------------------------------")

new_friends = friends.copy()
print(new_friends)

new_friends.sort()
print(new_friends)

new_friends.pop()
print(new_friends)