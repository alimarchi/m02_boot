class Dog():
    def __init__(self):
        self.nombre = ""
        self.edad = None
        self.peso = None
    
    def ladrar(self):
        if self.peso == None:
            print("Soy un fantasma")
        if self.peso >= 8:
            print("GUAU, GUAU")
        else:
            print("Guau, Guau")
        

class Perro():
    def __init__(self, n, e, p):
        self.nombre = n
        self.edad = e
        self.peso = p
        
    def ladrar(self):
        if self.peso >= 8:
            print("GUAU, GUAU")
        else:
            print("Guau, Guau")
            
    def __str__(self):
        return "Soy el perro {}, e: {}, p: {}".format(self.nombre, self.edad, self.peso)
        
def ladrar():
    print("No tengo perro")
    

class PerroAsistencia(Perro):
    def __init__(self, nombre, edad, peso, amo):
        Perro.__init__(self, nombre, edad, peso)
        self.amo = amo
        self.__trabajando = False
        
    def __str__(self):
        return "Perro asistencia de {}".format(self.amo)
    
    def pasear(self):
        print("{} ayudo a mi dueno {} a pasear".format(self.nombre, self.amo))
        
        
    def ladrar(self):
        if self.__trabajando:
            print("Shhhhh, no puedo ladrar")
        else:
            Perro.ladrar(self)
            
    def trabajando(self, valor=None):
        if valor == None:
            return self.__trabajando
        else:
            self.trabajando = valor
            
            
class Timido():
    def __init__(self, nombre):
        self.__nombre = nombre
        
    def preguntarNombreConCuidado(self):
        return self.__nombre