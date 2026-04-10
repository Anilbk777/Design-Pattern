from abc import ABC, abstractmethod
from dataclasses import dataclass

from typing import Optional
import random


@dataclass
class PaymentRequest:
    sender : str
    receiver : str
    amount : float
    currency : str

class BankingSystem(ABC):

    @abstractmethod
    def process_payment(self, amount:float) -> bool:
        pass


class PaytmBankingSystem(BankingSystem):

    def process_payment(self, amount:float) -> bool:
        r = (random.randrange(10, 100)) % 100
        return r > 30

class RazorpayBankingSystem(BankingSystem):

    def process_payment(self, amount:float) -> bool:
        r = (random.randrange(10, 100)) % 100
        return r > 20

class PaymentGateway(ABC):

    def __init__(self):
        self.banking_system : Optional[BankingSystem] | None = None

    def process_payment(self, payment_request:PaymentRequest) -> bool:
        if not (self.validate_payment(payment_request)):
            print(f"[PaymentGateway] validation failed for {payment_request.sender}.")
            return False
        if not (self.initiate_payment(payment_request)):
            print(f"[PaymentGateway] initiation failed for {payment_request.sender}.")
            return False
        if not (self.confirm_payment(payment_request)):
            print(f"[PaymentGateway] confirmation failed for {payment_request.sender}.")
            return False

        return True

    @abstractmethod
    def validate_payment(self, payment_request:PaymentRequest) -> bool:
        pass

    @abstractmethod
    def initiate_payment(self, payment_request:PaymentRequest) -> bool:
        pass

    @abstractmethod
    def confirm_payment(self,payment_request:PaymentRequest) -> bool:
        pass


class PaytmGateway(PaymentGateway):
    def __init__(self):
        self.banking_system = PaytmBankingSystem()

    def validate_payment(self, payment_request:PaymentRequest) -> bool:
        print(f"[Paytm] validating payment for {payment_request.sender}")

        if payment_request.amount <= 0 or payment_request.currency != "NRP":
            return False
        return True

    def initiate_payment(self, payment_request:PaymentRequest) -> bool:
        print(f"[Paytm] initiating payment of {payment_request.amount} {payment_request.currency} for {payment_request.sender}")

        return self.banking_system.process_payment(payment_request.amount)
    
    def confirm_payment(self,payment_request:PaymentRequest) -> bool:
        print(f"[Paytm] Confirming payment for {payment_request.sender}")
        return True
    