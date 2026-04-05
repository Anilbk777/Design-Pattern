from abc import ABC, abstractmethod

class ITextView(ABC):

    @abstractmethod
    def render(self) -> str:
        pass

class PlainTextView(ITextView):

    def __init__(self, text:str):
        self.text = text

    def render(self) -> str:
        return self.text

class ITextDecorator(ITextView):
    
    def __init__(self, text_view:ITextView):
        self.text_view = text_view

    def render(self):
        pass

class BoldDecorator(ITextDecorator):

    def __init__(self, text_view: ITextView):
        super().__init__(text_view)

    def render(self) -> str:
        return f"<b> {self.text_view.render()} </b>"
