
with open('TESLA.csv','r') as tesla:
    lista=tesla.readline().split(',')
    analisis=[]
    analisis.append(['Fecha analizada','Comportamiento de la accion','Ajuste Cuadratico de Close'])
    yeison={'date_lowest_open':'dia','lowest_open':200000,'date_highest_close':'dia','highest_close':0,'mean_volume':0,'date_greatest_difference':'day','greatest_difference':0}
    apertura=10000
    dif=0
    cierre=0
    cont=0
    suma=0
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
        if float(lista[1])<apertura:
            apertura=float(lista[1])
            yeison['date_lowest_open']=lista[0]
            yeison['lowest_open']=int(apertura)
        if float(lista[4])>cierre:
            cierre=float(lista[4])
            yeison['date_highest_close']=lista[0]
            yeison['highest_close']=int(cierre)
        if abs(float(lista[3])-float(lista[2]))>dif:
            dif=abs(float(lista[3])-float(lista[2]))
            yeison['date_greatest_difference']=lista[0]
            yeison['greatest_difference']=dif
        cont+=1
        suma+=float(lista[6])
    yeison['mean_volume']=(suma/cont)
            
    
import csv
with open('analisis_datos.csv', 'w', newline='') as file:
    writter=csv.writer(file, delimiter='\t')
    writter.writerows(analisis)
#print(yeison)
import json
with open('detalles.json','w') as archivo:
    json.dump(yeison,archivo)





