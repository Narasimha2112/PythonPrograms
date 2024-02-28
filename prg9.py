#write a program to check whether the given number is armstrong or not

def armstrong():
    num = eval(input("Enter a number: "))
    
    no_of_digits = len(str(num))
    
    sum = 0
    
    temp = num
    
    while temp > 0:
        digit = temp % 10
        sum += digit ** no_of_digits
        temp //= 10

    if num == sum:
       print(num,"is an Armstrong number")
    else:
       print(num,"is not an Armstrong number")

armstrong()
