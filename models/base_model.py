#!/usr/bin/python3

"""Defines all common attributes/methods for other classes """

import uuid
import cmd
import datetime
import json

class BaseModel:
    """The superclass for other classes. 
    Containes attributes and methods general
    to all instances.
    """

    id = str(uuid.uuid4())
    created_at = datetime.datetime.now()
    updated_at = created_at

    def __init__(self):
        """Initalizes an instance of any
        object that inherits this class
        """


    def __str__(self):
        """Format "print" function for this class"""

        dicts = {k:v for k, v in type(self).__dict__.items()if not
                k.startswith("_") and not callable(v)}
        return "[BaseModel] ({}) {}".format(self.id, dicts)

    def save(self):
        """Updates the updated_at attribute with the current datetime"""

        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dictionary containing all key-value pairs of __dict__
        of the instance
        """

        d = {k:v for k, v in self.__dict__.items() if not k.startswith('_') and not callable(v)}
        my_dict = d.copy()
        my_dict["id"] = type(self).id
        my_dict["created_at"] = type(self).created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["__class__"] = type(self).__name__
#        my_dict_json = json.dumps(my_dict)

        return my_dict
