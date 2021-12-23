
#funções sem classes
def somar(a,b):
    return(a+b)

def multiplicar(a,b):
    return(a*b)

#com classes
class Calculadora:
    
    def somarc(self,a,b):
        return(a+b)

    def multiplicarc(self,a,b):
        return(a*b)
        
    a = 6
    b = 8 #só existem dentro da classe

calculadora = Calculadora()

print(calculadora.somarc(5,7))

print(calculadora.a)

calculadora.a = 20
print(calculadora.multiplicarc(calculadora.a,calculadora.b))