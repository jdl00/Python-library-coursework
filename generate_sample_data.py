import json as js
import random as rand
'''
we create a class which deals with the write functions 
and the generate functions along with allignement and 
JSON parsing
'''
class data_generator:
	def __init__(self):
		self.__num_data_entries__ = int(0)
		self.__sample_names__ = []

	def write_line(self,string_to_write):

	def generated_sample_data(self):
		instantised_data = str("")
		name = parse_JSON()[rand.randint(0,100)]

		return instantised_data

	def parse_JSON(self):

	def write_sample_data(self):
		try:
			self.__num_data_entries__ = int(input("enter number of entries to enter"))
		except:
			raise Exception("non natural number entered ") 

		for i in range(self.__num_data_entries__):
			write_line(self,generated_sample_data(self))



def main():
   sample_data_generator = data_generator()
   sample_data_generator.write_sample_data()

if __name__ == "__main__":
    main()
	
	