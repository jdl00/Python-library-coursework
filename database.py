'''
contains common database functions such as
1)parsing the text file and return it as an array for ease of manipulation
2)write to a the database file (txt)
3)query database
4) the string returned from parse returns a string of id, title, Author, Purchase Date, Member ID
'''

'''
assuming data is stored as
1|BOOK 1|Tim|11/9/12|12345

'''






def format_array_for_writing(unformatted_array): #initial titles at the top of the file denote
    final_formatted_string = str("")
    for i in unformatted_array:
        final_formatted_string += str(i)+"|"
    return final_formatted_string+"\n"

def append_text_file(member_id,book_id):
    new_array_to_write = parse_text_file(False)
    for i in range(len(new_array_to_write)):
        current_parsed_line = parse_text_line(new_array_to_write[i])
        if int(current_parsed_line[0]) == int(book_id):
            current_parsed_line[4] = str(member_id)
            new_array_to_write[i] = format_array_for_writing(current_parsed_line)
    with open("database.txt","w+") as file:
        for i in new_array_to_write:
            file.write(i)
    return True


def log_action(member_id,book_id,date,checkout):
    array_to_format = []
    array_to_format.append(member_id)
    array_to_format.append(book_id)
    array_to_format.append(date)
    array_to_format.append(checkout)
    append_data(format_array_for_writing(array_to_format),True)



def append_data(string_to_write,should_use_log):
    file_to_use = "log.txt" if should_use_log else "database.txt"
    with open(file_to_use,"a") as file:
        file.write(string_to_write)


def parse_text_line(unparsed_array):
    parsed_array = []
    string_former = str("")
    for i in unparsed_array:
        if i == "|":
            parsed_array.append(string_former)
            string_former = str("")
        else:
            string_former += i
    return parsed_array

def parse_text_file(should_use_log):
    unparsed_array = []
    file_to_use = "log.txt" if should_use_log else "database.txt"
    with open(file_to_use,"r") as file:
        for i in file:
            unparsed_array.append(i)
    return unparsed_array
