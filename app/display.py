from abc import abstractmethod, ABC

from app.solid import Book, Formatter


class Display(ABC):
    def __init__(self, book: Book, formatter: Formatter) -> None:
        self.book = book
        self.formatter = formatter

    @abstractmethod
    def display(self) -> str:
        pass


class ConsoleDisplay(Display):
    def __init__(self, book: Book, formatter: Formatter):
        super().__init__(book, formatter)

    def display(self) -> None:
        print(self.formatter.format(self.book.content))


class ReverseDisplay(Display):
    def __init__(self, book: Book, formatter: Formatter):
        super().__init__(book, formatter)

    def display(self) -> None:
        print(self.formatter.format(self.book.content))
