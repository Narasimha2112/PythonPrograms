#Write a program to print multiplication table of user enetered number

def table():
    num = eval(input("enter a number: "))
    for i in range(1,11):
        print(num," * ",i," = ",num*i)
table()
