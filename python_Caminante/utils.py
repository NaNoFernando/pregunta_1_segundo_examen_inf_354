from ciudad import Ciudad
import csv
import random
from ruta import Ruta
from copy import deepcopy

def generate_cities(
    city_count:int,minx:int,miny:int,maxx:int,maxy:int
):
    cities=set()
    with open("cities.csv",encoding="utf8") as readable:
        reader=csv.reader(readable)
        for raw_city in reader:
            x=random.randint(minx,maxx)
            y=random.randint(miny,maxy)
            cities.add(Ciudad(name=raw_city[0],x=x,y=y))
    return set(random.sample(cities,city_count))

def genera_poblacion(ciudades,pop_size):
    poblacion=[]
    for _ in range(pop_size):
        poblacion.append(
            Ruta(random.sample(ciudades,len(ciudades)))
            )#sample nos permite escojer al azar sin repetir
    return poblacion

def _cruza_dos_padres(padre1,padre2):#se usa el metodo de PMX
    hijo=deepcopy(padre2)
    elementos=3#hacemos cruze de los primeros 3 elemntos del padre1
    for posicion_p1,valor_p1 in enumerate(padre1):
        posicion_p2=hijo.index(valor_p1)
        hijo[posicion_p2]=hijo[posicion_p1]
        hijo[posicion_p1]=valor_p1
    return hijo

def selecciona_padres(poblacion,n_padres):#selecciona los padres por el metodo elitista, por que selecciona los mejores
    ordenados_por_distancia=sorted(poblacion,key=lambda ruta: ruta.distancia)#este metodo entrega ordenados por la distancia
    return ordenados_por_distancia [:n_padres]

def cruza(mejores_padres,pop_size):
    hijos_faltantes=pop_size-len(mejores_padres)
    nuevos_hijos=[]
    for _ in range(hijos_faltantes):
        padre1,padre2=random.sample(mejores_padres,2)#escoje 2 padres de los mejores que hay de manera aleatoria y unica sin repetirse, tambien se podria escojer a un buen padre con uno pesimo, tambien se puede escojer a uno intermedio con otro superior , nose la seleccion es muy grande
        nuevo_hijo=Ruta(_cruza_dos_padres(padre1.ciudades,padre2.ciudades))
        nuevos_hijos.append(nuevo_hijo)
    return nuevos_hijos

def muta(nuevos_hijos):
    hijos_mutados=[]

    for hijo in nuevos_hijos:
        ciudades=deepcopy(hijo.ciudades)
        if 0.5>random.random():#si la probabilidad es mayora a 0.5 hacemos mutacion
            swap_from=random.randint(0,len(ciudades)-1)
            swap_to=random.randint(0,len(ciudades)-1)
            while swap_to == swap_from:
                swap_to=random.randint(0,len(ciudades)-1)
            aux=ciudades[swap_to]
            ciudades[swap_to]=ciudades[swap_from]
            ciudades[swap_from]=aux
        hijos_mutados.append(Ruta(ciudades))
    return hijos_mutados


