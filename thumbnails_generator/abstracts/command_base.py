from abc import ABC
from abc import abstractmethod


class CommandBase(ABC):
    @abstractmethod
    def _validate(*args) -> None:
        """A validate method that should be called in the execution
        """
        raise NotImplementedError()

    @abstractmethod
    def execute(*args) -> None:
        raise NotImplementedError()
