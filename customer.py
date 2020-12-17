from atm_card import ATMCard

class Customer(ATMCard):
    def __init__(self, id, custPin, custBalance):
        super().__init(defaultPin, defaultBalance)
        self.id = id
    
    def withdrawBalance(self, nominal):
        self.nominal = nominal
        return 'Saldo anda saat ini adalah Rp ' + str(self.custBalance - self.nominal)
    
    def depositBalance(self, nominal):
        self.nominal = nominal
        return 'Saldo anda saat ini adalah Rp ' + str(self.custBalance + self.nominal)
    
    def checkBalance(self):
        return "Saldo anda saat ini adalah Rp" + str(self.custBalance)
