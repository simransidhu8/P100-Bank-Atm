class Atm:
    def __init__(self, card_number, pin_number):
        self.card_number = card_number
        self.pin_number = pin_number

    def CashWithdrawl(self):
        print("Cash withdrawed")
    
    def BalanceEnquiry(self):
        print("This is balance enquiry")

    def CashDeposit(self):
        print("Deposit made")
    
cash = Atm("123456", "01234")
print(cash.card_number)
print(cash.pin_number)
print(cash.CashDeposit())