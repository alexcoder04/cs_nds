
class DynArray:
    pass

class DynArray:
    def __init__(self):
        self.__data = []

    def append(self, element: any) -> None:
        self.__data.append()

    def delete(self, index: int) -> None:
        del self.__data[index]

    def insertAT(self, index: int, element: any) -> None:
        self.__data.insert(index, element)

    def getItem(self, index: int) -> any:
        return self.__data[index]

    def setItem(self, index: int, element: any) -> None:
        self.__data[index] = element

    def isEmpty(self) -> bool:
        return len(self.__data) == 0

    def getLength(self) -> int:
        return len(self.__data)
    
    # convinience constructor methods
    @classmethod
    def from_list(cls, l: list) -> DynArray:
        s = cls()
        for el in l:
            s.append(el)
        return s

    @classmethod
    def from_elements(cls, *args: any) -> DynArray:
        s = cls()
        for el in args:
            s.append(el)
        return s
