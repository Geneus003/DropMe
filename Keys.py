import random

def creatingKeys():

    n = 1000
    sieve = list(range(n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = False

    def NeD(t,e):
        a = True
        while a==True:
            z = random.randint(1,1000)
            if (z * e) % t == 1:
                a = False
        return z




    def NeT(t):
        a = True
        while a == True:
            z = random.randint(1,1000)
            z = sieve[z]
            if (z < t and z != False and t % z != 0):
                a = False

        return z

    def encrypt(n,e):
        print("Write MES")
        z = input(str())
        u = 0
        for i in range(0,len(z),1):
            u = u + ord(z[i])
            print(u)

        u = u ** e
        print(u)
        u = u % n

        return u

    def decrypt(c,d,n):
        m = c ** d
        m = m % n

        print(m)

        m = chr(m)

        return(m)

    prosArr = [3, 2, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

    randomPros = random.randint(0, 13)
    randPros = random.randint(0, 13)

    p = prosArr[randomPros]
    q = prosArr[randPros]

    n = p * q
    t = (p - 1) * (q - 1)

    e = NeT(t)
    d = NeD(t,e)


    print(p,q,n,t,e,d)

    c = encrypt(n,e)

    print(c)
    j = decrypt(c,d,n)

    print(j, "\n")





creatingKeys()