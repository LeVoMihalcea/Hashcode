from Book import Book


class Library:
    def __init__(self, id, set_of_books, time_to_sign_up, no_of_books_per_day):
        self.id = id
        self.time_to_sign_up = time_to_sign_up
        self.no_of_books_per_day = no_of_books_per_day
        self.n = None
        self.set_of_books = set_of_books
        # self.set_of_books = []
        # while not set_of_books.empty():
        #     self.set_of_books.append(set_of_books.get()[1])
        print(self.id)


    def compute_n(self, current_day, deadline):
        n = (deadline - (current_day + self.time_to_sign_up)) * self.no_of_books_per_day
        if len(self.set_of_books) < n:
            n = len(self.set_of_books)
        return n

    def compute_rating(self, current_day, deadline):
        n = self.compute_n(current_day, deadline)
        self.n = n
        score = 0
        for i in range(n):
            score = score + self.set_of_books[i].get_score()
        return tuple([score / self.time_to_sign_up, 0 - self.time_to_sign_up])

    def get_books(self):
        return self.set_of_books[:self.n]

    def remove_duplicates(self, books_to_remove):
        for book in books_to_remove:
            try:
                self.set_of_books.remove(book)
            except ValueError:
                pass