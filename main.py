from ex01.classes import Pessoa
from ex02.conta import ContaBancaria


def main():
    pessoa1 = Pessoa("Jose de Almeida", 50, "Engenheiro")
    print(pessoa1.apresentar())
    print(pessoa1.idade)
    pessoa1.fazer_aniversario()
    print(pessoa1.idade)

    conta1 = ContaBancaria("Jose", 500, 1)
    conta2 = ContaBancaria("Ana", 100, 2)

    print(conta2.mostrar_saldo())
    print(conta1.mostrar_saldo())

    conta1.tranferir(conta2, 100)
    print(conta2.mostrar_saldo())
    print(conta1.mostrar_saldo())


if __name__ == "__main__":
    main()
