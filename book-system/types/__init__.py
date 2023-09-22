from abc import ABC, abstractclassmethod, abstractmethod


class TypeModel(ABC):

    @abstractclassmethod
    def create():
        raise NotImplementedError