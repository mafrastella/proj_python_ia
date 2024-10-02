from Calculadora import *
from Lambda import *

class Main:
  x=int(input("escolha a sua operação:\n1 - adição\n2 - subtração\n3 - multiplicação\n4 - divisão\nescolha: "))
  if (x==1):
    a=int(input("digite o n1: "))
    b=int(input("digite o n2: "))
    print(Lambda.adi(a,b))
  if(x==2):
    a=int(input("digite o n1: "))
    b=int(input("digite o n2: "))
    print(Lambda.sub(a,b))
  if(x==3):
    a=int(input("digite o n1 :"))
    b=int(input("digite o n2 :"))
    print(Lambda.div(a,b))
  if(x==4):
   a=int(input("digite o n1 :"))
   b=int(input("digite o n2 :"))
   print(Lambda.mul(a,b))

     