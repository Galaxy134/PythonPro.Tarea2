import random
import time
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
contraseña = ""
longitud = int(input("Introduzca la longitud de su contraseña:"))
for i in range(longitud):
    contraseña += random.choice(caracteres)
print("Generando contraseña...")
time.sleep(2)
print(contraseña)
