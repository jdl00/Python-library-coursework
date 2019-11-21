'''
contains common database functions such as 
1)parsing the text file and return it as an array for ease of manipulation
2)write to a the database file (txt) 
3)query database
4) the string returned from parse returns a string of id, title, Author, Purchase Date, Member ID
'''

def query_database(string_to_search_for,txt_file_to_search):
    parsed_array = parse_text_file(txt_file_to_search)
    for i in parsed_array:
        if i.lower() == string_to_search_for.lower():
            return true
    return false

def delete_from_text_file(string_to_delete,txt_file_to_delete_from):
    if query_database(string_to_delete,txt_file_to_delete_from)
        return   
    parsed_array = parse_text_file(txt_file_to_delete_from)
    string_to_delete = string_to_delete.lower()
    parsed_array.remove(string_to_delete)
    file = open(txt_file_to_delete_from,"r+")
    file.truncate(0)
    file.close()
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
def parse_each_text_line(string_to_parse):
    final_parsed_array = []
    previous_char = char('')
    temp_string_data_handler = str("")
    string_to_parse+="  "
    for i in string_to_parse:
        if i == " " and previous_char == " ":
            final_parsed_array.append(temp_string_data_handler)
            temp_string_data_handler = ""   
        else:
            temp_string_data_handler += i

    return final_parsed_array


def write_array_to_text_file(array_to_write,txt_file_to_write):
    file = open(txt_file_to_write,"w")
    for i in array_to_write:
        file.write(i+'\n')
    file.close()


def write_to_text_file(string_to_write,txt_file_to_write):
    string_to_write += "\n"
    file = open(txt_file_to_write,"w")
    file.write(string_to_write.lower())
    file.close() 

def extract_data_from_text_file(txt_file_to_parse):
    final_extracted_array = []
    parsed_array = parse_each_text_line(parse_text_file(txt_file_to_parse))
    return parsed_array



    
