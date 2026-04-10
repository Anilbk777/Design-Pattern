from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class PaymentRequest:
    sender : str
    receiver : str
    amount : float
    currency : str

