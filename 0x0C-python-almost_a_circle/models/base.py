#!/usr/bin/python3
"""
Class Base
"""
import json


class Base:
    """
    Class Base
    """
    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        return the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return("[]")
        else:
            return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        that writes the JSON string representation
        of list_objs to a file:
        """
        filename = cls.__name__
        filename = filename + ".json"
        with open(filename, mode="w") as myFile:
            if list_objs is None:
                myFile.write("[]")
            else:
                lists = [index.to_dictionary() for index in list_objs]
                myFile.write(Base.to_json_string(lists))

    @staticmethod
    def from_json_string(json_string):
        """
        that returns the list of the JSON string
        representation json_string:
        """
        if json_string is None or json_string == "[]":
            return([])
        else:
            return(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
        that returns an instance with all attributes already set:
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_obj = cls(1, 1)
            else:
                new_obj = cls(1)
            new_obj.update(**dictionary)
            return(new_obj)

    @classmethod
    def load_from_file(cls):
        """
        that returns a list of instances:
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, mode="r") as myFile:
                lists = Base.from_json_string(myFile.read())
                return([cls.create(**dicti) for dicti in lists])
        except IOError:
            return([])
