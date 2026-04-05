from abc import ABC, abstractmethod

class ITextView(ABC):

    @abstractmethod
    def render(self) -> str:
        pass

