class ClassConGetterySetter():
    def __init__(self):
        self.__propriedad_privada = None
      
    def setPropiedadPrivada(self, valor):
        self.__propriedad_privada = valor
        
    def getPropiedadPrivada(self):
        return self.__propriedad_privada
    
    def propiedadPrivada(self, valor = None):
        if valor = None
            return self.__propriedad_privada
        else:
            self.__propriedad_privada = valor
    
    def __str__(self):
        return "ClaseconGetterySetter con propriedadPrivada -> {}".format(self.__propriedad_privada)
        
        
if __name__ == "__main__":
    c = ClassConGetterySetter()