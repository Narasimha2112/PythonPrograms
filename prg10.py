#Write a program to check whether the number is prime or not 

num = eval(input("Enter a number: "))

def prime():
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                print(num,"is not a prime number")
                break
        else:
            print(num,"is a prime number")

prime()
