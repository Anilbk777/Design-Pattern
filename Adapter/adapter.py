from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self,amount:float, currency:str):
        pass

    @abstractmethod
    def is_payment_successful(self)-> bool:
        pass

    @abstractmethod
    def get_transaction_id(self) -> str:
        pass

class CheckOutService:
    def __init__(self, processor:PaymentProcessor):
        self._processor = processor

    def checkout(self, amount:float, currency:str):
        self._processor.process_payment(amount,currency)
        if self._processor.is_payment_successful():
            print(f"Payment successful: {amount} {currency}")
            print(f"Transaction ID: {self._processor.get_transaction_id()}")
        else:
            print("Payment failed")

class LegacyGateway:
    def __init__(self):
        self._transaction_refrence = None
        self._payment_successful = False

    def execute_transaction(self, amount:float, currency:str):
        print(f"Processing legacy transaction: {currency} {amount}")
        self._transaction_refrence = f"LEG-{hash(amount)}"
        self._payment_successful = True

    def get_transaction_refrence(self) -> str:
        return self._transaction_refrence

    def is_payment_successful(self) -> bool:
        return self._payment_successful


