# !/usr/bin/env/python3
#python programs to illustrate bank tax
#Name : Anita Sofia 
#Email : anitasofia254@gmail.com
#Date : 17th Feb 2023
#File : bank.py

#Write a program that can calculate 16%
#ranging between 100k - 150k

#19% tax income is between 150k - 300k
#30% tax income is above 300k
#5% if income is less than 100k 

#print gross income , net income
income = int(input("Enter your income: "))
if income <= 100000:
    net_income = income*0.95
elif income < 150000:
    net_income = income*0.84
elif income < 300000:
    net_income = income*0.81
else:
    net_income = income*0.7

print("Gross income: " + str(income) + " Net income: " + str(net_income))

gross_income = input("What is your income? ")
tax_group_a = (int(gross_income) * 0.05)
tax_group_b = (int(gross_income) * 0.16)
tax_group_c = (int(gross_income) * 0.19)
tax_group_d = (int(gross_income) * 0.30)

if int(gross_income) < 100000:
    print("Gross income",gross_income)
    print("Net income",int(gross_income) - tax_group_a)
elif int(gross_income) < 150000:
    print("Gross income",gross_income)
    print("Net income",int(gross_income) - tax_group_b)
elif int(gross_income) < 300000:
    print("Gross income",gross_income)
    print("Net income",int(gross_income) - tax_group_c)
elif int(gross_income) > 300000:
    print("Gross income",gross_income)
    print("Net income",gross_income - tax_group_d)
