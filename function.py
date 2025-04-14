def obid():
    print("Kantrktni qanday tolasa boladi")

obid()


def obid1(ism):
    print(f"Salom, {ism} togo")

obid1("Obidjon")


def kvadrat(x):
    return x*x

natija = kvadrat(5)
print(natija)


def daraja(x, n=2):
    return x**n

print(daraja(3))
print(daraja(3,3))

def summa(*args):
    return sum(args)

print(summa(1,2,3))

def user_info(**kwargs):
    for key , value, in kwargs.items():
        print(f"{key}:{value}")

user_info(name= "Obid", age=24)


kvadrat = lambda x: x*x
print(kvadrat(4))

sonlar = [1, 2, 3, 4]
juft_sonlar = list(filter(lambda x: x%2 ==0, sonlar))
print(juft_sonlar)

#n = int(input("Obid togoni yoshi:"))
def faktorial(n):
    if n == 1:
        return 1
    else:
        return n*faktorial(n-1)

print(faktorial(5))

def katta_qil(matn):
    return matn.upper()

def salom_ber(func, isim):
    return func(f"Salom, {isim}")

print(salom_ber(katta_qil, "obodo togo"))


def multiplier(n):
    def inner(x):
        return x*n
    return inner

ikki_barobar = multiplier(2)
print(ikki_barobar(5))


sonlar = [1, 2, 3, 4]

kvadratlar = list(map(lambda x: x**2, sonlar))
print(kvadratlar)

juftlar = list(filter(lambda x: x % 2 == 0, sonlar))
print(juftlar)

from functools import reduce
yigindi = reduce(lambda x, y: x + y, sonlar)
print(yigindi)