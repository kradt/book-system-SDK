from types import TypeModel


class Event(TypeModel):
    def __init__(
            self,
            title: str,
            additional_data: dict,
            saved: bool = False):
        self.title = title
        self.additional_data = additional_data
        self.saved = saved

    @classmethod
    def from_database(cls, event: dict):
        """
            Getting event using json that we get from API
        """
        pass
