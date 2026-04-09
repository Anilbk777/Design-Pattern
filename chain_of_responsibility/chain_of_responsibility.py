from abc import ABC, abstractmethod
from typing import Optional


class Request:
    def __init__(self, user, token, role, request_count, payload):
        self.user = user
        self.token = token
        self.role = role
        self.request_count = request_count
        self.payload = payload


class Handler(ABC):
    def __init__(self):
        self.next_handler: Optional["Handler"] | None = None

    def set_next(self, handler: "Handler") -> "Handler":
        self._next = handler
        return handler

    def handle(self, request: Request):
        if not self._process(request):
            return  

        if self._next:
            return self._next.handle(request)

    @abstractmethod
    def _process(self, request: Request) -> bool:
        pass


class AuthenticationHandler(Handler):
    def _process(self, request: Request) -> bool:
        if request.token != "valid_token":
            print("Authentication Failed")
            return False
        print("Authentication Passed")
        return True


class AuthorizationHandler(Handler):
    def _process(self, request: Request) -> bool:
        if request.role != "admin":
            print("Authorization Failed")
            return False
        print("Authorization Passed")
        return True


class RateLimitHandler(Handler):
    def _process(self, request: Request) -> bool:
        if request.request_count > 5:
            print("Rate Limit Exceeded")
            return False
        print("Rate Limit OK")
        return True


class ValidationHandler(Handler):
    def _process(self, request: Request) -> bool:
        if not isinstance(request.payload, dict):
            print("Invalid Payload")
            return False
        print("Validation Passed")
        return True


class BusinessHandler(Handler):
    def _process(self, request: Request) -> bool:
        print("Processing Business Logic")
        return True


def build_pipeline():
    auth = AuthenticationHandler()
    authz = AuthorizationHandler()
    rate = RateLimitHandler()
    validate = ValidationHandler()
    business = BusinessHandler()

    auth.set_next(authz).set_next(rate).set_next(validate).set_next(business)

    return auth


if __name__ == "__main__":
    pipeline = build_pipeline()

    req = Request(
        user="Anil",
        token="valid_token",
        role="admin",
        request_count=3,
        payload={"data": "hello"},
    )

    pipeline.handle(req)
