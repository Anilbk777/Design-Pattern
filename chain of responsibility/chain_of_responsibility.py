from abc import ABC, abstractmethod

class Handler(ABC):
    @abstractmethod
    def set_next(self, handler:"Handler"):
        pass

    @abstractmethod
    def handle_request(self, request):
        pass