class Post:
    def __init__(self, dict):
        self.data_as_dict = dict
        self.id = int(self.data_as_dict.get("id"))
        self.title = self.data_as_dict.get("title")
        self.subtitle = self.data_as_dict.get("subtitle")
        self.body = self.data_as_dict.get("body")
