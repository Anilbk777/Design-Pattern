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
