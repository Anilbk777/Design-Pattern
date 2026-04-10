from abc import ABC, abstractmethod
from dataclasses import dataclass

import random


@dataclass
class PaymentRequest:
    sender : str
    receiver : str
    amount : float
    currency : str

class BankingSystem(ABC):

    @abstractmethod
    def process_payment(amount:float) -> bool:
        pass


class PaytmBankingSystem(BankingSystem):

    def process_payment(amount:float) -> bool:
        r = (random.randrange(10, 100)) % 100
        return r > 30

class RazorpayBankingSystem(BankingSystem):

    def process_payment(amount:float) -> bool:
        r = (random.randrange(10, 100)) % 100
        return r > 20
