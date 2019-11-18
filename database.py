'''
contains common database functions such as 
1)parsing the text file and return it as an array for ease of manipulation
2)write to a the database file (txt) 
3)query database

'''

def query_database(string string_to_search_for,string txt_file_to_search):
    parsed_array = parse_text_file(txt_file_to_search)
    for i in parsed_array:
        if i.lower() == string_to_search_for.lower():
            return true
    return false

def delete_from_text_file(string string_to_delete, string txt_file_to_delete_from):
    found_record_line = None #dont want to use an int which could possibly remove a valid record
    parsed_array = parse_text_file(txt_file_to_delete_from)
    string_to_delete = string_to_delete.lower()
    for i in range(parsed_array.len()):
        if parsed_array[i].lower() == string_to_delete.lower():
            found_record_line = i
    file = open(txt_file_to_delete_from,"a")
    
    file.close()

def write_to_text_file(string string_to_write,string txt_file_to_write):
    string_to_write += "\n"
    file = open(txt_file_to_write,"w")
    file.write(string_to_write)
    file.close()
    


def parse_text_file(string txt_file_to_parse):
    parsed_array = []
    file = open(txt_file_to_parse,"r")
    for i in file:
        parsed_array.append(i)
    file.close()
    return parsed_array
    
