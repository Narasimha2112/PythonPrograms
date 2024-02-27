#write a program to find factorial of given numbers

num = eval(input("Enter a number: "))

def factorial():
    
    fact = 1
    
    if num<0:
        print("Sorry!, The Factorial doesnot exits for negative numbers.")
    elif num==0:
        print("The Factorial of 0 is 1")
    else:
        for i in range(1,num+1):
            fact = fact * i
        print("The Factorial of given number",num,"is :",fact)
factorial()
