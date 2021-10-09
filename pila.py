class pila:
    def __init__(self):
        self.items = []
    def estaVacia(self):
        return self.items==[]
    def apilar(self,item):
        self.items.append(item)
    def desapilar(self):
        self.items.pop()
    def verificar(self):
        return self.items[len(self.items)-1]
    def tamanio(self):
        return len(self.items)

def validar_parentesis(cadena):
    ex=pila()
    numeros=['1','2','3','4','5','6','7','8','9','0','+','-','*','/','.',' ']
    balanceado=True

    for c in cadena:
        if c=="(":
            ex.apilar(c)
        else:
            if c in numeros:
                next
            else:
                if ex.estaVacia():
                    balanceado=False
                else:
                    ex.desapilar()

    if balanceado and ex.estaVacia():
        return True
    else:
        return False

cade = "5.2 + (10 / 2 + 8.9 * 0.5"

if validar_parentesis(cade):
    print ("Expresión balanceada")
else:
    print ("Expresión No balanceada")
    pos=len(cade)
    print ("falta parentesis en la posición: ", pos+1)


 

