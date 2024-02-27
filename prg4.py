#write a program to print odd numbers between 1 to 10 numbers

def odd():
    odd_num=[i for i in range(11) if i%2!=0]
    print("odd numbers: ",odd_num)
odd()
