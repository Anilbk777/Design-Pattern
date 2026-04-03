from .payment_strategy import PaymentStrategy

class MobileBankingPaymentStrategy(PaymentStrategy):
    def __init__(self, account_no: int):
        self.account_no = account_no

    def pay(self, amount: float):
        print(f"Paid {amount} using Mobile banking app.")
