from operator import truediv
from tkinter import TRUE
from Conta import Conta


class ContaCorrente(Conta):
    def __init__(self, id_conta, saldo, limite):
        super().__init__(id_conta, saldo)
        self.limite = 1000

    def get_saldo(self):
        return self.saldo

    def set_saldo(self, valor):
        self.saldo = self.saldo + valor

    def get_valor(self):
        return self.saldo

    def set_deposita(self, valor):
        self.saldo += valor

    def set_sacar(self, valor):
        try:
            if (valor <= self.saldo):
                self.saldo -= valor
            else:
                print('saldo insuficiente')
        finally:
            print(f'Saldo restante: R${self.saldo:.2f}')

    def consultar_saldo(self):
        print(self.saldo)


kaua = ContaCorrente(id_conta=1, saldo=3000.00, limite=1000)
# kaua.set_deposita(1200.00)
kaua.set_sacar(valor=100.00)
#kaua.consultar_saldo()
