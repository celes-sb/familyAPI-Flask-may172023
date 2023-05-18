
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [{
            "id": self._generateId(),
            "first_name": "John",
            "last_name": last_name,
            "age": 33,
            "lucky_numbers": [7, 13, 22]
        },
        {
            "id": self._generateId(),
            "first_name": "Jane",
            "last_name": last_name,
            "age": 35,
            "lucky_numbers": [10, 14, 3]
        },
        {
            "id": self._generateId(),
            "first_name": "Jimmy",
            "last_name": last_name,
            "age": 5,
            "lucky_numbers": [1]
        }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        adding_member = {}

        if 'id' in member:
            adding_member['id'] = int(member['id'])
        else:
            adding_member['id'] = self._generateId()

        adding_member['first_name'] = str(member['first_name'])
        adding_member['last_name'] = self.last_name #porque es el mismo en la flia
        adding_member['age'] = int(member['age'])
        adding_member['lucky_numbers'] = member['lucky_numbers']

        self._members.append(adding_member)
        print(adding_member) #esto ocupa un pequeno espacio de memoria

        return None #quiero que cuando termine la funcion se borren de la memoria

    def delete_member(self, id):
        # fill this method and update the return
        for position in range(len(self._members)):
            if self._members[position]["id"] == int(id):
                self._members.pop(position)
                return {"Done": True}
        return None

    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member["id"] == int(id):
                return member

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

    def update_member(self, id, member):
        for position in range(len(self._members)):
            if self._members[position]["id"] == int(id):
                self._members[position].update(member) #method update({}) for lists
                return {"Done": True}