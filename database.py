'''
contains common database functions such as 
1)parsing the text file and return it as an array for ease of manipulation
2)write to a the database file (txt) 
3)query database
4) the string returned from parse returns a string of id, title, Author, Purchase Date, Member ID
'''

def delete_from_text_file(string_to_delete,should_use_log):
    file_to_use = "log.txt" if should_use_log else "database.txt"
    with open('file_path', 'r+') as file:
        if string_to_delete not in file:
            return 
        parsed_array = parse_text_file(file_to_use)
        string_to_delete = string_to_delete.lower()
        parsed_array.remove(string_to_delete)
        file.truncate(0)
        write_array_to_text_file(parsed_array,file_to_use)


def parse_text_file(should_use_log):
    parsed_array = []
    file_to_use = "log.txt" if should_use_log else "database.txt"
    with open(file_to_use,"r"):
        for line in file:
            parsed_array.append(line)
    return parsed_array

'''
assuming that storage below is formatted such that a double space is a marker that it is at the end of the 
place holder, to make for extraction of data easier
id title  Author Purchase Date Member ID
1  BOOK 1 Tim    11/9/12       12345
'''

def format_string_for_handling(string_to_handle):
    string_to_handle = string_to_handle" ".join(string_to_handle.split())
    return string_to_handle.replace(' ','|')


def parse_each_text_line(list_to_parse):
    final_parsed_array = []
    for i in list_to_parse:
        final_parsed_array.append(format_string_for_handling(i))

    return final_parsed_array

def get_line_formatting_length(string_to_check): #return an array signifying the length of the each of the columns of data
    length_array = []
    previous_i_char = char('')
    length_count = int(0)
    for i in string_to_check:
        if previous_i_char == ' ' and i != ' '
            length_array.append(length_count)
            length_count = 0
        else if previous_i_char != ' ' and i !=  ' ':
            length_count += 1
    return length_array


def format_array_for_writing(unformatted_array,should_use_log): #initial titles at the top of the file denote 
    file_to_use = "log.txt" if should_use_log else "database.txt"
    formatting_lengths = []                    #the spaces availible for each category if the length
    formatted_array = str("")
    with open(file_to_use,"r") as file:
        formatting_lengths = get_line_formatting_length(file.readline())  #exceeds this length then append spaces to fit correctly 
    for i in range(len(unformatted_array)):
        if formatting_lengths < len(unformatted_array[i])
            #call adjustment function
        else:
            #write function that handles the formatting of the string using the amount of spaces in between them

def write_data_to_text_file(array_to_write,should_use_log):
    file_to_use = "log.txt" if should_use_log else "database.txt"
    with open(file_to_use,"w+") as file:
        if file.write(format_array_for_writing(array_to_write)) == False:
            return False

    return True

def return_parsed_data(string_to_search_for, should_use_log):
    unparsed_searched_terms = []
    file_to_use = "log.txt" if should_use_log else "database.txt"
    with open(file_to_use,"r") as file:
        for i in file:
            if string_to_search_for in i:
                unparsed_searched_terms.append(i)
    return parse_each_text_line(unparsed_searched_terms)




    
