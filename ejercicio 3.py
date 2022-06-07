class calculadora:
  
  def __init__(self):
    self.num1=int(input("ingrese un numero"))
    self.num2=int(input("ingrese un numero"))

  def suma(self):
    sum= self.num1 + self.num2
    print("la suma de sus numeros son: ",sum)

  def resta(self):
    res= self.num1 - self.num2
    print("la resta de sus numeros son: ",res)

  def multi(self):
    mul= self.num1 * self.num2
    print("la multiplicacion de sus numeros son: ",mul)
    
  def divi(self):
    div= self.num1 / self.num2
    print("la division de sus numeros son: ",div)

calculadora=calculadora()
calculadora.suma()
calculadora.resta()
calculadora.multi()
calculadora.divi()
