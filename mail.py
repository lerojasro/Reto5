with open('TESLA.csv','r') as tesla:
    #filas =csv.reader(tesla)
    cont=0
    for l in tesla.readlines():
        cont+=1
        print(l,cont)
        #cont +=1
        #if cont>200:
        #    break
        
        
#print('cabecera',cabecera)
#print('prieros 5 resgistros')
#for i in range(6):
 # print(registros[i])
   ## lista=tesla.readline().split(',')
   # open=float(lista[1])
   # close=float(lista[4])
   # print(open-close)
    #break
    #if diferencia<0:
   #   comportamiento='SUBE'
   # elif diferencia>0:
    #  comportamiento='BAJO'
    #elif diferencia==0:
    #  comportamiento='ESTABLE'
    #print(comportamiento)
    #print(lista[2])
    