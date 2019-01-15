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
                'piety': 2,
                'luck': 5
            }
        maxstats = {
            'health': math.floor(basestats['vitality'] * .90),
            'stamina': round(basestats['vitality'] / 3) +
                       round(basestats['strength'] / 3) +
                       round(basestats['dexterity'] / 3),
            'mana': round((basestats['intelligence'] +  basestats['piety']) * .90),
        }
        scalingstats = {
            'health': math.floor(basestats['vitality'] * .90),
            'stamina': round(basestats['vitality'] / 3) +
                       round(basestats['strength'] / 3) +
                       round(basestats['dexterity'] / 3),
            'mana': round((basestats['intelligence'] +  basestats['piety']) * .90),
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
                         'abilitytype': 'buff',
                         'stattobuff': 'health'}
        }
        c = {
            'basestats': basestats,
            'combatstats': combatstats,
            'abilities': abilities,
            'scalingstats': scalingstats,
            'maxstats': maxstats
        }
        return c


    def warrior(self, basestats=None):
        if not basestats:
            basestats = {
                'vitality' : 10,
                'strength' : 8,
                'dexterity' : 4,
                'intelligence' : 1,
                'piety' : 2,
                'luck': 5
            }
        maxstats = {
            'health': math.floor(basestats['vitality'] * .90),
            'stamina': round(basestats['vitality'] / 3) +
                       round(basestats['strength'] / 3) +
                       round(basestats['dexterity'] / 3),
            'mana': round((basestats['intelligence'] +  basestats['piety']) * .90),
        }
        scalingstats = {
            'health': math.floor(basestats['vitality'] * .90),
            'stamina': round(basestats['vitality'] / 3) +
                       round(basestats['strength'] / 3) +
                       round(basestats['dexterity'] / 3),
            'mana': round((basestats['intelligence'] +  basestats['piety']) * .90),
        }
        combatstats = {
            'basedamage' : round((basestats['vitality'] + basestats['strength']) * .4)
        }
        abilities = {
            'overwhelm': {
                'damage': round(combatstats['basedamage'] * 1.4),
                'cost': 3,
                'costtype': 'stamina',
                'abilitytype': 'damage'
                },
            'warcry': {
                'buff': maxstats['health'] * .8,
                'cost': 7,
                'costtype': 'stamina',
                'abilitytype': 'buff',
                'stattobuff': 'health'
                }
        }
        c = {
            'basestats': basestats,
            'combatstats': combatstats,
            'abilities': abilities,
            'scalingstats': scalingstats,
            'maxstats': maxstats
        }
        return c

    def fighter(self, basestats=None):
        if not basestats:
            basestats = {
                'vitality': 6,
                'strength': 10,
                'dexterity': 5,
                'intelligence': 1,
                'piety': 3,
                'luck': 5
            }
        maxstats = {
            'health': math.floor(basestats['vitality'] * .90),
            'stamina': round(basestats['vitality'] / 3) +
                       round(basestats['strength'] / 3) +
                       round(basestats['dexterity'] / 3),
            'mana': round((basestats['intelligence'] +  basestats['piety']) * .90),
        }
        scalingstats = {
            'health': math.floor(basestats['vitality'] * .90),
            'stamina': round(basestats['vitality'] / 3) +
                       round(basestats['strength'] / 3) +
                       round(basestats['dexterity'] / 3),
            'mana': round((basestats['intelligence'] +  basestats['piety']) * .90),
        }
        combatstats = {
            'basedamage' : round(basestats['strength'] * 1.3)
        }
        abilities = {
            'brutalize': {'damage': round(combatstats['basedamage'] * 1.8),
                          'cost': 3,
                          'costtype': 'stamina',
                          'abilitytype': 'damage'},
        }
        c = {
            'basestats': basestats,
            'combatstats': combatstats,
            'abilities': abilities,
            'scalingstats': scalingstats,
            'maxstats': maxstats
        }
        return c

    
    def ranger(self, basestats=None):
        if not basestats:
            basestats = {
                'vitality' : 6,
                'strength' : 5,
                'dexterity' : 10,
                'intelligence' : 3,
                'piety' : 1,
                'luck': 5
            }
        maxstats = {
            'health': math.floor(basestats['vitality'] * .90),
            'stamina': round(basestats['vitality'] / 3) +
                       round(basestats['strength'] / 3) +
                       round(basestats['dexterity'] / 3),
            'mana': round((basestats['intelligence'] +  basestats['piety']) * .90),
        }
        scalingstats = {
            'health': math.floor(basestats['vitality'] * .90),
            'stamina': round(basestats['vitality'] / 3) +
                       round(basestats['strength'] / 3) +
                       round(basestats['dexterity'] / 3),
            'mana': round((basestats['intelligence'] +  basestats['piety']) * .90),
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
        c = {
            'basestats': basestats,
            'combatstats': combatstats,
            'abilities': abilities,
            'scalingstats': scalingstats,
            'maxstats': maxstats
        }
        return c


    def paladin(self, basestats=None):
        if not basestats:
            basestats = {
                'vitality': 10,
                'strength': 5,
                'dexterity': 3,
                'intelligence': 1,
                'piety': 6,
                'luck': 5
            }
        maxstats = {
            'health': math.floor(basestats['vitality'] * .90),
            'stamina': round(basestats['vitality'] / 3) +
                       round(basestats['strength'] / 3) +
                       round(basestats['dexterity'] / 3),
            'mana': round((basestats['intelligence'] +  basestats['piety']) * .90),
        }
        scalingstats = {
            'health': math.floor(basestats['vitality'] * .90),
            'stamina': round(basestats['vitality'] / 3) +
                       round(basestats['strength'] / 3) +
                       round(basestats['dexterity'] / 3),
            'mana': round((basestats['intelligence'] +  basestats['piety']) * .90),
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
        c = {
            'basestats': basestats,
            'combatstats': combatstats,
            'abilities': abilities,
            'scalingstats': scalingstats,
            'maxstats': maxstats
        }
        return c


    def cleric(self, basestats=None):
        if not basestats:
            basestats = {
                'vitality': 6,
                'strength': 3,
                'dexterity': 4,
                'intelligence': 2,
                'piety': 10,
                'luck': 5
            }
        maxstats = {
            'health': math.floor(basestats['vitality'] * .90),
            'stamina': round(basestats['vitality'] / 3) +
                       round(basestats['strength'] / 3) +
                       round(basestats['dexterity'] / 3),
            'mana': round((basestats['intelligence'] +  basestats['piety']) * .90),
        }
        scalingstats = {
            'health': math.floor(basestats['vitality'] * .90),
            'stamina': round(basestats['vitality'] / 3) +
                       round(basestats['strength'] / 3) +
                       round(basestats['dexterity'] / 3),
            'mana': round((basestats['intelligence'] +  basestats['piety']) * .90),
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
        c = {
            'basestats': basestats,
            'combatstats': combatstats,
            'abilities': abilities,
            'scalingstats': scalingstats,
            'maxstats': maxstats
        }
        return c

