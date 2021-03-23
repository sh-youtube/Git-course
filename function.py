from random import randint

#1
def random_number(num):
    a = randint(1,99)
    gess = num
    while gess != a:
        if gess > a:
            print("smaller")
        else:
            print("bigger")
        gess = int(input())
        
    print("thats right")

#2
def prime(num):
    x = num
    c = 0
    for i in range(1, x):
        if (x % i == 0):
            c+=1
    if (c == 1):
        print("prime")
    else:
        print("not prime")

#3
def bignum(num):
    x = num
    max_number = 0
    while x > -1:
        x = int(input())
        if max_number < x:
            max_number = x
    print(max_number)