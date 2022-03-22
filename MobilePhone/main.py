import csv
from typing import List


class Keyboard:
    buttons = {0: [' '], 2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'],
               4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'],
               6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'],
               8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}

    @staticmethod
    def counting_repeated_numbers(list_: list) -> List:
        counter = 1
        list_of_tuples = []
        # list_of_tuples.append((element, counter))
        for idx, element in enumerate(list_):
            is_last_element = idx == len(list_) - 1

            if is_last_element:
                list_of_tuples.append((list_[idx], counter))
            elif list_[idx] == list_[idx + 1]:
                counter += 1
            else:
                list_of_tuples.append((list_[idx], counter))
                counter = 1
        return list_of_tuples

    @classmethod
    def keyboard_message(cls, numbers: list):
        message = ""

        list_of_tuples = cls.counting_repeated_numbers(numbers)
        filtered_list = filter(lambda x: x[0] != -1, list_of_tuples)

        for (number, count) in filtered_list:
            number_presses = len(cls.buttons[number])
            selected_letter = count % number_presses - 1
            message += cls.buttons[number][selected_letter]

        return message


class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def instantiate_from_csv(self, file_name: str):
        with open(file_name, 'r') as f:
            reader = csv.DictReader(f)
            contacts_list = list(reader)

            for contact in contacts_list:
                key = contact['name']
                value = contact.get('phone_number')
                self.contacts[key] = value

    def get_contact_info(self, contact_name: str):
        if contact_name in self.contacts:
            return f"{contact_name}: {self.contacts.get(contact_name)}"
        else:
            return None


class Phone(PhoneBook, Keyboard):
    def __init__(self):
        # PhoneBook.__init__(self)
        super().__init__()


if __name__ == '__main__':
    phone1 = Phone()
    phone1.instantiate_from_csv('contacts.csv')
    print(phone1.contacts)

    contact_to_search = 'Georgi'
    print(phone1.get_contact_info(contact_to_search))

    print(Phone.keyboard_message([2, -1, 2, 2, -1, 2, 2, 2, 2]))
