#APLICACION DEL METODO DE FALSA POSICION
import sympy as sp
from sympy import Function

from prettytable  import PrettyTable

x= sp.Symbol('x')



fx_str = input("\n Ingrese la ecuación que desee resolver: ")  #(exp(x)) + (2*(-1(x))) + 2 * cos(x) - 6
try: 
    fx = sp.sympify(fx_str)
except sp.SympifyError:
    print("Inválido")
    exit(1)



                                                       
      



def falsa_posicion(a,b,error = 0.00001,max_iter= 100):
    if fx.subs(x,a).evalf() == 0:
        return f"La raíz buscada es el valor de a= {a}"
    elif fx.subs(x,b) == 0:
        return f"La raíz buscada es el valor de b= {b}"
    
    
    if fx.subs(x,a).evalf()*fx.subs(x,b).evalf() > 0:
        print("\nLa raíz NO se encuentra en el intervalo ingresado")
        return None
    tabla = PrettyTable()
    tabla.field_names = ["#Iteracion", "a", "b", "m", "f(a)", "f(b)", "f(m)", "Error%"]
    tabla.title = f"METODO DE FALSA POSICION Para la funcion : {fx} "
    m = b - ((fx.subs(x, b)).evalf() * (b - a) / (fx.subs(x, b).evalf() - fx.subs(x, a).evalf()))
    # Agregar la primera fila con los valores iniciales de a y b
   
    
    for i in range(max_iter):
        m_previo = m
            
        m = b - ((fx.subs(x, b)).evalf() * (b - a) / (fx.subs(x, b).evalf() - fx.subs(x, a).evalf()))
        errorc = abs(((m) - m_previo)/m) *100
        tabla.add_row([i + 1, a, b, m, fx.subs(x, a).evalf(), fx.subs(x, b).evalf(), fx.subs(x, m).evalf(), errorc])

        if fx.subs(x, m).evalf() == 0 or abs(fx.subs(x, m).evalf()) < error:
            break

        if fx.subs(x, m).evalf() * fx.subs(x, a).evalf() < 0:
            b = m
        else:
            a = m
        
            
    print()
    print(f"La raíz encontrada con un error menor a 0.01% es: {m}")
    print()
    print(tabla)




raiz = falsa_posicion(float(input("\n Ingrese el intervalo a: ")),float(input("\n ingrese el intervalo b: ")))