from function import *

h = True

hi = '''
hi.welcome to git course's game.Choose your desired game from the following options:
1.random number
2.prime
3.bigest number
4.exit
 '''
print(hi)

x = int(input("your choice: "))

while h == True:
    if x == 1:
        a = int(input("What number is in my mind: "))
        random_number(a)
