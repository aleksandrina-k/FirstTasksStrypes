import json
from typing import Iterable


class Jsonable:
    @staticmethod
    def from_iter_to_dictionary(itr):
        result_list = []
        for el in itr:
            if isinstance(el, Jsonable):
                result_list.append(el.to_dictionary())
            else:
                result_list.append(el)
        return result_list

    @staticmethod
    def dict_to_json(d: dict):
        result_dict = {}

        for key, value in d.items():
            if isinstance(value, Jsonable):
                result_dict[key] = value.to_dictionary()
            elif isinstance(value, dict):
                result_dict[key] = Jsonable.check_dict(value)
            elif isinstance(value, Iterable) and not isinstance(value, str):
                result_dict[key] = Jsonable.from_iter_to_dictionary(value)
            else:
                result_dict[key] = value

        return result_dict

    @staticmethod
    def dict_to_obj(d: dict):
        result_dict = {}

        for key, value in d.items():
            if isinstance(value, Jsonable):
                result_dict[key] = value.to_dictionary()
            elif isinstance(value, dict):
                result_dict[key] = Jsonable.check_dict(value)
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
                dictionary["dict"][attrib] = Jsonable.dict_to_json(value)
            elif isinstance(value, Iterable) and not isinstance(value, str):
                dictionary["dict"][attrib] = Jsonable.from_iter_to_dictionary(value)
            else:
                dictionary["dict"][attrib] = value

        return dictionary

    @classmethod
    def from_json(cls, json_string: str):
        python_dict = json.loads(json_string)
        print(python_dict)
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
                var_dict = {}
                for k, v in value.items():


            elif isinstance(value, Iterable) and not isinstance(value, str):
                var_list = []
                for el in value:
                    if Jsonable.is_object(el):
                        var_list.append(Jsonable.to_object(el))

                    else:
                        var_list.append(el)
                param_values_list.append(var_list)

            else:
                param_values_list.append(value)

        return eval(obj_class)(*param_values_list)

    @staticmethod
    def is_object(variable):
        if isinstance(variable, dict):
            if "dict" in variable.keys():
                return True
        return False


class Xmlable:
    def to_xml(self):
        xml_list = [f'<{self.__class__.__name__}>']
        for param, value in self.__dict__.items():
            element = '<' + param + '>' + str(value) + '</' + param + '>'
            xml_list.append(element)

        xml_list.append(f'</{self.__class__.__name__}>')

        return ''.join(xml_list)

    @classmethod
    def from_xml(cls, xml_string):
        xml_string = xml_string.replace('<', ' ')
        xml_string = xml_string.replace('>', ' ')
        print(xml_string)
        xml_list = xml_string.split('  ')

        arg_values = []
        for attrib in xml_list[1:-1]:
            arg_values.append(attrib.split(' ')[1])

        # print(arg_values)
        try:
            new_object = eval(cls.__name__)(*arg_values)
            return new_object
        except TypeError:
            raise ValueError
        except Exception:
            print('Error')


class Panda(Jsonable, Xmlable):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


class Person(Jsonable, Xmlable):
    def __init__(self, first_name: str, last_name: str, age: int, friends: list, panda: Panda):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.friends = friends
        self.children = {'boys': {"count": 2, "children": ['plamen', 'pavel']}, 'girls': {"count": 0, "children": []}}
        self.panda = panda

    def __eq__(self, other):
        return self.first_name == other.first_name and \
               self.last_name == other.last_name and \
               self.age == other.age and \
               self.friends == other.friends and \
               self.children == other.children and \
               self.panda == other.panda


if __name__ == '__main__':
    ivcho = Panda('ivcho', 2)
    goshko = Person('goshko', 'goshev', 5, [], ivcho)
    joro = Person('joro', 'georgiev', 20, ['sasho', 'stoyan', 'svetlio', goshko], ivcho)
    joro.children["boys"]["children"].append(goshko)

    print(joro.to_json())
    new_joro = Jsonable.from_json(joro.to_json())

    # print(joro == new_joro)
