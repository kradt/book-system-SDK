from types import TypeModel


class Event(TypeModel):
    def __init__(
            self,
            title: str,
            additional_data: dict):
        self.title = title
        self.additional_data = additional_data

    @classmethod
    def from_json(cls, event: dict):
        """
            Getting event using json that we get from API
            {
                "title": "str",
                "additional_data": "dict"
            }
        """
        return super().__init__(title=event["title"], additional_data=event["additional_data"])

    def to_dict(self) -> dict:
        return dict(title=self.title, additional_data=self.additional_data)
