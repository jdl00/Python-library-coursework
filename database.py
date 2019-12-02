'''
contains common database functions such as
1)parsing the text file and return it as an array for ease of manipulation
2)write to a the database file (txt)
3)query database
4) the string returned from parse returns a string of id, title, Author, Purchase Date, Member ID
'''

'''
assuming that storage below is formatted we can replace the spaces used with a symbol thats typically
not used with the sample data to ease with extraction of data
id title  Author Purchase Date Member ID
1  BOOK 1 Tim    11/9/12       12345
such that it becomes
1|BOOK 1|Tim|11/9/12|12345

we must also consider that book titles may have a space therefor we can use an escape character such as ~
to mark there should be a space to ensure the book name is properly formattedsss
'''





def delete_from_text_file(string_to_delete,should_use_log):
    file_to_use = "log.txt" if should_use_log else "database.txt"
    with open('file_path', 'r+') as file:
        if string_to_delete not in file:
            return False
        parsed_array = parse_text_file(file_to_use)
        string_to_delete = string_to_delete.lower()
        parsed_array.remove(string_to_delete)
        file.truncate(0) #clear the contents of the file and re-write it without the data to be removed
        write_array_to_text_file(format_array_for_writing(parsed_array),file_to_use) #need to re-format array before writing
    return True


def parse_text_file(should_use_log):
    parsed_array = []
    file_to_use = "log.txt" if should_use_log else "database.txt"
    with open(file_to_use,"r"):
        for line in file: #neglected to use readline due to its inefficiency of large files
            parsed_array.append(line)
    return parsed_array

'''
need to re-do to include further fuctionality for book names which include a space / author aswell
'''

def format_string_for_handling(string_to_handle):
    string_to_handle = string_to_handle" ".join(string_to_handle.split())
    string_to_handle = string_to_handle.replace(' ','|')
    string_to_handle = string_to_handle.replace('~',' ')
    return string_to_handle #the output will handle the |


def parse_each_text_line(unparsed_searched_terms):
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

def adjust_file_for_formatting(unformatted_array_lengths,should_use_log):
    file_to_use = "log.txt" if should_use_log else "database.txt"
    with open(file_to_use, "w+") as file:
        print("hello")



def format_array_for_writing(unformatted_array,should_use_log): #initial titles at the top of the file denote
    file_to_use = "log.txt" if should_use_log else "database.txt"
    formatting_lengths = []                    #the spaces availible for each category if the length
    formatted_array = str("")
    final_formatted_string = str("")
    with open(file_to_use,"r") as file:
        formatting_lengths = get_line_formatting_length(file.readline())  #exceeds this length then append spaces to fit correctly
    for i in range(len(unformatted_array)):
        if formatting_lengths[i] < len(unformatted_array[i])
            #call adjustment function
        else:
            #write function that handles the formatting of the string using the amount of spaces in between them
    return final_formatted_string

def write_data_to_text_file(array_to_write,should_use_log):
    file_to_use = "log.txt" if should_use_log else "database.txt"
    with open(file_to_use,"w+") as file:
        return file.write(format_array_for_writing(array_to_write))

def return_parsed_data(string_to_search_for, should_use_log):
    unparsed_searched_terms = []
    file_to_use = "log.txt" if should_use_log else "database.txt"
    with open(file_to_use,"r") as file:
        for i in file:
            if string_to_search_for in i:
                unparsed_searched_terms.append(i)
    return parse_each_text_line(unparsed_searched_terms)
