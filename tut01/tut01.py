 
    

x=int(input("Enter the number whose factorial is to be found \n"))


def factorial(x):
    if x==0: return 1
    if x==1: return 1
    return x*factorial(x-1)

print(factorial(x))