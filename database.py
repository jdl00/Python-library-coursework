'''
contains common database functions such as 
1)parsing the text file and return it as an array for ease of manipulation
2)write to a the database file (txt) 
3)query database
4) the string returned from parse returns a string of id, title, Author, Purchase Date, Member ID
'''

def delete_from_text_file(string_to_delete,txt_file_to_delete_from):
    with open('file_path', 'r+') as file:
        if string_to_delete not in file:
            return 
        parsed_array = parse_text_file(txt_file_to_delete_from)
        string_to_delete = string_to_delete.lower()
        parsed_array.remove(string_to_delete)
        file.truncate(0)
        write_array_to_text_file(parsed_array,txt_file_to_delete_from)

def parse_text_file(txt_file_to_parse):
    parsed_array = []
    file = open(txt_file_to_parse,"r")
    for line in file:
        parsed_array.append(line)
    file.close()
    return parsed_array

'''
assuming that storage below is formatted such that a double space is a marker that it is at the end of the 
place holder, to make for extraction of data easier
id title  Author Purchase Date Member ID
1  BOOK 1 Tim    11/9/12       12345
'''

def format_string_for_handling(string_to_handle):
    return string_to_handle.replace(' ','|')


def parse_each_text_line(list_to_parse):
    final_parsed_array = []
    for i in list_to_parse:
        final_parsed_array.append(format_string_for_handling(i))

    return final_parsed_array

def format_array_for_writing(unformatted_string): #check the length of 
    formatted_string = str("")

def write_data_to_text_file(array_to_write,should_use_log):
    if should_use_log:
        file = open("log.txt","w")
    else:
        file = open("database.txt","w")
    file.close()

def return_parsed_data(string_to_search_for, should_use_log):
    file = None
    unparsed_searched_terms = []
    if !should_use_log:
        file = open("database.txt","r")
    else:
        file = open("log.txt","r")
    for i in file:
        if string_to_search_for in i:
            unparsed_searched_terms.append(i)
    file.close()
    return parse_each_text_line(unparsed_searched_terms)




    
