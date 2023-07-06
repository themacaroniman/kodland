import random
character =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pass_length = int(input("Masukkan panjang password"))

password = ""
for i in range(pass_length):
    password += random.choice(character)
print(password)
