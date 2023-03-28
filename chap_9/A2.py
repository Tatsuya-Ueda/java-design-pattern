from abc import ABC, abstractmethod
import random


class Display:
    def __init__(self, impl: "DisplayImpl") -> None:
        self.__impl: "DisplayImpl" = impl

    def open(self) -> None:
        self.__impl.raw_open()

    def print(self) -> None:
        self.__impl.raw_print()

    def close(self) -> None:
        self.__impl.raw_close()

    def display(self):
        self.open()
        self.print()
        self.close()


class RandomCountDisplay(Display):
    def __init__(self, impl: "DisplayImpl") -> None:
        super().__init__(impl)

    def multi_display(self, times: int):
        self.open()
        for _ in range(random.randint(0, times)):
            self.print()
        self.close()


class CountDisplay(Display):
    def __init__(self, impl: "DisplayImpl") -> None:
        super().__init__(impl)

    def multi_display(self, times: int):
        self.open()
        for _ in range(times):
            self.print()
        self.close()


class DisplayImpl(ABC):
    @abstractmethod
    def raw_open(self):
        pass

    @abstractmethod
    def raw_print(self):
        pass

    @abstractmethod
    def raw_close(self):
        pass


class StringDisplayImpl(DisplayImpl):
    def __init__(self, string) -> None:
        self.__string = string

    # @override
    def raw_open(self):
        self.print_line()

    # @override
    def raw_print(self):
        print("|{}|".format(self.__string))

    # @override
    def raw_close(self):
        self.print_line()

    def print_line(self):
        print("+{}+".format("-" * len(self.__string)))


class FileDisplayImpl(DisplayImpl):
    def __init__(self, filename) -> None:
        self.__filename = filename
        self.__maxlen = max(map(len, open(filename).read().split("\n")))

    # @override
    def raw_open(self):
        self.print_line()

    # @override
    def raw_print(self):
        l = open(self.__filename).read().split("\n")
        for s in l:
            print("|{}|".format(s + " " * (self.__maxlen - len(s))))

    # @override
    def raw_close(self):
        self.print_line()

    def print_line(self):
        print("+{}+".format("-" * self.__maxlen))


class Main:
    def __init__(self) -> None:  # Javaのmain関数を模して，これをmainとする
        # d1: Display = Display(StringDisplayImpl("Hello, Japan."))
        # d2: Display = CountDisplay(StringDisplayImpl("Hello, World."))
        # d3: CountDisplay = CountDisplay(StringDisplayImpl("Hello, Universe."))

        # d1.display()
        # d2.display()
        # d3.display()
        # d3.multi_display(5)

        d4 = RandomCountDisplay(FileDisplayImpl("A2.txt"))
        d4.multi_display(10)


Main()
