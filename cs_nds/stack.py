
class Stack:
    pass

class Stack:
    def __init__(self) -> None:
        self.__data = []

    def isEmpty(self) -> bool:
        return len(self.__data) == 0

    def top(self) -> any:
        if len(self.__data) < 1:
            return None
        return self.__data[-1]

    def push(self, element: any) -> None:
        self.__data.append(element)

    def pop(self) -> any:
        return self.__data.pop()
    
    # convinience constructor methods
    @classmethod
    def from_string(cls, string: str) -> Stack:
        s = cls()
        for char in string:
            s.push(char)
        return s

    @classmethod
    def from_list(cls, l: list) -> Stack:
        s = cls()
        for el in l:
            s.push(el)
        return s

    @classmethod
    def from_elements(cls, *args: any) -> Stack:
        s = cls()
        for el in args:
            s.push(el)
        return s

