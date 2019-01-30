import math


class Character:

    def __init__(self, basestats=None):
        if not basestats:
            self.basestats = {
                    'vitality': 1,
                    'strength': 1,
                    'dexterity': 1,
                    'intelligence': 1,
                    'piety': 1,
                    'luck': 1
                }

    def common_attrs(self):
        equipment = {
            "primary_hand": None
        }
        return {
            "equipment": equipment
        }

    def define_maxstats(self):
        maxstats = {
            'health': math.floor(self.basestats['vitality'] * .90),
            'stamina': round(self.basestats['vitality'] / 3) +
                       round(self.basestats['strength'] / 3) +
                       round(self.basestats['dexterity'] / 3),
            'mana': round((self.basestats['intelligence'] + self.basestats['piety']) * .90),
        }
        return maxstats

    def define_scalingstats(self):
        scalingstats = {
            'health': math.floor(self.basestats['vitality'] * .90),
            'stamina': round(self.basestats['vitality'] / 3) +
                       round(self.basestats['strength'] / 3) +
                       round(self.basestats['dexterity'] / 3),
            'mana': round((self.basestats['intelligence'] + self.basestats['piety']) * .90),
        }
        return scalingstats

    def mage(self, basestats=None):
        if not basestats:
            self.basestats = {
                'vitality': 6,
                'strength': 3,
                'dexterity': 4,
                'intelligence': 10,
                'piety': 2,
                'luck': 5
            }

        combatstats = {
            'basedamage': round(self.basestats['intelligence'] * 1.4)
        }
        abilities = {
            'fireball': {'damage': round(combatstats['basedamage'] * 2),
                         'cost': 3,
                         'costtype': 'mana',
                         'abilitytype': 'damage'},
            'manawall': {'buff': self.basestats['vitality'] * .5,
                         'cost': 3,
                         'costtype': 'mana',
                         'abilitytype': 'buff',
                         'stattobuff': 'health'}
        }
        common = self.common_attrs()
        c = {
            'basestats': self.basestats,
            'combatstats': combatstats,
            'abilities': abilities,
            'scalingstats': self.define_scalingstats(),
            'maxstats': self.define_maxstats(),
            'equipment': common['equipment']
        }
        return c

    def warrior(self, basestats=None):
        if not basestats:
            self.basestats = {
                'vitality': 10,
                'strength': 8,
                'dexterity': 4,
                'intelligence': 1,
                'piety': 2,
                'luck': 5
            }
        maxstats = self.define_maxstats()
        combatstats = {
            'basedamage': round((self.basestats['vitality'] + self.basestats['strength']) * .4)
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
        common = self.common_attrs()
        c = {
            'basestats': self.basestats,
            'combatstats': combatstats,
            'abilities': abilities,
            'scalingstats': self.define_scalingstats(),
            'maxstats': self.define_maxstats(),
            'equipment': common['equipment']
        }
        return c

    def fighter(self, basestats=None):
        if not basestats:
            self.basestats = {
                'vitality': 6,
                'strength': 10,
                'dexterity': 5,
                'intelligence': 1,
                'piety': 3,
                'luck': 5
            }
        combatstats = {
            'basedamage': round(self.basestats['strength'] * 1.3)
        }
        abilities = {
            'brutalize': {'damage': round(combatstats['basedamage'] * 1.8),
                          'cost': 3,
                          'costtype': 'stamina',
                          'abilitytype': 'damage'},
        }
        common = self.common_attrs()
        c = {
            'basestats': self.basestats,
            'combatstats': combatstats,
            'abilities': abilities,
            'scalingstats': self.define_scalingstats(),
            'maxstats': self.define_maxstats(),
            'equipment': common['equipment']
        }
        return c
    
    def ranger(self, basestats=None):
        if not basestats:
            self.basestats = {
                'vitality': 6,
                'strength': 5,
                'dexterity': 10,
                'intelligence': 3,
                'piety': 1,
                'luck': 5
            }
        combatstats = {
            'basedamage': round(self.basestats['dexterity'] * 1.2)
        }
        abilities = {
            'assassinate': {'damage': round(combatstats['basedamage'] * 2.4),
                            'cost': 3,
                            'costtype': 'stamina',
                            'abilitytype': 'damage'},
        }
        common = self.common_attrs()
        c = {
            'basestats': self.basestats,
            'combatstats': combatstats,
            'abilities': abilities,
            'scalingstats': self.define_scalingstats(),
            'maxstats': self.define_maxstats(),
            'equipment': common['equipment']
        }
        return c

    def paladin(self, basestats=None):
        if not basestats:
            self.basestats = {
                'vitality': 10,
                'strength': 5,
                'dexterity': 3,
                'intelligence': 1,
                'piety': 6,
                'luck': 5
            }

        combatstats = {
            'basedamage': round((self.basestats['vitality'] + self.basestats['piety']) * .35)
        }
        abilities = {
            'smite': {'damage': round(combatstats['basedamage'] * 1.8),
                      'cost': 3,
                      'costtype': 'mana',
                      'abilitytype': 'damage'},
        }
        common = self.common_attrs()
        c = {
            'basestats': self.basestats,
            'combatstats': combatstats,
            'abilities': abilities,
            'scalingstats': self.define_scalingstats(),
            'maxstats': self.define_maxstats(),
            'equipment': common['equipment']
        }
        return c

    def cleric(self, basestats=None):
        if not basestats:
            self.basestats = {
                'vitality': 6,
                'strength': 3,
                'dexterity': 4,
                'intelligence': 2,
                'piety': 10,
                'luck': 5
            }
        combatstats = {
            'basedamage': round(self.basestats['piety'] * .9)
        }
        abilities = {
            'holy': {'damage': round(combatstats['basedamage'] * 3),
                     'cost': 3,
                     'costtype': 'mana',
                     'abilitytype': 'damage'},
        }
        common = self.common_attrs()
        c = {
            'basestats': self.basestats,
            'combatstats': combatstats,
            'abilities': abilities,
            'scalingstats': self.define_scalingstats(),
            'maxstats': self.define_maxstats(),
            'equipment': common['equipment']
        }
        return c

