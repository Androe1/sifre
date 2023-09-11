import random

x = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

sifre_uz = int(input("Şifre kaç harfli olsun?"))

pasw = ""

for i in range(sifre_uz):
    pasw += random.choice(x)

print(pasw)
