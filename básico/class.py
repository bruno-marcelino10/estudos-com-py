class Carro:

    def __init__(self, empresa, ano, cor): #__init__ são as propriedades iniciais que toda classe tem

        self.empresa = empresa
        self.ano = ano 
        self.cor = cor

    def MostrarEmpresa(self): # pode-se definir MÉTODOS que são funções cujos argumentos já foram definidos na classe

        print("CAPITALISMO")

    def ligar(self): 

        print("Caio macho")  

    def bilau(self):

        print(self.ano) 

amauri = Carro("disney", "1999", "vermelho")             
print(amauri.ano, amauri.cor, amauri.empresa)
print(amauri.MostrarEmpresa())