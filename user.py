class User:
    def __init__(self, name):
        self.name = name
        pass

    def __repr__(self):
        return f"{self.name}"
