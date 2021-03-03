'''
 В модулях повинні бути реалізовані наступні класи: Кімната, Персонаж, Ворог, Товариш, Предмет.
Протокол (файл log.txt) одного сеансу гри також може допомогти успішно виконати це завдання.
'''

from typing import List, Type, Dict, Optional

current_room = ''

class Room:
    def __init__(self, name: str,
                characters: List[Type['Character']]=[],
                items: List[Type['Item']]=[],
                directions: Dict[str, str]={}):
        self.name = name
        self.character = None
        self.item = None
        self.directions = directions
        self.description = None

    def set_description(self, message: str): 
        self.description = str(message)

    def set_character(self, character: Type['Chatacter']):
        self.character = character

    def get_character(self):
        """ As far as I see, the rule is that each room has only one character

        Returns:
            [type]: [description]
        """
        return self.character

    def set_item(self, item: Type['Item']):
        self.item = item

    def get_item(self):
        return self.item

    def link_room(self, other_room: Type['Room'], direction: str):
        self.directions[direction] = other_room

    def get_details(self):
        for key in self.__dict__:
            print(self.__dict__[key])

    def move(self, direction: str):
        try:
            return self.directions[direction]
        except KeyError:
            return current_room

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
        return self.description

class Character:
    def __init__(self, name: str, description: str='', lives: int=3):
        self.name = name
        self.description = description
        self.lives = lives
        self.message = None
        self.weakness = None

    def set_conversation(self, message: str):
        self.message = message

    def set_weakness(self, weakness: str):
        self.weakness = weakness


    def describe(self):
        return self.description

    def talk(self):
        print(self.message)

class Hero(Character):
    def __init__(self, lives: int=3, 
                backpack: List[Type['Item']]=[]):
        super().__init__(lives=lives)
        self.backpack = backpack

class Enemy(Character):
    defeated: int = 0
    def __init__(self, name: str, description: str):
        super().__init__(name, description)


    def fight(self, fight_with: Optional[Type['Item']]=None) -> bool:
        if fight_with == self.weakness:
            self.defeated += 1
            return True

        return False

    def get_defeated(self):
        return self.defeated


class Friend(Character):
    def __init__(self, mame: str, description: str,
                item_to_give: Type['Item'], lives: int=3):
        super().__init__(name, description, lives=lives)
        self.item_to_give = item_to_give

class GameField:
    def __init__(self, rooms: Optional[List[Type['Room']]]=None,
                    current_room: Optional[Type['Room']]=None):
        self.rooms = rooms
        self.current_room = current_room

    def add_room(self, room: Type['Room']):
        self.rooms.append(room)

    def set_current_room(self, room: Type['Room']):
        self.current_room = current_room
