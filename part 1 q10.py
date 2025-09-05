def argument():
    num= int(input("Enter the number :"))
    check = True

    if num <= 1 :
        check = False
    else:
        for i in range(2, num):
           if num % i == 0 : 
              check = False
              break
    if check :
            print(f"{num} is prime number .")
    else :
         print(f"{num} is not prime number .")

argument()
