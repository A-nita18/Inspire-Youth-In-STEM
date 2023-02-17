# !/usr/bin/env/python3
#python programs to illustrate strings
#Name : Anita Sofia 
#Email : anitasofia254@gmail.com
#Date : 17th Feb 2023
#File : strings.py

poem = ''' This is a poem about nothing
 It is funny that people laugh about nothing
'''
print(poem)
print(len(poem))

f_name = "Dokja "
s_name = "Kim"

full_name = f_name + s_name
age = 25 # years
print("My name is " + full_name + " and I am " + str(age) + " years old")
print("My name is {} and I am {} years old".format(full_name, str(age)))

print("Hello from Dokja \n How are you?\n I am fine")
print("Hello from Dokja \t How are you?\t I am fine")