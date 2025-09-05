def argument():
    a=int(input("Enter your age :"))
    if a < 18 :
        print("You are minor .")
    elif 60 > a > 18 :
        print("You are adult .")
    else :
        print("You are senior .")

argument()
