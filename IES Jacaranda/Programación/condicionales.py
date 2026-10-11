"""
saldo = 500

if saldo < 1000:
    print("Saldo isuficiente")
    print("Deberías ponerte a trabajar")
print("Fin del programa")



encender_aire, encender_ventilador, encender_calefaccion = False, False, False
temperatura = 15

if temperatura <= 15:
    encender_calefaccion = True
    print("Calentando habitación")

elif temperatura <= 25:
    encender_ventilador = True
    print("Ventilando habitación")

else :
    encender_aire = True
    print("Refrigerando habitación")



FICHA 3

#Ejercicio 2
numero_1 = int(input("Introduce un número:  "))
numero_2 = int(input("Introduce otro número:  "))
if numero_1 == numero_2:
    print(f"{numero_1} y {numero_2} son iguales")

elif numero_1 < numero_2:
    print(f"{numero_1} es menor que {numero_2}")

else:
    print(f"{numero_1} es mayor que {numero_2}")


#Ejercicio 3
numero_x = int(input("Introduzca un número:  "))
if numero_x % 5 == 0 and numero_x % 7 == 0:
    print(f"El número {numero_x} es múltiplo de 5 y de 7")

elif numero_x % 5 == 0:
    print(f"El número {numero_x} es múltiplo de 5")

elif numero_x % 7 == 0:
    print(f"El número {numero_x} es múltiplo de 7")

else:
    print()
numeros_superiores+= "  " + str(numero_1)


#Ejercicio 5
numero_1 = int(input("1.Introduce un número:  "))
numero_2 = int(input("2.Introduce otro número:  "))
numero_3 = int(input("3.Introduce otro número:  "))
numero_4 = int(input("4.Introduce otro número:  "))

media = ((numero_1+numero_2+numero_3+numero_4 )/4)
contador = 0
numeros_superiores = " "

if numero_1 > media:
    contador+= 1
    numeros_superiores+= " "+str(numero_1)
    #contador=contador+1

if numero_2 > media:
    contador+= 1
    numeros_superiores+= " "+str(numero_2)

if numero_3 > media:
    contador+= 1
    numeros_superiores+= " "+str(numero_3)

if numero_4 > media:
    contador+= 1
    numeros_superiores+= " "+str(numero_4)

  

print(f"La media es de {media} y hay {contador} números superiores a la media:{numeros_superiores}")


#Ejercicio 6
numero_1 = int(input("Introduzca un número:  "))
numero_2 = int(input("Introduzca otro número:  "))

if numero_1 % numero_2 == 0 or numero_2 % numero_1 == 0:
    print(f"Los números {numero_1} y {numero_2} son múltiplos entre sí")

else :
    print(f"Los números {numero_1} y {numero_2} no son múltiplos entre sí  ")


#Ejercicio 7
letra = str(input("Introduzca un carácter:  "))

if letra == "a" or letra == "A":
    print(f"La primera vocal {letra}")

elif letra == "e" or letra == "E":
    print(f"La segunda vocal {letra}")

else:
    print("El carácter introducido no es una vocal ")


#Ejercicio 10 (Bucle anidado)
hora_1 = int(input("Hora 1:  "))
minutos_1 = int(input("Minutos 1:  "))
segundos_1 = int(input("Segundos 1:  "))

hora_2 = int(input("Hora 2:  "))
minutos_2 = int(input("Minutos 2:  "))
segundos_2 = int(input("Segundos 2:  "))

if  0 <= hora_1 <= 23 and  0 <= hora_2 <= 23 and 0 <= minutos_1 <= 59 and  0 <= minutos_2 <= 59 and  0 <= segundos_1 <= 59 and 0 <= segundos_2 <= 59:
    if hora_1 > hora_2:
     print("Hora 1 es mayor")
    else:
        if minutos_1 > minutos_2:
            print("Hora 1 es mayor")
        elif minutos_1 > minutos_2:
            print("Hora 2 es mayor")
        else:
            if segundos_1 > segundos_2:
                print("Hora 1 es mayor")
            elif segundos_1 < segundos_2:
                print("Hora 2 es mayor")
            else:
                print("Las horas son iguales")
else:
    print("Los datos son erróneos")


#Ejercicio 8
edad = int(input("Indique su edad:  "))
estado_civil = str(input("Indique su estado civil (S/C/V/D):  "))


if 0 < edad < 35:
    if estado_civil =="S" or estado_civil== "D":
        print("Retención del 12%")
    elif estado_civil == "V" or estado_civil == "C":
        print("Retención del 11.3%")
elif edad >= 50:
    print("Retención del 8.5%")
elif edad >=35:
    print("Retención del 10.5%")

"""

#Ejercicio 11
customer = str(input("Student/Regular/Other:  "))
amount = float(input("Introduzca el importe:  "))
discount = 0

if customer == "student":
    if amount >= 100:
       discount = 15
    else:
        discount = 10
elif customer == "regular" and amount >= 200:
    discount = 12
else:
    discount = 5

print(amount*(1-discount/100), discount)




#Ejercicio 14
print("Introduce las monedas que tienes de cada tipo:  ")

m2 = int(input("De 2 euros:  "))
m1 = int(input("De 1 euro:  "))
m50_c =int(input("De 50 céntimos:  "))
m20_c = int(input("De 20 céntimos:  "))
m10_c = int(input("De 10 céntimos:  "))
m5_c = int(input("De 5 céntimos:  "))
m2_c = int(input("De 2 céntimos:  "))
m1_c = int(input("De 1 céntimo:  "))

total_centimos = (m2 * 200) + (m1 * 100) + (m50_c * 50) + (m20_c * 20) + (m10_c * 10) + (m5_c * 5) + (m2_c * 2) + (m1_c * 1)
total_euros = total_centimos/100

print(f"El dinero total que tienes es: {total_euros} euros")
