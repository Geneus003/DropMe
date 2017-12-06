class Main:

    def __init__(self,b):
        self.b = b

c = int(input().split())
a = Main(c)


def snow(a):

    if a.b % 2 == 0:
        print("Even")
    else:
        print("Odd")

snow(a)