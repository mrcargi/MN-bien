#Estrategias Especulativas: Bull Spread
from prettytable import PrettyTable 
from prettytable.colortable import ColorTable, Themes

c1 = int(input("Ingresa la prima 1 : "))
c2 = int(input("Ingresa la prima 2: "))
k1 = int(input("Ingresa precio de ejercicio 1 (strike price) : "))
k2 = int(input("Ingresa precio de ejercicio 2 (strike price) : "))
s_t = int(input("Ingresa el precio del subyancente: "))



tabla = PrettyTable()
tabla = ColorTable(theme = Themes.DEFAULT)

tabla.title = "Bull Spread"
tabla.field_names= ["Precio del Subyacente","Resultado Long Call","Resultado Short Call", "Ganancia o Perdida neta"]

tabla.add_row(["St <= k1", -c1,c2,c2-c1])
tabla.add_row(["k1 <= St < k2",s_t-k1-c1,c2,s_t-k1+c2-c1])
tabla.add_row(["St=>K2",s_t-k1-c1,k2-s_t,k2-k1+c2-c1])


print(tabla)