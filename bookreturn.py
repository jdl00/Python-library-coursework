from database import *


from database import *
from datetime import datetime
book_list = []


def check_if_book_is_availible(book_id_search):
    global book_list
    book_list = parse_text_file(False)
    check_boolean = False #checks if there are multiple entries of the same book
    for record in book_list:
        temp_record_storage = parse_text_line(record)
        if int(book_id_search) == int(temp_record_storage[0]) and int(temp_record_storage[4]) != int(0):
            check_boolean = True
    return check_boolean

def return_book(member_id,book_id): #does all the criteria checks and returns the data based on whether it works correctly
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

    if check_if_book_is_availible(book_id) == False:
        return "book is availible"
    else:
        if append_text_file("0",book_id) == True:
            log_action("0",book_id,datetime.today().strftime('%Y-%m-%d'),"return")
            return "success"
        else:
            return "failure in writing"

    return "unknown error occurred"

    # return_book("1932","4") -test data
