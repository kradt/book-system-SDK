from abc import ABC, abstractclassmethod, abstractmethod


class TypeModel(ABC):

    @abstractclassmethod
    def from_json(object_json: dict):
        raise NotImplementedError
    
    @abstractmethod
    def to_dict():
        raise NotImplementedError