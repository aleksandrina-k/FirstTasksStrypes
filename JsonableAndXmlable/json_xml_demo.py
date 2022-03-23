import json
from typing import Iterable


class NotValidObjectType(Exception):
    print("NotValidObjectType")


class Jsonable:
    # from python to json
    @staticmethod
    def from_iter_to_dictionary(itr):
        result_list = []
        for el in itr:
            if isinstance(el, Jsonable):
                result_list.append(el.to_dictionary())
            elif isinstance(el, dict):
                result_list.append(Jsonable.dict_to_json_dict(el))
            elif isinstance(el, Iterable) and not isinstance(el, str):
                result_list.append(Jsonable.from_iter_to_dictionary(el))
            else:
                result_list.append(el)
        return result_list

    @staticmethod
    def dict_to_json_dict(d: dict):
        result_dict = {}

        for key, value in d.items():
            if isinstance(value, Jsonable):
                result_dict[key] = value.to_dictionary()
            elif isinstance(value, dict):
                result_dict[key] = Jsonable.dict_to_json_dict(value)
            elif isinstance(value, Iterable) and not isinstance(value, str):
                result_dict[key] = Jsonable.from_iter_to_dictionary(value)
            else:
                result_dict[key] = value

        return result_dict

    def to_json(self, indent=4):
        dictionary = self.to_dictionary()
        return json.dumps(dictionary, indent=indent)

    def to_dictionary(self):
        dictionary = {"dict": {},
                      "type": self.__class__.__name__}

        for attrib, value in self.__dict__.items():
            if isinstance(value, Jsonable):
                dictionary["dict"][attrib] = value.to_dictionary()
            elif isinstance(value, dict):
                dictionary["dict"][attrib] = Jsonable.dict_to_json_dict(value)
            elif isinstance(value, Iterable) and not isinstance(value, str):
                dictionary["dict"][attrib] = Jsonable.from_iter_to_dictionary(value)
            else:
                dictionary["dict"][attrib] = value

        return dictionary

    # from json to python
    @staticmethod
    def get_iter_values(itr: Iterable):
        values_list = []
        for el in itr:
            if Jsonable.is_object(el):
                values_list.append(Jsonable.to_object(el))
            elif isinstance(el, dict):
                values_list.append(Jsonable.get_dict_values(el))
            elif isinstance(el, Iterable) and not isinstance(el, str):
                values_list.append(Jsonable.get_iter_values(el))
            else:
                values_list.append(el)

        return values_list

    @staticmethod
    def get_dict_values(d: dict):
        values_dict = {}

        for key, value in d.items():
            if Jsonable.is_object(value):
                values_dict[key] = Jsonable.to_object(value)
            elif isinstance(value, dict):
                values_dict[key] = Jsonable.get_dict_values(value)
            elif isinstance(value, Iterable) and not isinstance(value, str):
                values_dict[key] = Jsonable.get_iter_values(value)
            else:
                values_dict[key] = value

        return values_dict

    @staticmethod
    def is_object(variable):
        if isinstance(variable, dict):
            if "dict" in variable.keys():
                return True
        return False

    @classmethod
    def from_json(cls, json_string: str):
        python_dict = json.loads(json_string)

        if cls.__name__ != python_dict["type"]:
            raise NotValidObjectType

        object = Jsonable.to_object(python_dict)

        return object

    @classmethod
    def to_object(cls, python_dict: dict):
        obj_class = python_dict["type"]
        param_values_list = []

        for key, value in python_dict["dict"].items():
            if Jsonable.is_object(value):
                param_values_list.append(Jsonable.to_object(value))
            elif isinstance(value, dict):
                param_values_list.append(Jsonable.get_dict_values(value))
            elif isinstance(value, Iterable) and not isinstance(value, str):
                param_values_list.append(Jsonable.get_iter_values(value))
            else:
                param_values_list.append(value)

        return eval(obj_class)(*param_values_list)


# class Xmlable:
#     def to_xml(self):
#         xml_list = [f'<{self.__class__.__name__}>']
#         for param, value in self.__dict__.items():
#             element = '<' + param + '>' + str(value) + '</' + param + '>'
#             xml_list.append(element)
#
#         xml_list.append(f'</{self.__class__.__name__}>')
#
#         return ''.join(xml_list)
#
#     @classmethod
#     def from_xml(cls, xml_string):
#         xml_string = xml_string.replace('<', ' ')
#         xml_string = xml_string.replace('>', ' ')
#         print(xml_string)
#         xml_list = xml_string.split('  ')
#
#         arg_values = []
#         for attrib in xml_list[1:-1]:
#             arg_values.append(attrib.split(' ')[1])
#
#         # print(arg_values)
#         try:
#             new_object = eval(cls.__name__)(*arg_values)
#             return new_object
#         except TypeError:
#             raise ValueError
#         except Exception:
#             print('Error')


class Panda(Jsonable):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


class Person(Jsonable):
    def __init__(self, name: str, age: int, friends: list, children: dict, panda: Panda):
        self.name = name
        self.age = age
        self.friends = friends
        self.children = children
        self.panda = panda

    def __eq__(self, other):
        return self.name == other.name and \
               self.age == other.age and \
               self.friends == other.friends and \
               self.children == other.children and \
               self.panda == other.panda


if __name__ == '__main__':
    ivcho = Panda('ivcho', 2)
    ivan = Person('goshko', 5, [], {}, ivcho)
    joro = Person('joro', 20,
                  ['stoyan', 'svetlio', ivan],
                  {'boys': {"count": 3, "children": ['plamen', 'pavel', ivan]}, 'girls': {"count": 0, "children": []}}
                  , ivcho)

    # print(joro.to_json())

    new_joro = Person.from_json(ivcho.to_json())
    print(new_joro.__dict__)
