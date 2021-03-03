'''
The following classes are implemented in the module:
Room, Character, Enemy, Friend, Subject.
These are used for implementation of simple walking game.
'''

from typing import List, Type, Dict, Optional

class Room:
    """
    Room can contain enemies, items and is linked to other rooms
    """

    def __init__(self, name: str) -> 'Room':
        self.name = name
        self.character = self.item = self.description = None
        self.directions = {}

    def set_description(self, message: str): 
        """Adds a description to a room
        Args:
            message (str)
        """

        self.description = message

    def set_character(self, character: Type['Chatacter']):
        """ Adds an enemy to a room

        Args:
            character (Type['Character'])
        """

        self.character = character

    def get_character(self) -> Type['Enemy']:
        """
        Returns an Enemy instance
        """

        return self.character

    def set_item(self, item: Type['Item']):
        """setter"""

        self.item = item

    def get_item(self) -> Type['Item']:
        return self.item

    def link_room(self, other_room: Type['Room'], direction: str):
        self.directions[direction] = other_room

    def get_details(self):
        print(self.name)
        print('--------------------')
        print(self.description)
        for direction in self.directions:
            try:
                print(f'The {self.directions[direction].name} is {direction}')
            except KeyError: continue

    def move(self, direction: str):
        try:
            return self.directions[direction]
        except KeyError:
            print(f'The entrance to {direction} direction is covered with stones...')
            return self

    def __repr__(self):
        return f'Room({self.name}, {self.description}, {self.character}, {self.item})'


class Item:
    def __init__(self, name: str):
        self.name = name
        self.description = None

    def set_description(self, description: str):
        self.description = description

    def get_name(self):
        return self.name

    def describe(self):
        print(f'The {self.name} is here - {self.description}')


class Character:
    def __init__(self, name: str, description: str=''):
        self.name = name
        self.description = description
        self.message = self.weakness = None

    def set_conversation(self, message: str):
        self.message = message

    def set_weakness(self, weakness: str):
        self.weakness = weakness

    def describe(self):
        print(f'{self.name} is here!')
        print(f'{self.description}')

    def talk(self):
        print(f'{self.name} says: {self.message}')


class Enemy(Character):

    defeated: int = 0
    def __init__(self, name: str, description: str):
        super().__init__(name, description)

    def fight(self, fight_with: str=None) -> bool:
        if fight_with == self.weakness:
            Enemy.defeated += 1
            return True

        return False

    def get_defeated(self):
        return self.defeated
