from utils import generate_cities,genera_poblacion,selecciona_padres
from utils import cruza,muta
todas_ciudades=generate_cities(40,0,0,100,100)#con 40 ciudades 
poblacion=genera_poblacion(todas_ciudades,70)#70 es el tamano de la ppoblacion inicial

for generacion_id in range(1000):#seleccionar padres, la muta y la cruza
    mejor_ruta=sorted(poblacion,key=lambda ruta: ruta.distancia)[0]#ordenamelos por la distancia de cada uno
    print(f"{generacion_id} : {mejor_ruta.distancia}")
    padres_seleccionados=selecciona_padres(poblacion,20)#seleccionara a los mejores 20 padres


    nuevos_hijos=cruza(padres_seleccionados,70)

    hijos_mutados=muta(nuevos_hijos)

    poblacion=padres_seleccionados+hijos_mutados


