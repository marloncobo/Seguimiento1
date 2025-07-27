class Cuentabancaria:
    def __init__(self, titular, numerocuenta, saldoinicial):
        self.__titular = titular
        self.__numerocuenta = numerocuenta
        self.__saldoinicial = saldoinicial

    def depositar(self, monto):
        self.__saldoinicial += monto

    def retirar(self, monto):
        if self.__saldoinicial > monto:
            self.__saldoinicial -= monto
            return True
        else: return False

    def transfer(self,cuentadestino ,monto):
        if self.__saldoinicial > monto:
            self.__saldoinicial -= monto
            cuentadestino.depositar(monto)
        else: print("No hay saldo suficiente")

    def gettitular(self):
        return self.__titular
    def getnumerocuenta(self):
        return self.__numerocuenta
    def getsaldoinicial(self):
        return self.__saldoinicial
