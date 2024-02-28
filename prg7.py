#Write a program to print the number in reverse of user entered number

num = eval(input("enter a number: "))

def rev():
    
    x=str(num)
    print("The reverse number is",x[::-1])
rev()
