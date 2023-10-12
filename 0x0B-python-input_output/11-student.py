
#!/usr/bin/python3

class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            res = {}
            for attr in attrs:
                if attr in self.__dict__:
                    res[attr] = self.__dict__[attr]
            return res
    
    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)