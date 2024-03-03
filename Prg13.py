#write a program to print fibonacci series upto user entered number

num = eval(input("enter a number: "))

a, b = 0, 1

for _ in range(1,num):
    print(a, end=' ')
    a, b = b, a + b
