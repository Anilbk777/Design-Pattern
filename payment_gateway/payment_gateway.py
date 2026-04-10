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

    @abstractmethod
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
