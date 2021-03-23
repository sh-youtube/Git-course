from random import randint

#1
def random(num):
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