
class ContaBancaria:

    def __init__(self, titular: str, saldo: float, numero_da_conta: int):
        self.titlar = titular
        self.__saldo = saldo
        self.numero_da_conta = numero_da_conta

    def _tem_saldo(self, valor: float) -> bool:
        if valor > self.__saldo:
            print("Saldo insufiente")
            return False
        return True

    def mostrar_saldo(self) -> float:
        return self.__saldo

    def _validar_valor(self, valor: float) -> bool:
        if valor <= 0:
            print("Valor invalido, insira um valor valido")
            return False
        return True

    def depositar(self, valor: float) -> bool:
        if not self._validar_valor(valor):
            return False
        self.__saldo += valor
        print(f"Deposito de valor {valor}, realizado com sucesso")
        return True

    def levantar(self, valor: float):
        if not self._tem_saldo(valor):
            return False
        self.saldo -= valor
        print(
            f"O valor {valor} depositado com sucesso, valor atual {self.mostrar_saldo}")

    def tranferir(self, conta_destino: "ContaBancaria", valor: float) -> bool:
        if not self._validar_valor(valor):
            return False
        if not self._tem_saldo(valor):
            return False
        self.__saldo -= valor
        conta_destino.__saldo += valor
        print(f"Transferencia de valor {valor}, realizad com sucesso")
        return True
