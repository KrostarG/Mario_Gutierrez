class CuentaBancaria():
    ''' Clase que nos permite la gestión de una Cuenta Bancaria genérica!
    '''
    
    def __init__(self, saldo_inicial, nombre, apellido, moneda = '$'):
        # TODO: Ver la forma de soportar cajas de ahorro y/o cuentas corrientes
        self.movimientos = []
        self.saldo = saldo_inicial
        self.nombre = nombre
        self.apellido = apellido
        self.moneda = moneda

    def depositar(self, monto):
        '''Método que nos permite realizar un depósito bancario'''
        self.movimientos.append('DEPOSITO: ' + str(monto))
        self.saldo = self.saldo + monto

    def datos_titular(self):
        '''Método que nos permite mostrar los datos del titular y su saldo'''
        return self.apellido + ', ' + self.nombre + " con el saldo: " + str(self.saldo) + " " + self.moneda
    
    def datos_saldo(self):
        return self.saldo

    def _reset_saldo(self):
        self.saldo = 0 

    def datos_movimientos(self):
        return list(self.movimientos)


class CC(CuentaBancaria):
    def __init__(self,saldo_inicial, nombre, apellido, limite_descubierto, moneda = '$'):
        self.movimientos = []
        self.saldo = saldo_inicial
        self.nombre = nombre
        self.apellido = apellido
        self.limite_descubierto = limite_descubierto
        self.moneda = moneda

        
    
    
    def extraer(self, monto):
        '''Método que nos permite realizar una extracción de un cuenta bancaria'''
        if self.saldo - monto >= self.limite_descubierto*-1:
            self.movimientos.append('EXTRACCION: ' + str(monto))
            self.saldo = self.saldo - monto
        else:
           self.movimientos.append('SALDO INSUFICIENTE: ' + str(monto)) 
           print("Saldo insuficiente")
        

class CA(CuentaBancaria):
    def __init__(self, saldo_inicial, nombre, apellido, moneda = '$'):
        self.movimientos = []
        self.saldo = saldo_inicial
        self.nombre = nombre
        self.apellido = apellido
        self.moneda = moneda
    
    def extraer(self, monto):
        '''Método que nos permite realizar una extracción de un cuenta bancaria'''
        if self.saldo - monto >= 0:
            self.movimientos.append('EXTRACCION: ' + str(monto))
            self.saldo = self.saldo - monto
        else:
           self.movimientos.append('SALDO INSUFICIENTE: ' + str(monto)) 
           print("Saldo insuficiente")




# Creación de objeto
x = CC(0, 'Felipe', 'Morales',200000)

# Invocación de métodos
print(x.datos_titular())


# Operación de deposito
x.depositar(100000)
print(x.datos_saldo())

# Operación de extracción
x.extraer(250000)
print(x.datos_saldo())


# Imprimo el listado de movimientos de la cuenta
print(x.datos_movimientos())




# Creación de objeto
j = CA(0, 'Felipe', 'Morales')

# Invocación de métodos
print(j.datos_titular())


# Operación de deposito
x.depositar(100000)
print(j.datos_saldo())

# Operación de extracción
x.extraer(250000)
print(j.datos_saldo())


# Imprimo el listado de movimientos de la cuenta
print(j.datos_movimientos())