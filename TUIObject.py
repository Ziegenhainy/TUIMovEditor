from abc import abstractmethod, ABC

class TUIObject(ABC):
    @abstractmethod
    def render(self, canvas: list[list[str]]):
        pass

    @abstractmethod
    def __init__(self):
        pass