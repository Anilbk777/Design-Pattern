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


class ItalicDecorator(ITextDecorator):

    def __init__(self, text_view: ITextView):
        super().__init__(text_view)

    def render(self) -> str:
        return f"<i> {self.text_view.render()} </i>"


class UnderLineDecorator(ITextDecorator):

    def __init__(self, text_view: ITextView):
        super().__init__(text_view)

    def render(self) -> str:
        return f"<u> {self.text_view.render()} </u>"


if __name__ == "__main__":
    text = PlainTextView("Hello world")
    print(f"Plain text: {text.render()}")

    bold_text = BoldDecorator(text)
    print(f"Bold text: {bold_text.render()}")

    italic_text = ItalicDecorator(text)
    print(f"Italic text: {italic_text.render()}")

    underline_text = UnderLineDecorator(text)
    print(f"Under line text: {underline_text.render()}")

    all_styles = UnderLineDecorator(ItalicDecorator(BoldDecorator(text)))
    print(f"All style text: {all_styles.render()}")
    