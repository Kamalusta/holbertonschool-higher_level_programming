#!/usr/bin/python3
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "my_list.txt"
my_list = "kamal"
save_to_json_file(my_list, filename)
