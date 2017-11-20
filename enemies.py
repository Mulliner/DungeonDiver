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
            'health': int((12 + self.characterlevel) / 2),
            'damage': int((12 + self.characterlevel) / 3)
        }
        return stats
