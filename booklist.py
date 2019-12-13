from datetime import datetime
from database import *

active_book = []
log_book = []

'''
using log we can associate certain books to certain seasons of popularity
and being taken out
in that order
query the database on whether a book has historically
been more popular within a season and check that against the current amount of check outs to
predict whether itll be a popular book
'''

def sort_list_by_most_taken_out(array_to_sort):
    index_based = [0] *len(array_to_sort)
    return_array = []
    count = 0
    parsed_line = str("")
    for i in range(len(array_to_sort)):
        parsed_line = parse_text_line(array_to_sort[i])
        if parsed_line[3] == "checkout":
            index_based[i] +=1
    for i in array_to_sort:
        count+=1
        parsed_line = parse_text_line(array_to_sort[i])
        return_array.append([parsed_line[2],index_based[count]])

    return_array.sort(key = lambda x: x[1])

sort_list_by_most_taken_out(["1456|1|2019-12-13|checkout|","1456|2|2019-12-13|checkout|","1456|1|2019-12-13|checkout|"])

def associate_index_to_book(data_to_process,array_being_used):
    parsed_data = []


def get_month(string_to_get):
    return string_to_get[5:7]

#get_month 2019-12-13 test data

def sort_list_by_date(array_to_sort):
    current_date = datetime.today().strftime('%m')
    temp_parsed_line = []
    final_parsing_line = []
    month_difference = int(0)
    for i in array_to_sort:
        temp_parsed_line = parse_text_line(i)
        record_month = get_month(temp_parsed_line[2])
        if record_month > current_date:
            month_difference = int(record_month) - int(current_date)
        else:
            month_difference = int(current_date) - int(record_month)

        final_parsing_line.append([month_difference,temp_parsed_line[1]])

    final_parsing_line.sort(key = lambda x: x[0])

    return final_parsing_line

#sort_list_by_date(["1456|1|2019-12-13|checkout|","1456|2|2019-12-13|checkout|","1456|1|2019-12-13|checkout|"])  test data



def determine_popularity_of_books():
    most_taken_out = []
    most_popular_for_current_season = []
    temp_string_storage = str("")
    temp_num_storage = int(0)
    log_book = parse_text_file(True)
    final_popularity_array = [""] * (len(most_taken_out)*3)
    most_taken_out = sort_list(log_book)

    print(most_taken_out)
