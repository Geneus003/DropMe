import random

print("Login")
name = str(input())
print ("Password")
pas = str(input())


def randomKey():
    for i in range(10):
        a = chr(random.randint(97,122))
        print (a)

randomKey()
SHA