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

def parse_text_line(string_to_parse):
    final_parsed_array = []
    temp_string_handler = str("")
    temp_string_data_handler = str("")
    for i in string_to_parse:
        if temp_string_handler == "id":
            if temp_string_data_handler[len(temp_string_data_handler) - 3:len(temp_string_data_handler)] != "tit":
                final_parsed_array.append(temp_string_data_handler)
                temp_string_handler = temp_string_data_handler[len(temp_string_data_handler) - 3:len(temp_string_data_handler)]


        else:
            temp_string_handler += i 

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

def parse_text_file(txt_file_to_parse):
    parsed_array = []
    file = open(txt_file_to_parse,"r")
    for i in file:
        parsed_array.append(i)
    file.close()
    return parsed_array
    
