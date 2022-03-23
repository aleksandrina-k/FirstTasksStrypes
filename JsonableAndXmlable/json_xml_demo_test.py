import unittest
from json_xml_demo import Panda, Person


class TestJsonXml(unittest.TestCase):

    def setUp(self):
        self.panda = Panda('name', 1)
        self.person = Person('firstname', 15, ['aaa', 'bbb', self.panda], {}, self.panda)
        self.panda_json_string = """{
    "dict": {
        "name": "ivcho",
        "age": 2
    },
    "type": "Panda"
}"""
        self.person_json_string = """{
    "dict": {
        "name": "joro",
        "age": 20,
        "friends": [
            "stoyan",
            "svetlio",
            {
                "dict": {
                    "name": "goshko",
                    "age": 5,
                    "friends": [],
                    "children": {},
                    "panda": {
                        "dict": {
                            "name": "ivcho",
                            "age": 2
                        },
                        "type": "Panda"
                    }
                },
                "type": "Person"
            }
        ],
        "children": {
            "boys": {
                "count": 2,
                "children": [
                    "plamen",
                    "pavel",
                    {
                        "dict": {
                            "name": "goshko",
                            "age": 5,
                            "friends": [],
                            "children": {},
                            "panda": {
                                "dict": {
                                    "name": "ivcho",
                                    "age": 2
                                },
                                "type": "Panda"
                            }
                        },
                        "type": "Person"
                    }
                ]
            },
            "girls": {
                "count": 0,
                "children": []
            }
        },
        "panda": {
            "dict": {
                "name": "ivcho",
                "age": 2
            },
            "type": "Panda"
        }
    },
    "type": "Person"
}
        """

    def test_from_json(self):
        self.assertIsInstance(Panda.from_json(self.panda_json_string), Panda)
        self.assertIsInstance(Person.from_json(self.person_json_string), Person)

    def test_to_json(self):
        self.assertIsInstance(self.panda.to_json(), str)
        self.assertIsInstance(self.person.to_json(), str)

    def test_output(self):
        self.assertRaises(ValueError, Person.from_json, self.panda_json_string)
