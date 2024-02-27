#Write a program to print sum of user entered 10 numbers

sum=0
for i in range(1,11):
    x=eval(input("Enter a  number: "))
    sum=sum+x
print("The sum of 10 numbers is ",sum)
