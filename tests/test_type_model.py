import pytest

from book_system.types import TypeModel


def test_not_implemented_error_in_interface_of_type():

    class Test(TypeModel):
        def params(self):
            super().params()

        def body(self):
            super().body()
        
        def from_json(self):
            TypeModel.from_json({"title": "hello"})

    obj = Test()

    with pytest.raises(NotImplementedError):
        obj.from_json()

    with pytest.raises(NotImplementedError):
        obj.params()

    with pytest.raises(NotImplementedError):
        obj.body()
