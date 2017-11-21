class Character:

    def __init__(self, **kwargs):
        pass

    def mage(self):
        basestats = {
            'vitality': 6,
            'strength': 3,
            'dexterity': 4,
            'intelligence': 10,
            'piety': 2
        }
        combatstats = {
            'basedamage' : round(basestats['intelligence'] * 1.4)
        }
        abilities = {
            'fireball': {'damage': round(combatstats['basedamage'] * 2), 'cost': 3},
            'manawall': basestats['vitality'] * .5
        }
        return basestats, combatstats, abilities

    def warrior(self):
        basestats = {
            'vitality' : 10,
            'strength' : 8,
            'dexterity' : 4,
            'intelligence' : 1,
            'piety' : 2
        }
        combatstats = {
            'basedamage' : round((basestats['vitality'] + basestats['strength']) * .4)
        }
        abilities = {
            'overwhelm': {'damage': round(combatstats['basedamage'] * 1.4)}
        }
        return basestats, combatstats, abilities

    def fighter(self):
        basestats = {
            'vitality': 6,
            'strength': 10,
            'dexterity': 5,
            'intelligence': 1,
            'piety': 3
        }
        combatstats = {
            'basedamage' : round(basestats['strength'] * 1.3)
        }
        abilities = {
            'brutalize': {'damage': round(combatstats['basedamage'] * 1.8)}
        }
        return basestats, combatstats, abilities
    def ranger(self):
        basestats = {
            'vitality' : 6,
            'strength' : 5,
            'dexterity' : 10,
            'intelligence' : 3,
            'piety' : 1
        }
        combatstats = {
            'basedamage' : round(basestats['dexterity'] * 1.2)
        }
        abilities = {
            'assassinate': {'damage': round(combatstats['basedamage'] * 2.4)}
        }
        return basestats, combatstats, abilities

    def paladin(self):
        basestats = {
            'vitality': 10,
            'strength': 5,
            'dexterity': 3,
            'intelligence': 1,
            'piety': 6
        }
        combatstats = {
            'basedamage' : round((basestats['vitality'] + basestats['piety']) * .35)
        }
        abilities = {
            'smite': {'damage': round(combatstats['basedamage'] * 1.8)}
        }
        return basestats, combatstats, abilities

    def cleric(self):
        basestats = {
            'vitality': 6,
            'strength': 3,
            'dexterity': 4,
            'intelligence': 2,
            'piety': 10
        }
        combatstats = {
            'basedamage' : round(basestats['piety'] * .9)
        }
        abilities = {
            'holy': {'damage': round(combatstats['basedamage'] * 3)}
        }
        return basestats, combatstats, abilities
