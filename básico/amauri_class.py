class Carro:
    #modelo empresa ano
    def __str__(self): # O que será mostrado quando printarmos o objeto
        return(self.modelo + " 9021// " + self.empresa + " " + str(self.ano))

    def __init__(self, modelo, empresa, ano): # Requisitos para criar uma classe
        self.modelo = modelo # Atributos da classe que podem ser chamados com objeto.atributo
        self.empresa = empresa
        self.ano = ano

    def mudar_ano(self, ano_novo): # Função (método) que só se aplica aos elementos da classe
        self.ano = ano_novo # alterando novamente um atributo da classe

#
carro = Carro("Focus", "Ford", 2006) # Criando um objeto do tipo Carro
print(carro) # retorna algo

print(carro.ano) # retorna um atributo do carro

carro.mudar_ano(2001) # retorna um método aplicável ao carro 
print(carro.ano) # a função alterou o atributo do carro 