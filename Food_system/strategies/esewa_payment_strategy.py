from .payment_strategy import PaymentStrategy

class EsewaPaymentStrategy(PaymentStrategy):
    def __init__(self, mobile_no:int):
        self.mobile_no = mobile_no

    def pay(self, amount:float):
        print(f"Paid {amount} using Esewa.")