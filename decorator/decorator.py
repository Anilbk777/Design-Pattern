from abc import ABC, abstractmethod

class ITextView(ABC):

    @abstractmethod
    def render(self) -> str:
        pass

class PlainTextVIew(ITextView):

    def __init__(self, text:str):
        self.text = text

    def render(self) -> str:
        return self.text
    
class ITextDecorator(ITextView):
    
    def __init__(self, text_view:ITextView):
        self.text_view = text_view

    def render(self):
        pass
