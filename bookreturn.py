from database import *


def check_if_book_is_availible(book_id_search):
    global book_list
    book_list = parse_text_file()
    check_boolean = False #checks if there are multiple entries of the same book
    for record in book_list:
        if book_id_search in record and parse_text_line(record)[4] != 0:
            check_boolean = True
    return check_boolean

def return_book(member_id,book_id):
    try:
        if member_id == "0000" or int(member_id) < 1000 or int(member_id) > 9999:
            return "invalid member id!"
    except:
        return "invalid member id!"
    try:
        if int(book_id) < 1:
            return "invalid book id"
    except:
        return "invalid book id"

    if check_if_book_is_availible == False:
        return "book is unavailible"
    else:
        if append_text_file(0,book_id) == True:
            log_action(member_id,book_id,int(datetime.today().strftime('%Y-%m-%d'),"return"))
            return "success"
        else:
            return "failure in writing"

    return "unknown error occurred"
