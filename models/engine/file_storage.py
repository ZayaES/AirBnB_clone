#!/usr/bin/python
"""serializes instances to a JSON file and
deserializes JSON file to instances
"""

class FileStorage:
    """serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "file.json"
    __object = {}

    def all(self):
        """Returns __object"""
        return __object
    def new(self, obj):
        """coming back"""

    def save(self):
        """Serializes __object to the json file"""

        with open(type(self).__file_path), "w") as json_file:
            json.dump(type(self).__object, json_file)

    def reload(self):
        """deserializes the JSON file
        to __objects (only if the JSON file
        (__file_path) exists ; otherwise, does nothing.
        If the file doesn’t exist, no exception is raised)
        """
        try:
            with open(type(self).__file_path), "r") as json_file:
                data = json.load(json_file)
                type(self).__object = dict(data)
        except Exception:
            pass

