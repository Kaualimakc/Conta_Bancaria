from ContaCorrente import ContaCorrente


class ContaPoupança(ContaCorrente):

    def __init__(self, id_conta, saldo, limite):
        super().__init__(id_conta, saldo, limite)

    def get_Taxa_de_redimento_ao_ano(self):
        return self.saldo

    def set_Taxa_de_rendimento_ao_ano(self):
        self.porcentagem_ano = self.saldo * 0.0085

    def Exibir_rendimento_ano(self):
        print(f"seu rendimento ao ano é de:  R${self.porcentagem_ano:.2f}")

    def get_Taxa_de_redimento_ao_mes(self):
        return self.saldo

    def set_Taxa_de_rendimento_ao_mes(self):
        self.porcentagem_mes =self.saldo * 0.0005

    def Exibir_rendimento_mes(self):
        print(f"seu rendimento ao mes é de:  R${self.porcentagem_mes:.2f}")


kaua = ContaPoupança(id_conta=3, saldo=3000.00, limite=1500)
kaua.set_Taxa_de_rendimento_ao_mes()
kaua.Exibir_rendimento_mes()
kaua.set_Taxa_de_rendimento_ao_ano()
kaua.Exibir_rendimento_ano()

