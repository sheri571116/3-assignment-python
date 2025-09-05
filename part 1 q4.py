def argument():
    n1=int(input("Enter first number :"))
    n2=int(input("Enter second number :"))
    n3=int(input("Enter third number :"))
    if n3 < n1 > n2 :
        print(f"{n1} is larger than {n2} and {n3} .")
    elif n3 < n2 > n1 :
        print(f"{n2} is larger than {n1} and {n3} .")
    else :
        print(f"{n3} is larger than {n1} and {n2} .")

argument()
                 
