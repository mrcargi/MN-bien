#implementacion del metodo Newthon Raphson
import sympy as sp
from sympy import diff
from prettytable import PrettyTable
x = sp.Symbol('x')

def metodo(fx,max_iter = 100,error = 0.0000001 ):
     deri = diff(fx,x)
     x_i = float(input("Ingresa el valor inicial de x (en caso de ser % dividiarlo entre 100): "))
     tabla = PrettyTable()
     tabla.field_names = ["#i ", "Xi"]
     tabla.title = "Metodo Newton - Raphson"

     for i in range(max_iter):     
          x_i_1 = x_i - (fx.subs(x,x_i)/deri.subs(x,x_i))
          tabla.add_row([i+1,x_i_1.evalf()])   
          if abs(fx.subs(x,x_i_1)) <error:
               break
          x_i = x_i_1
          

     print(tabla)


op = input("Favor de ingresar el tipo de operacion que desea realizar (vpn o ecuacion): ")

if op.lower() == "vpn":
     
     invin = float(input("Ingresa la inversion inicial: "))
     retornos = []

     while True: 
     
          flujos = float(input("ingresa el flujjo de efectivo para cada año en el perido(ingresa '0' para salir):  "))
               
               
          if flujos == 0:
               break
          
          
          retornos.append(flujos)
          
     vpn = -invin
     fx  = vpn

     for i in range(len(retornos)):
          fx  += retornos[i]/ (1+x)**(i+1)
               

     print(fx)
     metodo(fx)
    


elif op.lower() == "ecuacion":
     fx = sp.exp(-x)-x
     metodo(fx)

          
else:
     print("Ingresa un valor valido pendejo")

