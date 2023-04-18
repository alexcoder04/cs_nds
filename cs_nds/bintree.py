
class BinTree:
    pass

class BinTree:
    def __init__(self, inhalt: any = None) -> None:
        self.__value = inhalt
        self.__left = None
        self.__right = None

    def hasItem(self) -> bool:
        return self.__value is not None

    def setItem(self, inhalt: any) -> None:
        self.__value = inhalt

    def deleteItem(self) -> None:
        self.__value = None

    def isLeaf(self) -> bool:
        return (self.__right is None) and (self.__left is None)

    def hasLeft(self) -> bool:
        return self.__left is not None

    def getLeft(self) -> BinTree:
        return self.__left

    def setLeft(self, b: BinTree) -> None:
        self.__left = b

    def deleteLeft(self) -> None:
        self.__left = None

    def hasRight(self) -> bool:
        return self.__right is not None

    def getRight(self) -> BinTree:
        return self.__right

    def setRight(self, b: BinTree) -> None:
        self.__right = b

    def deleteRight(self) -> None:
        self.__right = None

