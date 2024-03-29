#!/usr/bin/python3
''' add arguments to a list'''
import sys
import json
import os
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


listarg = list(sys.argv[1:])
if not os.path.exists("add_item.json"):
    save_to_json_file(listarg, "add_item.json")
else:
    list = load_from_json_file("add_item.json")
    list += listarg[:]
    save_to_json_file(list, "add_item.json")
