#Write a program to check whether the given number is palindrome or not??

num = eval(input("Enter a number: "))

def palindrome():
    
    x=str(num)
    if(x==x[::-1]):
        print("The number",num,"is Palindrome.")
    else:
        print("The number",num,"is Not a palindrome")
        
palindrome()
