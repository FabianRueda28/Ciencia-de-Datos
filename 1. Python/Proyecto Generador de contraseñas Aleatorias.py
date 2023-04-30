import random as r

print(' Bienvenido a tu Generador de contraseñas aleatorias')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+'

numero = input(' Cuantas contraseñas quieres generar? ')
numero = int(numero)

rango = input(' Cuantos caracteres quieres que tenga cada contraseña? ') 
rango = int(rango) 

print(' Aquí tienes tus contraseñas: ') 

for pwd in range(numero):
    passwords = ''
    for c in range(rango):
        passwords += r.choice(chars)
    print(passwords)






