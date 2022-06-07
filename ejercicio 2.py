# declaramos la clase persona
class Persona:
    # declaramos el metodo __init__
    def __init__(self):
        self.nombre=input("Ingrese el nombre: ")
        self.nota=int(input("Ingrese su nota: "))
 
 
    # declaramos el metodo mostrar
    def mostrar(self):
        print("Nombre: ",self.nombre)
        print("nota: ",self.nota)

 
    def nota_final(self):
      if self.nota>=3:
        print("aprovo")
      else:
       print("Reprovo")
# bloque principal
persona1=Persona()
persona1.mostrar()
persona1.nota_final()
