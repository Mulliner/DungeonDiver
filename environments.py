import random
from enemies import Enemies


class Environments:

    def __init__(self, level):
        self.enemies = Enemies(characterlevel=level)

    def dungeon(self):
        mobs = list()
        boss = self.enemies.ogre()

        skeletoncount = random.randint(2, 9)
        batcount = random.randint(5, 18)

        for i in range(skeletoncount):
            mobs.append(self.enemies.skeleton())
        for i in range(batcount):
            mobs.append(self.enemies.bat())

        objtoreturn = {
            'name': 'Dungeon',
            'mobs': mobs,
            'boss': boss
        }

        return objtoreturn

    def forest(self):
        mobs = list()
        boss = self.enemies.alphawolf()

        squirrelcount = random.randint(5, 13)
        wolfcount = random.randint(5, 12)
        cougercount = random.randint(1, 4)

        for i in range(squirrelcount):
            mobs.append(self.enemies.rabidsquirrel())
        for i in range(wolfcount):
            mobs.append(self.enemies.wolf())
        for i in range(bearcount):
            mobs.append(self.enemies.couger())

        objtoreturn = {
            'name': 'Forest',
            'mobs': mobs,
            'boss': boss
        }

        return objtoreturn
