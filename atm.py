class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("El depósito no puede ser negativo")
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("El retiro no puede ser negativo")

        if amount > self.balance:
            raise ValueError("Fondos insuficientes")

        self.balance -= amount


if __name__ == "__main__":
    atm = ATM(1000)

    print("=== CAJERO AUTOMÁTICO ===")
    print("Saldo:", atm.check_balance())

    atm.deposit(500)
    print("Después del depósito:", atm.check_balance())

    atm.withdraw(200)
    print("Después del retiro:", atm.check_balance())