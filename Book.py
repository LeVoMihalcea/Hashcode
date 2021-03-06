class Book:
    def __init__(self, id, score):
        self.id = id
        self.score = score
        self.scanned = False

    def get_score(self):
        return self.score

    def get_id(self):
        return self.id

    def __eq__(self, other):
        return self.id == other.get_id()

    def __lt__(self, other):
        return False