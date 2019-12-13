from database import *


def query_database_by_text(string_to_search_for):
        selected_data = []
        unparsed_data = parse_text_file(False)
        for i in unparsed_data:
                if parse_text_line(i)[1].lower() == string_to_search_for.lower():
                        selected_data.append(i[:-2])


        return selected_data

#query_database_by_text("Harry PoTter") test data
