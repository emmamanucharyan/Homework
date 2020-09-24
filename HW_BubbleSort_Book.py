def return_book_info():
    import json

    with open("HW_Book.json") as open_file:
        books = json.load(open_file)
    return books


def get_book_years_list(books):
    list_of_years = []
    for book in books:
        for key, value in book.items():
            if key == "Publishing Year":
                list_of_years.append(value)
    return list_of_years


def bubble_sort(my_list):
    for current_length in range(len(my_list), 0, -1):
        i = 1
        while i < current_length:
            if my_list[i - 1] > my_list[i]:
                temp = my_list[i-1]           
                my_list[i-1] = my_list[i]     
                my_list[i] = temp             
            i += 1
    return my_list


def return_sorted_books(books, sorted_list):
    sorted_books = []
    j = 0
    while j < len(sorted_list):
        for book in books:
            for value in book.values():
                if j == 0:
                    if value == sorted_list[0]:
                        sorted_books.append(book["Title"])
                else:
                    if sorted_list[j] != sorted_list[j-1]:
                        if value == sorted_list[j]:
                            sorted_books.append(book["Title"])
        j += 1
    return sorted_books


def main():
    books = return_book_info()
    my_list = get_book_years_list(books)
    bubble_sort(my_list)
    final_list = return_sorted_books(books, my_list)
    print("Here are your books in order of year published(old to new).", "\n")
    for element in final_list:
        print(element)

    
main()

