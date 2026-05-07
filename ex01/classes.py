class Pessoa:
    def __init__(self, nome: str, idade: int, profissao: str):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def apresentar(self) -> str:
        return f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e sou {self.profissao}."

    def fazer_aniversario(self):
        self.idade += 1
