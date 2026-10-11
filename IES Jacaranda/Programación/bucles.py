"""
for i in range(1,10,2):
    print(i,"Hola")

for  i in range(3,16,2):
    print(i, "Adios")


#Ejercicio Tabla multiplicar

numero = int(input("Introduce un número:  "))

for i in range(1):
    print(i,(numero * 1) , (numero * 2) , (numero * 3) , (numero * 4) , (numero * 5) , (numero * 6), (numero * 7 ), (numero * 8) , (numero * 9 ), (numero * 10))

#FICHA 4 

#Ejercicio 2
numero = int(input("Introduce un número:  "))
acumulador = 0
for i in range(0,11):
    acumulador+= numero
    print(acumulador)


numero = int(input("Introduce un número:  "))

for i in range(1,11):
    #print( i * numero)
    print(f"{numero} * {i} = {numero * i}")


numero = int(input("Introduce un número:  "))

for i in range(1,11):
   #print( i ** numero)
    print(f"{numero} ** {i} = {numero ** i}")



numero = 3
while numero < 15:
    print("Hola")
    numero+= 1


a = 1
while a < 5:
   print(a)
   a+= 1

for i in range(10 ,0, -1 ):
    #print(i)

 a = 10
while a >= 0:
    print(a)
    a-=1 
"""
a = 0
while a < 11:
   print(a)
   a+=1 



    


    