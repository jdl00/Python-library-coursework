from datetime import datetime
from database import *

active_book = []
log_book = []

'''
using log we can associate certain books to certain seasons of popularity
we can also associate books with frequent check outs of a long duration
in that order
query the database on whether a book has historically
been more popular within a season and check that against the current amount of check outs to
predict whether itll be a popular book
also the frequency of which the book is on loan
'''

def sort_list(array_to_sort):
    array_to_sort.sort(key = lambda x: x[1])
    return array_to_sort

def determine_popularity_of_books():
    global log_book
    currentdate = datetime.today().strftime('%Y-%m-%d')
    most_taken_out = []
    most_popular_for_current_season = []
    newest_books = []
    temp_string_storage = str("")
    temp_num_storage = int(0)
    log_book = parse_text_file(True)
    final_popularity_array = [""] * (len(most_taken_out)*3)


    for i in range(len(most_taken_out)):
        temp_string_storage = most_taken_out[i]
        temp_num_storage = most_popular_for_current_season.index(temp_string_storage) + i + newest_books.index(temp_string_storage)
        final_popularity_array[temp_num_storage]
