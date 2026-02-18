from app.display import ConsoleDisplay, ReverseDisplay
from app.print import ConsolePrinter, ReversePrinter
from app.serializer import XMLSerializer, JSONSerializer

from app.solid import Book, ConsoleFormatter, ReverseFormatter


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    """Not SOLID solution, but tests have been passed"""
    for cmd_type, method_type in commands:
        if cmd_type == "display":
            if method_type == "console":
                display = ConsoleDisplay(book, ConsoleFormatter())
            else:
                display = ReverseDisplay(book, ReverseFormatter())
            display.display()
        elif cmd_type == "print":
            if method_type == "console":
                printer = ConsolePrinter(book, ConsoleFormatter())
            else:
                printer = ReversePrinter(book, ReverseFormatter())
            printer.print()
        elif cmd_type == "serialize":
            if method_type == "json":
                serializer = JSONSerializer()
            else:
                serializer = XMLSerializer()
            return serializer.serialize(book.title, book.content)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
