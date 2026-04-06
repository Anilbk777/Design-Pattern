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
