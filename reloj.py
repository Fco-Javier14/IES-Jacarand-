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





