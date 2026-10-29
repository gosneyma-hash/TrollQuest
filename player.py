class Player:
    def __init__(self):
        self.flag = False
        self.pants = False
        self.shoe = False
        self.exam = False

    def hasFlag(self) -> bool:
        return self.flag

    def setFlag(self, b: bool) -> None:
        self.flag = b

    def hasPants(self) -> bool:
        return self.pants

    def setPants(self, b: bool) -> None:
            self.pants = b

    def hasShoe(self) -> bool:
        return self.shoe

    def setShoe(self, b: bool) -> None:
            self.shoe = b

    def hasExam(self) -> bool:
        return self.exam

    def setExam(self, b: bool) -> None:
            self.exam = b