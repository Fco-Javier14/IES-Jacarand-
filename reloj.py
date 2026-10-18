hora = int(input("Hora:  ")) 
minuto = int(input("Minutos:  "))
segundo = int(input("Segundos:  "))


while not (0 <= hora <=23 and 0 <= minuto <= 59 and 0 <= segundo <= 59):
        hora = int(input("Hora:  ")) 
        minuto = int(input("Minutos:  "))
        segundo = int(input("Segundos:  "))
        

if  hora == 23 and minuto == 59 and segundo == 59:
        print("0:0:0")
elif hora < 23 and minuto== 59 and segundo== 59:
        print(f"{hora+1}:0:0")
elif hora <= 23 and minuto < 59 and segundo == 59:
        print(f"{hora}:{minuto+1}:0")    
else:
        print(f"{hora}:{minuto}:{segundo+1}")



"""
En este trabajo he logrado poner en práctica cada concepto aprendido en las primeras semanas. He logrado crear un programa que simula el funcionamiento de un reloj digital al hacer que, cuando se introduzca las horas, minutos y segundos , salga reflejado en el terminal la hora del reloj cuando pasa +1 segundo. 
He utilizado todo lo que he aprendido hasta el momento: he colocado las tres variables del programa (hora, minutos y segundos) con sus respectivos input para introducir los valores , los cuáles son enteros (int), en el terminal; he puesto un bucle "while" con not para dejar claro que cuando no cumplan alguno de los
requisitos el programa seguirá pidiendo los datos hasta que sean correctos; y posteriormente he puesto condicionales para indicar las posibilidades que hay y lo que tiene que salir reflejado en cada caso.
"""

