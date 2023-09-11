import random

x = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

sifre_uz = int(input("Şifre kaç harfli olsun?"))
sifre_adet = 10

for _ in range(sifre_adet):
    pasw = ""
    for i in range(sifre_uz):
        harf = random.choice(x)
        while i > 0 and harf == pasw[i - 1]:
            harf = random.choice(x)
        pasw += harf
    print(pasw)
