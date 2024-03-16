#Take n as an input from the user and write a program to print the table of n

n = int(input("enter a number: "))
for i in range (1, 11):
    print(n,"X",i,"=",n*i)