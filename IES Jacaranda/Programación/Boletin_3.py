#Ejercicio 1
numero = int(input("Introduzca un número:  "))
if numero % 2 == 0 or numero == 0:
    print("El número introducido es par")
else:
    print("El número introducido es impar")


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


#Ejercicio 4
edad = int(input("Introduzca su edad:  "))
if 0 <= edad <= 6:
    print("Educación infantil")
elif 7 <= edad <= 11:
    print("Educación primaria")
elif 12 <= edad <= 16:
    print("Educación secundaria obligatoria")
elif 16 < edad <= 65:
    print("Enseñanza post-obligatoria")
else:
    print("Se ha producido un error en el programa")


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

elif letra == "i" or letra == "I":
    print(f"La tercera vocal {letra}")

elif letra == "o"  or letra == "O":
    print(f"La cuarta vocal {letra}")
 
elif letra == "u" or letra == "U":
    print(f"La quinta vocal {letra}")

else:
    print("El carácter introducido no es una vocal ")


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


#Ejercicio 9
dia_semana = str(input("Introduzca un día de la semana:  "))

if dia_semana == "1":
    print("Lunes")

elif dia_semana == "2":
    print("Martes")

elif dia_semana == "3":
    print("Miércoles")

elif dia_semana == "4":
    print("Jueves")

elif dia_semana == "5":
    print("Viernes")

elif dia_semana == "6":
    print("Sábado")

elif dia_semana == "7":
    print("Domingo")

else:
    print("Error")


#Ejercicio 10
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
        elif minutos_1 < minutos_2:
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


#Ejercicio 12
dia = int(input("¿Qué día de la semanas es?:  "))
vacaciones = str(input("¿Estás de vaciones?: (Si/No) "))

if 1<= dia <= 5 and vacaciones == "No":
    print("La alarma suena a las a las 7:00")

elif 6<= dia <= 7 and vacaciones == "No":
    print("La alarma suena a las 10:00")

elif vacaciones == "Si":
    print("La alarma está apagada")

else:
    print("Error")


#Ejercicio 13

caracter = str(input("Introduce un carácter:  "))
numero_1 = int(input("Introduce un número:  "))
numero_2 = int(input("Introduce otro número:  "))

if caracter == "==" or caracter == "!=" or caracter == "<=" or caracter == ">=" or caracter == "<" or caracter == ">" or caracter == "+" or caracter == "-" or caracter == "/" or caracter == "%" or caracter == "*" or caracter == "**":
    calculo = numero_1,caracter,numero_2
    print(calculo)

else:
    print(f"{numero_1} {caracter} {numero_2}")


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


#Ejercicio 15
day = int(input("Introduce un día:  "))
month = int(input("Introduce un mes:  "))
year = int(input("Introduce un año:  "))

bisiesto = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if bisiesto:
    print(f"El año {year} es bisiesto")

else:
    print(f"El año {year} no es bisiesto")

fecha_valida = False

if year > 0 and 1 <= month <= 12:
    if month == 2:
        if(bisiesto and 1 <= day <= 29) or (not bisiesto and 1 <= day <= 28):
            fecha_valida = True

    elif month == 4 or month == 6 or month == 9 or month == 11:
        if 1 <= day <= 30:
            fecha_valida = True

    else:
        if 1 <= day <= 31:
            fecha_valida = True


if fecha_valida:
    print(f"La fecha {day}/{month}/{year} existe, por lo tanto es válida")

else:
    print(f"La fecha {day}/{month}/{year} no existe, por lo tanto no es válida")
        

#Ejercicio 16
base = float(input("Base:  "))
exponente = int(input("Exponente:  "))

if exponente > 0:
    print(base ** exponente)

elif exponente == 0:
    print(1)

elif exponente != 0:
    print(1/ base ** -exponente)

else:
    print("Error")


#Ejercicio 17
a = float(input("Lado 1:  "))
b = float(input("Lado 2:  "))
c = float(input("Lado 3:  "))

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print("Equilátero")
    elif a == b or a == c or b == c:
        print("Isósceles")
    else:
        print("Escaleno")

    hipotenusa = max(a,b,c) # max se utiliza para sacar el máximo de los valores agrupados
    if a**2 + b**2 + c**2 == 2 * hipotenusa**2:
        print("También es rectángulo")

else:
    print("No forman un triángulo válido")


#Ejercicio 18

n1 = float(input("Primer número:  "))
n2 = float(input("Segundo número:  "))

distancia = n1 - n2
if distancia < 0:
    distancia= -distancia

print("Distancia:", distancia)


#Ejercicio 19
alumnos = int(input("Número de alumnos:  "))

if alumnos >= 100:
    costo_alumno = 65
    total = costo_alumno * alumnos
elif alumnos >= 50:
    costo_alumno = 70
    total = costo_alumno * alumnos
elif alumnos >= 30:
    costo_alumno = 95
    total = costo_alumno * alumnos
else:
    total = 2500
    costo_alumno = total/alumnos

print(f"Pago a la compañía: {total} euros")
print(f"Cada alumno paga: {costo_alumno} euros")


#Ejercicio 20
minutos = int(input("Duración en minutos:  "))
dia = str(input("Dia de la semana:  "))
turno = str(input("Turno de la semana:  "))

if minutos <= 10:
    coste = minutos * 0.66
elif minutos <= 13:
    coste = 6.60 + (minutos - 10) * 0.50
elif minutos <= 15:
    coste = 8.10 + (minutos - 13) * 0.45
else:
    coste = 9.00 + (minutos - 15) * 0.35

if dia == "domingo":
    impuesto = 0.03
elif turno == "mañana":
    impuesto = 0.15
else:
    impuesto = 0.10

print(f"Total a pagar: {coste * (1 + impuesto)} euros")


#Ejercicio 21
mates = float(input("Nota Match:  "))
ingles = float(input("Nota English:  "))
prog = float(input("Nota Programming:  "))
asistencia = float(input("Asistencia (%):  "))

media = (mates + ingles + prog)

if mates < 60 or ingles < 60 or prog < 60:
    print("Rechazado, no aprueba los tres exámenes")

elif media >= 85:
    print("Admitido con beca")

elif media >= 70 and asistencia >= 75:
    print("Admitido sin beca")

elif 60 <= media < 70:
    print("Lista de espera")

else:
    print("Rechazado")
    

    