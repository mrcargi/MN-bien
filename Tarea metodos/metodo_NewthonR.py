#implementacion del metodo Newthon Raphson
import sympy as sp
from sympy import diff
from prettytable import PrettyTable
from sympy import Function
x = sp.Symbol('x')

def metodo(fx,max_iter = 100,error = 0.0001 ):
     deri = diff(fx,x)
     x_i = float(input("\nIngrese el valor inicial de x (o TIR) en decimal: "))
     print(f"\nLa fórmula de su función con los datos ingresados, es la siguiente: \n{fx}")
     tabla = PrettyTable()
     tabla.field_names = ["#i ", "Xi"]
     tabla.title = "Metodo Newton - Raphson"
     
     for i in range(max_iter):    
          x_i_1 = x_i - (fx.subs(x,x_i)/deri.subs(x,x_i))            
          tabla.add_row([i+1,x_i_1.evalf()])   
          if abs(fx.subs(x,x_i_1)) <error:
               break
          x_i = x_i_1
          
          
          
     print()
     print(f"La raíz encontrada con un error menor a 0.01% es: {x_i}")
     print()
     print(tabla)


op = input("\nFavor de ingresar el tipo de operacion que desea realizar (VPN o ecuacion): ")

if op.lower() == "vpn":
     
     invin = float(input("\nIngresa la inversion inicial: "))
     retornos = []
     año=1
     print("\nPresione la tecla 0 cuando haya terminado de introducir los flujos")
     while True: 
     
          flujos = float(input(f"\nIngresa el flujo de efectivo del año {año}:  "))
               
               
          if flujos == 0:
               break
          
          
          retornos.append(flujos)
          año+=1  
          
     vpn = -invin
     fx  = vpn

     for i in range(len(retornos)):
          fx  += retornos[i]/ (1+x)**(i+1)
             
     
     metodo(fx)
    


elif op.lower() == "ecuacion":
     x= sp.Symbol('x')
     exp = Function('exp')
     fx_str =input("Ingrese la función por favor: ")                         #sp.exp(-x)-x
     try: 
        fx = sp.sympify(fx_str, locals= {'exp': sp.exp})
     except sp.SympifyError:
        print("Inválido")
        exit(1)
     metodo(fx)

          
else:
     print("Ingrese un valor válido por favor")