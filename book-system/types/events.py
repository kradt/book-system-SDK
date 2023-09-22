

class Event:
    def __init__(
            self,
            title: str,
            additional_data: dict,
            saved: bool = False):
        self.title = title
        self.additional_data = additional_data
        self.saved = saved

    def from_database(self, event: dict):
        """
            Getting event using json that we get from API
        """
        pass

    def save(self):
        """
            TODO: saving Event in the database
        """
        pass



