import math


class Character:

    def __init__(self, **kwargs):
        pass

    def mage(self, basestats=None):
        if not basestats:
            basestats = {
                'vitality': 6,
                'strength': 3,
                'dexterity': 4,
                'intelligence': 10,
                'piety': 2
            }
        maxstats = {
            'health': math.floor(basestats['vitality'] * .90),
            'stamina': round(basestats['vitality'] / 3) +
                       round(basestats['strength'] / 3) +
                       round(basestats['dexterity'] / 3),
            'mana': round(basestats['intelligence'] * .90),
        }
        scalingstats = {
            'health': math.floor(basestats['vitality'] * .90),
            'stamina': round(basestats['vitality'] / 3) +
                       round(basestats['strength'] / 3) +
                       round(basestats['dexterity'] / 3),
            'mana': round(basestats['intelligence'] * .90),
        }
        combatstats = {
            'basedamage' : round(basestats['intelligence'] * 1.4)
        }
        abilities = {
            'fireball': {'damage': round(combatstats['basedamage'] * 2),
                         'cost': 3,
                         'costtype': 'mana',
                         'abilitytype': 'damage'},
            'manawall': {'buff': basestats['vitality'] * .5,
                         'cost': 3,
                         'costtype': 'mana',
                         'abilitytype': 'buff'}
        }
        return basestats, combatstats, abilities, scalingstats, maxstats

    def warrior(self, basestats=None):
        if not basestats:
            basestats = {
                'vitality' : 10,
                'strength' : 8,
                'dexterity' : 4,
                'intelligence' : 1,
                'piety' : 2
            }
        maxstats = {
            'health': math.floor(basestats['vitality'] * .90),
            'stamina': round(basestats['vitality'] / 3) +
                       round(basestats['strength'] / 3) +
                       round(basestats['dexterity'] / 3),
            'mana': round(basestats['intelligence'] * .90),
        }
        scalingstats = {
            'health': math.floor(basestats['vitality'] * .90),
            'stamina': round(basestats['vitality'] / 3) +
                       round(basestats['strength'] / 3) +
                       round(basestats['dexterity'] / 3),
            'mana': round(basestats['intelligence'] * .90),
        }
        combatstats = {
            'basedamage' : round((basestats['vitality'] + basestats['strength']) * .4)
        }
        abilities = {
            'overwhelm': {'damage': round(combatstats['basedamage'] * 1.4),
                          'cost': 3,
                          'costtype': 'stamina',
                          'abilitytype': 'damage'}
        }
        return basestats, combatstats, abilities, scalingstats, maxstats

    def fighter(self, basestats=None):
        if not basestats:
            basestats = {
                'vitality': 6,
                'strength': 10,
                'dexterity': 5,
                'intelligence': 1,
                'piety': 3
            }
        maxstats = {
            'health': math.floor(basestats['vitality'] * .90),
            'stamina': round(basestats['vitality'] / 3) +
                       round(basestats['strength'] / 3) +
                       round(basestats['dexterity'] / 3),
            'mana': round(basestats['intelligence'] * .90),
        }
        scalingstats = {
            'health': math.floor(basestats['vitality'] * .90),
            'stamina': round(basestats['vitality'] / 3) +
                       round(basestats['strength'] / 3) +
                       round(basestats['dexterity'] / 3),
            'mana': round(basestats['intelligence'] * .90),
        }
        combatstats = {
            'basedamage' : round(basestats['strength'] * 1.3)
        }
        abilities = {
            'brutalize': {'damage': round(combatstats['basedamage'] * 1.8),
                          'cost': 3,
                          'costtype': 'stamin',
                          'abilitytype': 'damage'},
        }
        return basestats, combatstats, abilities, scalingstats, maxstats
    def ranger(self, basestats=None):
        if not basestats:
            basestats = {
                'vitality' : 6,
                'strength' : 5,
                'dexterity' : 10,
                'intelligence' : 3,
                'piety' : 1
            }
        maxstats = {
            'health': math.floor(basestats['vitality'] * .90),
            'stamina': round(basestats['vitality'] / 3) +
                       round(basestats['strength'] / 3) +
                       round(basestats['dexterity'] / 3),
            'mana': round(basestats['intelligence'] * .90),
        }
        scalingstats = {
            'health': math.floor(basestats['vitality'] * .90),
            'stamina': round(basestats['vitality'] / 3) +
                       round(basestats['strength'] / 3) +
                       round(basestats['dexterity'] / 3),
            'mana': round(basestats['intelligence'] * .90),
        }
        combatstats = {
            'basedamage' : round(basestats['dexterity'] * 1.2)
        }
        abilities = {
            'assassinate': {'damage': round(combatstats['basedamage'] * 2.4),
                            'cost': 3,
                            'costtype': 'stamina',
                            'abilitytype': 'damage'},
        }
        return basestats, combatstats, abilities, scalingstats, maxstats

    def paladin(self, basestats=None):
        if not basestats:
            basestats = {
                'vitality': 10,
                'strength': 5,
                'dexterity': 3,
                'intelligence': 1,
                'piety': 6
            }
        maxstats = {
            'health': math.floor(basestats['vitality'] * .90),
            'stamina': round(basestats['vitality'] / 3) +
                       round(basestats['strength'] / 3) +
                       round(basestats['dexterity'] / 3),
            'mana': round(basestats['intelligence'] * .90),
        }
        scalingstats = {
            'health': math.floor(basestats['vitality'] * .90),
            'stamina': round(basestats['vitality'] / 3) +
                       round(basestats['strength'] / 3) +
                       round(basestats['dexterity'] / 3),
            'mana': round(basestats['intelligence'] * .90),
        }
        combatstats = {
            'basedamage' : round((basestats['vitality'] + basestats['piety']) * .35)
        }
        abilities = {
            'smite': {'damage': round(combatstats['basedamage'] * 1.8),
                      'cost': 3,
                      'costtype': 'mana',
                      'abilitytype': 'damage'},
        }
        return basestats, combatstats, abilities, scalingstats, maxstats

    def cleric(self, basestats=None):
        if not basestats:
            basestats = {
                'vitality': 6,
                'strength': 3,
                'dexterity': 4,
                'intelligence': 2,
                'piety': 10
            }
        maxstats = {
            'health': math.floor(basestats['vitality'] * .90),
            'stamina': round(basestats['vitality'] / 3) +
                       round(basestats['strength'] / 3) +
                       round(basestats['dexterity'] / 3),
            'mana': round(basestats['intelligence'] * .90),
        }
        scalingstats = {
            'health': math.floor(basestats['vitality'] * .90),
            'stamina': round(basestats['vitality'] / 3) +
                       round(basestats['strength'] / 3) +
                       round(basestats['dexterity'] / 3),
            'mana': round(basestats['intelligence'] * .90),
        }
        combatstats = {
            'basedamage' : round(basestats['piety'] * .9)
        }
        abilities = {
            'holy': {'damage': round(combatstats['basedamage'] * 3),
                     'cost': 3,
                     'costtype': 'mana',
                     'abilitytype': 'damage'},
        }
        return basestats, combatstats, abilities, scalingstats, maxstats
