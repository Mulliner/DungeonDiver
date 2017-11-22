class Enemies:

    def __init__(self, **kwargs):
        self.characterlevel = kwargs['characterlevel']

    def skeleton(self):
        stats = {
            'name': 'Skeleton',
            'health': int((5 + self.characterlevel) / 2),
            'damage': int((5 + self.characterlevel) / 3)
        }
        return stats

    def bat(self):
        stats = {
            'name': 'Bat',
            'health': int((4 + self.characterlevel) / 2),
            'damage': int((2 + self.characterlevel) / 3)
        }
        return stats

    def ogre(self):
        stats = {
            'name': 'Ogre',
            'health': int((12 + self.characterlevel)),
            'damage': int((12 + self.characterlevel) / 3.5)
        }
        return stats

    def wolf(self):
        stats = {
            'name': 'Wolf',
            'health': int((5 + self.characterlevel) / 2),
            'damage': int((6 + self.characterlevel) / 2.1)
        }
        return stats

    def cougar(self):
        stats = {
            'name': 'Cougar',
            'health': int((7 + self.characterlevel) / 2),
            'damage': int((9 + self.characterlevel) / 1.7)
        }
        return stats

    def rabidsquirrel(self):
        stats = {
            'name': 'Rabid Squirrel',
            'health': int((4 + self.characterlevel) / 2),
            'damage': int((3 + self.characterlevel) / 3)
        }
        return stats

    def alphawolf(self):
        stats = {
            'name': 'Alpha Wolf',
            'health': int((12 + self.characterlevel)),
            'damage': int((14 + self.characterlevel) / 1.2)
        }
        return stats
