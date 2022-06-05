import csv
cabecera=[]
registros=[]
with open('TESLA.csv','r') as csvfile:
    lector =csv.reader(csvfile)
    
    #para sacar la cabecera usamos la función next
    cabecera=next(lector)
    
    #extraemos cada registro con un ciclo for
    for fila in lector:
        registros.append(fila)
    
    print('total de registros encontrados', lector.line_num)
print('cabecera: ',cabecera)
print('primeros 5 registros')
for i in range(253):
    print(registros[i][0])