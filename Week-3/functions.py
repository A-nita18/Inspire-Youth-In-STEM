#!/usr/bin/env/python3
#python programs to understanding functions
#Name : Anita Sofia 
#Email : anitasofia254@gmail.com
#Date : 23rd Feb 2023
#File : functions.py

#Functions are blocks of code that are executed together
#Use keyword :def
def print_name():
    print("My name is Dokja")
    print("I am from Seoul")
    print("I am a 29 years old")
    print("My hobby is reading TWSA")

def add_numbers(num1, num2,):
    sum_num = num1 + num2
    print(sum_num)

def diff_numbers(num1, num2,):
    sub_num = num1 - num2
    print(sub_num)

def multiply_numbers(num1, num2,):
    prod_num = num1 * num2
    print(prod_num)

def divide_numbers(num1, num2,):
    quot_num = num1 / num2
    print(quot_num)

#Calling/Invoking the function
print_name()
add_numbers(4,5) #pass the parameters
diff_numbers(20,28)
multiply_numbers(36,4)
divide_numbers(18,3)