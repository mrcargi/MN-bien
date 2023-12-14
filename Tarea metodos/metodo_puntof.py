#APLICACION DEL METODO DE PUNTO FIJO
import sympy as sp
from prettytable  import PrettyTable
from sympy import Function


x= sp.Symbol('x')

fx_str = input("Ingrese la función que desee resolver: ")  #x*3-6*x*2+9*x-3.75
try: 
    fx = sp.sympify(fx_str)
except sp.SympifyError:
    print("Inválido")
    exit(1)

gx_str = input("\nIngrese el despeje de la x con el mayor exponente: ")  
try: 
    gx = sp.sympify(gx_str)
except sp.SympifyError:
    print("Inválido")
    exit(1)

def metodo(gx, max_iter=100, error=0.0001):
    x_i = float(input("\nIngrese el valor inicial de x: "))
    tabla = PrettyTable()
    tabla.field_names = [f"#i", "Xi", "g_x = {gx}", "Error %"]
    tabla.title = f"Método de Punto Fijo para la función {fx}"

    for i in range(max_iter):
        gx1 = gx.subs(x, x_i)
        errorc = abs((gx1 - x_i) / gx1)*100
        if errorc == 0:
            errorc = "NA"
        tabla.add_row([i + 1, x_i, gx1, errorc])
        if errorc < error:
            break
        x_i = gx1
    print()
    print(f"La raíz encontrada con un error menor a 0.01% es: {gx1}")
    print()
    print(tabla)
   
metodo(gx)