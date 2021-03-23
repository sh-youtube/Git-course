from random import randint

def random():
    a = randint(1,99)
    gess = int(input())
    while gess != a:
        if gess > a:
            print("smaller")
        else:
            print("bigger")
        gess = int(input())
    print("thats right")