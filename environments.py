import random
from enemies import Enemies


class Environments:

    def __init__(self, level):
        self.enemies = Enemies(characterlevel=level)

    def dungeon(self):
        mobs = list()
        boss = self.enemies.ogre()

        for i in range(2, 8):
            mobs.append(self.enemies.skeleton())
        for i in range(5, 17):
            mobs.append(self.enemies.bat())

        objtoreturn = {
            'name': 'Dungeon',
            'mobs': mobs,
            'boss': boss
        }

        return objtoreturn
