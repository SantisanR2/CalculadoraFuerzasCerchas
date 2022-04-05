from cmath import sin
import math
from re import X
from xml.etree.ElementTree import tostring

tipo_cercha = ""
distancia_horizontal = 0
distancia_vertical = 0
resistencia_soporte = 0
T = dict()
angulo = 0
F = dict()
n = 0
sen=0
cos=0


distancia_horizontal = 3
distancia_vertical = 4
n = 12
T = dict()
for i in range(2,n):
    T[i]=0
T[2]=12
T[4]=20
angulo = math.atan(distancia_vertical/distancia_horizontal)
sen=math.sin(angulo)
cos=math.cos(angulo)
F = dict()



def initialize(pN,pTipoCercha,pDistanciaHorizontal,pDistanciaVertical,pT):
    tipo_cercha = pTipoCercha
    distancia_horizontal = pDistanciaHorizontal
    distancia_vertical = pDistanciaVertical
    T = pT
    n = pN
    angulo = math.atan(distancia_vertical/distancia_horizontal)
    sen=math.sin(angulo)
    cos=math.cos(angulo)


def calcularFuerzasWarren(n,distancia_horizontal,T,F,sen,cos):
    D=dict()
    x=distancia_horizontal/2
    resistencia_soporte=0
    for i in range(n-1, 0, -1):
        D[i]=x
        x=x+(distancia_horizontal/2)
        
        
    
    for i in range(2,n):
        resistencia_soporte=resistencia_soporte+D[i]*T[i]
    
    resistencia_soporte=resistencia_soporte/D[1]
    print(str(resistencia_soporte))

    F["1-2"]=(resistencia_soporte/sen)
    F["1-3"]=(F["1-2"]*cos)

    F["2-3"]=(F["1-2"]*sen-T[2])/sen
    F["2-4"]=cos*(F["1-2"]+F["2-3"])


    for i in range(3,n-2):
        if(i%2 == 1):
            F[str(i)+"-"+str(i+1)]=(F[str(i-1)+"-"+str(i)]+T[i])/sen
            F[str(i)+"-"+str(i+2)]=F[str(i-2)+"-"+str(i)]+F[str(i-1)+"-"+str(i)]*cos-F[str(i)+"-"+str(i+1)]*cos
        else:
            F[str(i)+"-"+str(i+1)]=(F[str(i-1)+"-"+str(i)]-T[i])/sen
            F[str(i)+"-"+str(i+2)]=-F[str(i-2)+"-"+str(i)]-F[str(i-1)+"-"+str(i)]*cos-F[str(i)+"-"+str(i+1)]*cos

    F[str(n-1)+"-"+str(n)]=1/2*(F[str(n-3)+"-"+str(n-1)]/cos+T[n-1]/sen)
    F[str(n-2)+"-"+str(n-1)]=(F[str(n-1)+"-"+str(n)]*sen + T[n-1])/sen
    
    if(n==5):
        F[str(n-2)+"-"+str(n-1)]=(-F[str(n-3)+"-"+str(n-2)]*sen + T[n-2])/sen
        F[str(n-2)+"-"+str(n)]=(F[str(n-4)+"-"+str(n-2)] + F[str(n-3)+"-"+str(n-2)]*cos - F[str(n-2)+"-"+str(n-1)]*cos)

    F["n"]=F[str(n-1)+"-"+str(n)]*sen
def calcularFuerzasHowe(n,distancia_horizontal,T,F,sen,cos):
    D=dict()
    x=distancia_horizontal
    resistencia_soporte=0
    for i in range(n-1, 1, -2):
        
        D[i]=x
        D[i-1]=x
        print(str(D[i]))
        x=x+(distancia_horizontal)
    D[1]=x
    D[n]=0
    print(str(D[1]))

    for i in range(2,n):
        resistencia_soporte=resistencia_soporte+D[i]*T[i]
    
   
    resistencia_soporte=resistencia_soporte/D[1]

#Balance nodo 1
print(str(sen))
F["1-2"]=-resistencia_soporte/sen
F["1-3"]=-(F["1-2"])

#Balance nodo 2
F["2-4"]=-(F["1-2"])*cos
F["2-3"]= (F["1-2"])*sen - T[2]

#Primer for

for i in range(2, int(n/2)-1):
    if (i%2==1):
        F[str(i)+"-"+str(i+1)]=(F[str(i-1)+"-"+str(i)]+T[i])/sen
        F[str(i)+"-"+str(i+2)]=-(F[str(i-2)+"-"+str(i)]+F[str(i)+"-"+str(i+1)]*cos-F[str(i)+"-"+str(i+1)]*cos)
    else:
        F[str(i)+"-"+str(i+1)]=(F[str(i-1)+"-"+str(i)]*sen - T[i])
        F[str(i)+"-"+str(i+2)]=-(F[str(i-2)+"-"+str(i)]+F[str(i-1)+"-"+str(i)]*cos)

i = n/2 + 1
F[str(i)+"-"+str(i+2)] = -F[str(i)+"-"+str(i+2)]
F[str(i-1)+"-"+str(i)]=-T[i]

i = n/2
F[str(i)+"-"+str(i+3)]=(-F[str(i)+"-"+str((i+1))]+ F[str(i-1)+"-"+str(i)]*sen -T[i])/(sen)
F[str(i)+"-"+str(i+2)]=-(F[str(i-2)+"-"+str((i))]+ F[str(i-1)+"-"+str(i)]*cos + F[str(i)+"-"+str(i+3)]*cos)

#Segundo for

for i in range(int(n/2) + 2, n - 2):
    if(i==n/2 + 2):
        F[str(i)+"-"+str(i+3)]=(F[str(i)+"-"+str(i+1)] + T[i])/(sen)
        F[str(i)+"-"+str(i+2)]=-(F[str(i-2)+"-"+str(i)] + F[str(i)+"-"+str(i+3)])
    elif(i==n-3):
        F[str(i-1)+"-"+str(i)] = F[str(i-3)+"-"+str(i)]*sen + T[i]
    else:
        F[str(i-1)+"-"+str(i)] = F[str(i-3)+"-"+str(i)]*sen + T[i]
        F[str(i+1)+"-"+str(i+4)] = (F[str(i+1)+"-"+str(i+2)] + T[i+1])/sen
        F[str(i+1)+"-"+str(i+3)] =-(F[str(i-1)+"-"+str(i+1)] + F[str(i+1)+"-"+str(i+4)])
        F[str(i)+"-"+str(i+2)] = - (F[str(i-2)+"-"+str(i)] + F[str(i-3)+"-"+str(i)]*cos)
    
#Vida complicada
i = n - 2
F[str(i)+"-"+str(n)] = -(F[str(i-2)+"-"+str(i)])/cos
F[str(i)+"-"+str(i+1)] = -(F[str(i)+"-"+str(n)]*sen + T[i])
F[str(i-1)+"-"+str(i+1)] = -(F[str(i-3)+"-"+str(i-1)] + F[str(i-4)+"-"+str(i-1)]*cos)
F["n"] = F[str(i)+"-"+str(n)]*sen
# de n -1 a n para después


        

distancia_horizontal = 3
distancia_vertical = 4
n = 12
T = dict()
for i in range(2,n):
    T[i]=0
T[2]=12
T[4]=20
angulo = math.atan(distancia_vertical/distancia_horizontal)
sen=math.sin(angulo)
cos=math.cos(angulo)
F = dict()

calcularFuerzasHowe(n,distancia_horizontal,T,F,sen,cos)
#calcularFuerzasWarren(n,distancia_horizontal,T,F,sen,cos)
'''for i in range(1,n):
    print("F["+str(i)+"-"+str(i+1)+"]= "+str(F[str(i)+"-"+str(i+1)]))
    print("F["+str(i+1)+"-"+str(i)+"]= "+str(-F[str(i)+"-"+str(i+1)]))

print("------------")

for i in range(1,n-1):
    print("F["+str(i)+"-"+str(i+2)+"]= "+str(F[str(i)+"-"+str(i+2)]))
    print("F["+str(i+2)+"-"+str(i)+"]= "+str(-F[str(i)+"-"+str(i+2)]))

print("F["+str(n)+"]= "+str(F["n"]))'''




