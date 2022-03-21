from cmath import sin
import math
from xml.etree.ElementTree import tostring

nodos = list()
tipo_cercha = ""
distancia_horizontal = 0
distancia_vertical = 0
tipo_soporte = ""
resistencia_soporte = 0
tension_nodo = dict()
angulo = 0
fuerzas_nodo = dict()
n = 0

def initialize(pNodos,pTipoCercha,pDistanciaHorizontal,pDistanciaVertical,pTipoSoporte,pResistenciaSoporte,pTensionNodo):
    nodos = pNodos
    tipo_cercha = pTipoCercha
    distancia_horizontal = pDistanciaHorizontal
    distancia_vertical = pDistanciaVertical
    tipo_soporte = pTipoSoporte
    resistencia_soporte = pResistenciaSoporte
    tension_nodo = pTensionNodo
    n = len(nodos)
    angulo = math.atan(distancia_vertical/distancia_horizontal)

def calcularFuerzas():
    for i in nodos:
        if(i==1):
            fuerzas_nodo["1-2"] = -tension_nodo[1]/math.sin(angulo)
            fuerzas_nodo["1-3"] = -fuerzas_nodo[1-2]*math.cos(angulo)
        elif(i==n):
            fuerzas_nodo[str(n-2)+"-"+str(n)] = -tension_nodo[2]/math.sin(angulo)
            fuerzas_nodo[str(n-1)+"-"+str(n)] = fuerzas_nodo[str(n-2)+"-"+str(n)]*math.cos(angulo)

def calcularFuerzasHowe(n):
    pass
