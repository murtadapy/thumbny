from abc import ABC
from abc import abstractmethod


class CommandBase(ABC):
    @abstractmethod
    def execute(*args) -> None:
        raise NotImplementedError()
