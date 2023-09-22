from abc import ABC, abstractclassmethod, abstractmethod


class TypeModel(ABC):

    @abstractclassmethod
    def from_database(object_json: dict):
        raise NotImplementedError

    @abstractmethod
    def save():
        raise NotImplementedError
    
    @abstractmethod
    def to_dict():
        raise NotImplementedError