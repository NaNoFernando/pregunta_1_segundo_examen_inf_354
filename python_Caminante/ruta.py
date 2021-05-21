from ciudad import Ciudad

class Ruta:#Cromosoma
    def __init__(self,ciudades) :
        self.ciudades=ciudades
        self.distancia=sum(
            (a.distancia(b) for a, b in zip(self.ciudades[1:],self.ciudades[:-1]))
        )
        

        
