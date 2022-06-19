class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin
    def check_balance (self):
        print('your balance is 50000')
object=Atm(20)