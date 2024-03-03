#Write a program to print numbers between 1 to 50 which is divisible by 3 but not by 7

div_by_3=[i for i in range(1,51) if i%3==0 and i%7!=0]

print(div_by_3)
