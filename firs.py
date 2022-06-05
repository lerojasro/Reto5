
with open('TESLA.csv','r') as tesla:
    lista=tesla.readline().split(',')
    analisis=[]
    analisis.append(['Fecha analizada','Comportamiento de la accion','Ajuste Cuadratico de Close'])
    for i in range(253):
        lista=tesla.readline().split(',')
        diferencia=float(lista[4])-float(lista[1])
        comportamiento=str
        if diferencia<0:
            comportamiento='SUBE'
        elif diferencia>0:
            comportamiento='BAJA'
        elif diferencia==0:
            comportamiento='ESTABLE'
        Ajuste=float(lista[4])-float(lista[5])
        analisis.append([lista[0],comportamiento,Ajuste])
import csv
with open('analisis_datos.csv', 'w', newline='') as file:
    writter=csv.writer(file, delimiter='\t')
    writter.writerows(analisis)
    
   
    #lista=tesla.readline()
    #for i in tesla.readlines():
    #    cont+=1
        #lista=tesla.readline()
     #   print(i,cont)