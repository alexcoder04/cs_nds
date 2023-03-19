
class Queue:
    def __init__(self) -> None:
        self.__data = []

    def isEmpty(self) -> bool:
        return len(self.__data) == 0

    def head(self) -> any:
        return self.__data[0]

    def enqueue(self, element: any) -> None:
        self.__data.append(element)

    def dequeue(self) -> any:
        return self.__data.pop(0)

