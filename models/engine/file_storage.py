#!/usr/bin/python3

import json
import os.path


class FileStorage:

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects = {(obj.__class__.__name__).obj.id: obj}

    def save(self):
        with open("file,json", "w") as outfile:
            json.dump(self.__objects, outfile)

    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r+') as file:
                self.__object = json.load(file)
