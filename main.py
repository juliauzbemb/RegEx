import re
from pprint import pprint
import csv

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


def get_new_contacts_list(data):
    search_pattern = \
        r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*' \
        r'(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
    sub_pattern = r'+7(\2)\3-\4-\5 \6\7'
    updated_list = []
    for element in data:
        full_name = ' '.join(element[:3]).split(' ')
        result = [full_name[0], full_name[1], full_name[2],
                  element[3], element[4],
                  re.sub(search_pattern, sub_pattern, element[5]).strip(),
                  element[6]]
        updated_list.append(result)
    contact_dict = {}
    for contact in updated_list:
        if contact[0] in contact_dict:
            value = contact_dict[contact[0]]
            for i in range(len(value)):
                if contact[i]:
                    value[i] = contact[i]
        else:
            contact_dict[contact[0]] = contact
    return list(contact_dict.values())


if __name__ == "__main__":
    new_contacts_list = get_new_contacts_list(contacts_list)
    pprint(new_contacts_list)
    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(new_contacts_list)
