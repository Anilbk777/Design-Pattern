from abc import ABC, abstractmethod
from dataclasses import dataclass

from enum import Enum
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


class RazorpayGateway(PaymentGateway):
    def __init__(self):
        self.banking_system = RazorpayBankingSystem()

    def validate_payment(self, payment_request: PaymentRequest) -> bool:
        print(f"[Razorpay] validating payment for {payment_request.sender}")

        if payment_request.amount <= 0:
            return False
        return True

    def initiate_payment(self, payment_request: PaymentRequest) -> bool:
        print(
            f"[Razorpay] initiating payment of {payment_request.amount} {payment_request.currency} for {payment_request.sender}"
        )

        return self.banking_system.process_payment(payment_request.amount)

    def confirm_payment(self, payment_request: PaymentRequest) -> bool:
        print(f"[Razorpay] Confirming payment for {payment_request.sender}")
        return True

class PaymentGatewayProxy(PaymentGateway):
    def __init__(self,payment_gateway:PaymentGateway, max_retries:int):
        self.payment_gateway = payment_gateway
        self.max_retries = max_retries

    def process_payment(self, payment_request:PaymentRequest) -> bool:
        result = False
        for attempt in range(self.max_retries + 1):
            if (attempt > 0):
                print(f"[Proxy] Retrying payment (attemp - {attempt}) for {payment_request.sender}.")
            
            result = self.payment_gateway.process_payment(payment_request)
            if result: break 

        if (not result):
            print(f"[Proxy] Payment failed after {self.max_retries} attempts for {payment_request.sender}")
        
        return result
    
    def validate_payment(self, payment_request):
        return self.payment_gateway.validate_payment(payment_request)
    
    def initiate_payment(self, payment_request):
        return self.payment_gateway.initiate_payment(payment_request)

    def confirm_payment(self, payment_request):
        return self.payment_gateway.confirm_payment(payment_request)


class GatewayType(Enum):
    PAYTM = "paytm"
    RAZORPAY = "razorpay"


class GatewayFactory:
    def get_getway(self, type: GatewayType) -> PaymentGateway:
        if type == GatewayType.PAYTM:
            paytm_gateway = PaytmGateway()
            return PaymentGatewayProxy(paytm_gateway,4)
        
        else:
            razorpay_gateway = RazorpayGateway()
            return PaymentGatewayProxy(razorpay_gateway, 2)

class PaymentService:
    def __init__(self):
        self.payment_gateway :Optional[PaymentGateway] | None = None

    def set_gateway(self, payment_gateway: PaymentGateway):
        self.payment_gateway = payment_gateway

    def process_payment(self, payment_request:PaymentRequest):
        if not self.payment_gateway:
            print(f"[PaymentService] No payment gateway selected.")
            return False

        return self.payment_gateway.process_payment(payment_request)


class PaymentController:

    def handle_payment(self, gateway_type:GatewayType, payment_request: PaymentRequest):
        payment_gateway = GatewayFactory().get_getway(gateway_type)
        PaymentService().set_gateway(payment_gateway)
        return PaymentService().process_payment(payment_request)


if __name__ == "__main__":
    payment_request1 = PaymentRequest("Ram","shyam",500,"NRP")

    print("Processing via Paytm")
    print("="*60)
    payment_controller = PaymentController()
    result1 = payment_controller.handle_payment("paytm",payment_request1)
    print("SUCCESS" if result1 else "FAIL")
    print("=" * 60)

    payment_request2 = PaymentRequest("David", "John", 500, "USD")
    print("Processing via Razorpay")
    print("=" * 60)
    payment_controller = PaymentController()
    result2 = payment_controller.handle_payment("razorpay", payment_request2)
    print("SUCCESS" if result2 else "FAIL")
    print("=" * 60)
