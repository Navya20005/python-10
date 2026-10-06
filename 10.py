class Payment:
    def pay(self):
        print("Payment processing")


class UPIPayment(Payment):
    def pay(self):
        print("Payment made using UPI")


class CardPayment(Payment):
    def pay(self):
        print("Payment made using Card")


class CashPayment(Payment):
    def pay(self):
        print("Payment made using Cash")


upi = UPIPayment()
card = CardPayment()
cash = CashPayment()

upi.pay()
card.pay()
cash.pay()