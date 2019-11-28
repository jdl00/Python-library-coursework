import database
parsed_global_data[]


def query_database_by_text(string_to_search_for,should_use_active):
	global parsed_global_data		
	parsed_global_data = extract_data_from_text_file("database.txt") if should_use_active else extract_data_from_text_file("log.txt")
	if string_to_search_for in parsed_global_data:
		return return_parsed_data(string_to_search_for,should_use_active) #should return an array and let the menu deal with formatting






	