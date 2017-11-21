class Character:

    def __init__(self, **kwargs):
        pass

    def mage(self):
        stats = {
            'vitality': 6,
            'strength': 3,
            'dexterity': 4,
            'intelligence': 10,
            'piety': 2
        }
        abilities = [
            {
                'name': 'Fireblast',
                'damage': stats['intelligence'] * 2,
            }
        ]
        return [stats, abilities]

    def warrior(self):
        stats = {
            'vitality' : 10,
            'strength' : 8,
            'dexterity' : 4,
            'intelligence' : 1,
            'piety' : 2
        }
        return stats

    def fighter(self):
        stats = {
            'vitality': 6,
            'strength': 10,
            'dexterity': 5,
            'intelligence': 1,
            'piety': 3
        }
        return stats

    def ranger(self):
        stats = {
            'vitality' : 6,
            'strength' : 5,
            'dexterity' : 10,
            'intelligence' : 3,
            'piety' : 1
        }
        return stats

    def paladin(self):
        stats = {
            'vitality': 10,
            'strength': 5,
            'dexterity': 3,
            'intelligence': 1,
            'piety': 6
        }
        return stats

    def cleric(self):
        stats = {
            'vitality': 6,
            'strength': 3,
            'dexterity': 4,
            'intelligence': 2,
            'piety': 10
        }
        return stats
