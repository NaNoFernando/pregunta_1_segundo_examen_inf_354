from dataclasses import dataclass
import math
@dataclass(eq=True,frozen=True)
class Ciudad:
    name:str
    x:int
    y:int

    def distancia(self,otra_ciudad):
        xx=otra_ciudad.x-self.x
        yy=otra_ciudad.y-self.y
        return (math.sqrt(xx**2+yy**2))

