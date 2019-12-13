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
    active_database = parse_text_file(False)
    mid_count_array = [0]*len(active_database)
    finalised_array = []
    temp_parsed_array = []
    return_array = []
    for i in range(len(array_to_sort)):
        temp_parsed_array = parse_text_line(array_to_sort[i])
        if temp_parsed_array[3] == "checkout":
            index_to_use = int(temp_parsed_array[1])
            mid_count_array[index_to_use] = mid_count_array[index_to_use] + 1

    for i in range (len(mid_count_array)):
        temp_parsed_array = parse_text_line(active_database[i])
        finalised_array.append([mid_count_array,temp_parsed_array[1]])


    finalised_array.sort(key = lambda x: x[0])

    for i in finalised_array:
        return_array.append(i[1])

    return return_array

#print(sort_list_by_most_taken_out(["1456|1|2019-12-13|checkout|","1456|2|2019-12-13|checkout|","1456|1|2019-12-13|checkout|"])) test code





def get_month(string_to_get):
    return string_to_get[5:7]

#get_month 2019-12-13 test data

def sort_list_by_date(array_to_sort):
    current_date = datetime.today().strftime('%m') #get the current month
    temp_parsed_line = []
    final_parsing_line = []
    month_difference = int(0)
    active_database = parse_text_file(False)
    temp_variable_storage = str("")
    return_array = []
    for i in array_to_sort:
        temp_parsed_line = parse_text_line(i) #calculate the difference between them
        record_month = get_month(temp_parsed_line[2])
        if record_month > current_date:
            month_difference = int(record_month) - int(current_date)
        else:
            month_difference = int(current_date) - int(record_month)

        final_parsing_line.append([month_difference,temp_parsed_line[1]]) 

    final_parsing_line.sort(key = lambda x: x[0])
    for i in range(len(final_parsing_line)): #associate each of the ids to the book name
        temp_variable_storage = final_parsing_line[i]
        for y in active_database:
            temp_parsed_line = parse_text_line(y)
            if temp_parsed_line[0] == temp_variable_storage[1]:
                return_array.append(temp_parsed_line[1])


    return return_array

#print(sort_list_by_date(["1456|1|2019-12-13|checkout|","1456|2|2019-12-13|checkout|","1456|1|2019-12-13|checkout|"]))  #test data



def determine_popularity_of_books():
    most_taken_out = []
    most_popular_for_current_season = []
    temp_string_storage = str("")
    sum_score = int(0)
    adjustment = int(0)
    log_book = parse_text_file(True)
    final_popularity_array = [""] * (len(log_book)*2)
    most_taken_out = sort_list_by_most_taken_out(log_book)
    most_popular_for_current_season = sort_list_by_date(log_book)        

    for i in range(len(most_taken_out)): #use a rating system to judge which books have been most succesful based on their index in the respective lists
        if most_taken_out[i] in most_popular_for_current_season:
            sum_score = i + most_popular_for_current_season.index(most_taken_out[i])
            final_popularity_array[sum_score] = most_taken_out[i]
        else:
            final_popularity_array.append(most_taken_out[i])
        
    formatted_list = [x for x in final_popularity_array if x]
    
    return formatted_list

print(determine_popularity_of_books())
