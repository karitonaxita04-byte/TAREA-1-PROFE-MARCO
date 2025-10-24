lista =[]


def __init__(self, nombre, apellido, email):

    self.nombre = nombre
    self.apellido = apellido       
    self.email = email
    self.limite_credito = 30000
    self.saldo_pagar = 0
    
    def hacer_compra(self, monto:int):  
        self.saldo_pagar += monto   
        print(f"compra realizada por {monto}.nuevo saldo:{self.salgo_pagar}")

    def pagar_tarjeta(self,monto:int):
        if monto > self.saldo_pagar:
            monto = self.saldo_pagar
        self.saldo_pagar -= monto
        print(f"pago realizado por {monto}.nuevo saldo:{self.salgo_pagar}")


def mostrar_saldo_usario(self):
            print(f"clente1:{self.nombre} {self.apellido}, saldo a pagar:{self.saldo_pagar} ")

def transferir_deuda(self, otro_usuario, monto:int):
        if monto > self.saldo_pagar:
            monto = self.saldo_pagar

        self.saldo_pagar -= monto
        otro_usuario.saldo_pagar += monto
        print(f"Se han transferido ${monto} de deuda a {otro_usuario.nombre} {otro_usuario.apellido}.")

cliente1 = lista("karen","nuñez","kdkkd@gmail.com",3000)
cliente2 = lista("paloma","cortes","mdmdndn@gmail.com", 359100)

cliente1.saldo_apagar()
cliente2.limite_credito()

cliente1.hacer_compra(5000)
cliente1.mostrar_saldo_usuario()

cliente1.pagar_tarjeta(2000)
cliente1.mostrar_saldo_usuario()

cliente1.transferir_deuda(cliente2, 1000)
cliente1.mostrar_saldo_usuario()
cliente2.mostrar_saldo_usuario()







