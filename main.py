from Book import Book
from Library import Library
from queue import PriorityQueue

def find_book_in_array(book_id, master_array):
    for book in master_array:
        if book.get_id() == book_id:
            return book

# def get_max_rating(libraries):
#     max = -9999999
#     for library in libraries:
#

if __name__ == "__main__":
    in_file = open('input.txt', 'r')
    out_file = open('output.txt', 'w')

    ##INPUT
    first_line = in_file.readline().strip().split(' ')
    number_of_total_books = int(first_line[0])
    number_of_total_libraries = int(first_line[1])
    deadline = int(first_line[2])
    current_day = 0

    book_scores = in_file.readline().strip().split(' ')

    master_books_array = {}
    for i in range(number_of_total_books):
        new_book = Book(i, int(book_scores[i]))
        master_books_array[i] = new_book

    print("created master book array")

    libraries = []
    for n in range(number_of_total_libraries):
        library_atttributes = in_file.readline().strip().split(' ')
        books_in_library = in_file.readline().strip().split(' ')

        # set_of_books = PriorityQueue()
        set_of_books = []
        for i in books_in_library:
            # book_to_put_in = find_book_in_array(int(i), master_books_array)
            # set_of_books.put((book_to_put_in.get_score(), book_to_put_in))
            set_of_books.append(master_books_array[int(i)])

        new_library = Library(n, set_of_books, int(library_atttributes[1]), int(library_atttributes[2]))
        libraries.append(new_library)

    ##-------
    ##COMPUTING
    output_string = ""
    chosen_libraries = 0

    while current_day < deadline:
        print(str(current_day) + "/" + str(deadline))
        if not libraries:
            break
        mvp = libraries[0]
        mvp_rating = mvp.compute_rating(current_day, deadline)
        for library in libraries:
            library_rating = library.compute_rating(current_day, deadline)
            if library_rating > mvp_rating:
                mvp = library
                mvp_rating = library_rating

        libraries.remove(mvp)
        books_to_remove = mvp.get_books()
        for book in books_to_remove:
            book.scanned = True
        if mvp.n <= 0: break
        chosen_libraries += 1
        output_string += str(mvp.id) + " " + str(len(books_to_remove)) + "\n"
        for book in books_to_remove:
            output_string += str(book.get_id()) + " "
        output_string += "\n"
        current_day += mvp.time_to_sign_up

    ##-------
    ##OUTPUT
    out_file.write(str(chosen_libraries) + "\n" + output_string)
