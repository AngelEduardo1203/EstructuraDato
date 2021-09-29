
print("acciones comunes de matematicas basicas en cadena  ")
print("\n")

name = input("estudiente ingresa tu nombre:  ")
print("hola ", name, "haora comensemos")
print("\n")

print(" 1.- Agamos una resta secuencial : es decir a un numero(tottal) le restaremos otro valor(resta) hasta un  balor minimo ")
total=int(input("ingresa el total:  "))
r=int(input("ingresa la resta:  "))
def Restas(total):
  total -= r
  if total >=0 :
      print(total)
      Restas(total)
  else:
        print("limite de balor minimo alcansado")
print(name, "el resultado de la resta es=")
Restas(total)
print("\n")

print(" 2.- Aora sera una suma seccuencia: es decir a un a un balor(base) entre 0 y 100, le sumarremos otro valor(suma), hasta un li mite de 1000")
Base=int(input("ingresa el base:   "))
print("¡¡Adbertencia!!no usar negatibos")
S=int(input("ingresa la sumas2:   "))
def suma(Base):
  Base += S
  if (Base<=1000):
      print(Base)
      suma(Base)
  else:
      print("final de las suma")
print(name, "la cadena de sumas es:")
suma(Base)
print("\n")

print(" 3.- encontremos todos los exponenciales de un numero  ",name)
def multiplo(tabla):
    tabla *= n
    if tabla <=1000 :
      print(tabla)
      multiplo(tabla)
    else:
        print("limite de rango alcansado")
n = int(input("Ingrese un numero del 1 al 100 paar aobtenter sus numeros exponexilaes en un rango de 1 al 1000: "))
print(name," la tabla de elebacion obtenida es:")
print(n)
multiplo(n)
print("\n")

print(" 4.- en este monento ",name," obtendremos una cadena de diviociones tomando un numero(dibidendo) ydibideirlo entre n(divisor) y el resultado entre n y asi susesibamente antes de ser menor a la unaidad ")

def dibiciones(dibidendo):
    dibidendo /= num
    if dibidendo >=1 :
      print(dibidendo)
      dibiciones(dibidendo)
    else:
        print("unidad minima alcansada ")
dibidendo = int(input("indica que numero que desas dividir:  "))
num = int(input("indica el inicio del divisor:  "))
print(name," las cosientes posibles son =")
print(dibidendo,"  entre ",num)
dibiciones(dibidendo)
print("\n")

print(" 5",name," daremos la cadena multiplocacion usando un numero(base) y multiplocarlo por x(exponente) y el resultado sera tendra un limite de 10000 ")

def exponiensiaciones(inis):
    inis *= ex
    if inis <=100000 :
      print(inis)
      exponiensiaciones(inis)
    else:
        print("unidad lumite esponencial alcansado")
print("las recomendaciones son para evitar una saturacuin o u termini muy rapido de la seccuencia")
inis = int(input("escoje una base (de preferrencia menor a 10 y 1ue no sea negativa):  "))
ex= int(input("colca un exponente(con lams mismas reglas que la base):  "))
print(name," las cosientes posibles son =")
print(inis,"  entre ",ex)
exponiensiaciones(inis)
print("grasias por usar esta aplicacion")