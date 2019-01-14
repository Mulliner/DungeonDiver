import math
import os
from random import shuffle
from random import randint
from colorama import init
from colorama import Fore, Back, Style

from character import Character
from environments import Environments


def start():
    init(autoreset=True)
    c = Character()
    with open('art/dungeon.txt') as f:
        print(f.read())
    print('')

    print('#' * 80 + '\n#' + ' ' * 78 + '#' + '\n#\tWelcome to Command-Line Dungeon Diver! '\
    'Begin by selecting a class:     #\n' + '#' + ' ' * 78 + '#' + '\n' + '#' * 80)

    announce('Mage, Warrior, Fighter, Cleric, Ranger or Paladin?')
    classtoplay = input('>>> ')
    character = dict()
    if classtoplay.lower() == 'mage':
        character['stats'] = c.mage()
    elif classtoplay.lower() == 'warrior':
        character['stats'] = c.warrior()
    elif classtoplay.lower() == 'fighter':
        character['stats'] = c.fighter()
    elif classtoplay.lower() == 'cleric':
        character['stats'] = c.cleric()
    elif classtoplay.lower() == 'ranger':
        character['stats'] = c.ranger()
    elif classtoplay.lower() == 'paladin':
        character['stats'] = c.paladin()
    else:
        start()

    announce('Ah, a {classtoplay}. What shall we call you?'.format(classtoplay=classtoplay))
    character['name'] = input('>>> ')
    character['stats']['health'] = math.floor(character['stats']['vitality'] * .85)
    character['experience'] = 0
    character['level'] = 1
    character['type'] = classtoplay.lower()

    announce('Here are your stats, {name}..\n'.format(name=character['name']))
    for k, v in character['stats'].items():
        announce('\t{stat}: {value}'.format(stat=k, value=v))

    env = Environments(level=character['level'])
    environment = env.dungeon()
    announce("You've entered a {env}! Clear out all of the enemies!".format(env=environment['name']))

    shuffle(environment['mobs'])
    for mob in environment['mobs']:
        announce('Uh-oh! {mobname} attacks!'.format(mobname=mob['name']))
        if mob['name'] == 'Bat':
            with open('art/bat.txt', mode='r') as f:
                print(f.read())
        elif mob['name'] == 'Skeleton':
            with open('art/skeleton.txt', mode='r') as f:
                print(f.read())
        fight(character, mob)

    announce("\nYou've cleared out all of the enemies, now its time for the boss!")
    if environment['boss']['name'] == 'Ogre':
        with open('art/ogre.txt', mode='r') as f:
            print(f.read())
    fight(character, environment['boss'])


def fight(character, mob):
    higheststatvalue = 0
    mobexperiencevalue = mob['health']
    if character['type'] == 'mage':
        damagestat = character['stats']['intelligence']
    if character['type'] == 'warrior':
        damagestat = round((character['stats']['vitality'] + character['stats']['strength']) * .65)
    if character['type'] == 'fighter':
        damagestat = character['stats']['strength']
    if character['type'] == 'ranger':
        damagestat = character['stats']['dexterity']
    if character['type'] == 'paladin':
        damagestat = round((character['stats']['vitality'] + character['stats']['piety']) * .65)
    if character['type'] == 'cleric':
        damagestat = character['stats']['piety']


    while mob['health'] > 0:
        announce('\nWhat action will you do? (basic or ability)')
        whoattacks = randint(0, 1)
        action = prompt_fight_action()

        if action.lower() == 'basic':
            damage = randint(0, int(damagestat / 2))
        else:
            announce(Back.CYAN + 'Action not available, you forfeit your turn.')
            whoattacks = 1

        if whoattacks == 0:
            if damage != 0:
                announce(Fore.YELLOW + "{name} attacks {mobname} for {damage} damage!".format(mobname=mob['name'],
                    name=character['name'], damage=damage))
                mob['health'] -= damage
            else:
                announce(Back.YELLOW + "{name} missed!".format(name=character['name']))
        else:
            mobdamage = randint(0, mob['damage'])
            if mobdamage != 0:
                announce(Fore.RED + '{mobname} attacks {name} for {damage} damage!'.format(mobname=mob['name'],
                    name=character['name'], damage=mobdamage))
                character['stats']['health'] -= mobdamage
            else:
                announce(Back.YELLOW + '{mobname} missed!'.format(mobname=mob['name']))

        announce('{charname} health remaining: {charhealth} | {mobname} health remaining: {mobhealth}'
            .format(charname=character['name'], charhealth=character['stats']['health'],
                    mobname=mob['name'], mobhealth=mob['health']))

        if mob['health'] <= 0:
            os.system('cls')
            announce('{mobname} has died!\n\n'.format(mobname=mob['name']) + '^' * 80)
            character['experience'] += mobexperiencevalue
            heal(character)
            announce('{name} has gained {earnedexp} experience | '\
                     'Total exp: {exp}'.format(name=character['name'], earnedexp=mobexperiencevalue,
                                               exp=character['experience']))

        if character['experience'] >= character['level'] * 10:
            level(character)

        if character['stats']['health'] <= 0:
            announce('Game Over!')
            start()

def prompt_fight_action():
    return input('>>> ')


def level(character):
    announce('!' * 40 + ' LEVEL UP ' + '!' * 40)
    points = 3
    attributes = ['vitality', 'intelligence', 'strength', 'dexterity', 'piety']

    while points > 0:
        announce('You have {points} points to spend!'.format(points=points))
        announce('Where would you like them to go? Enter in format "Amount:Attribute"')
        wheretospend = input('>>> ').split(':')
        try:
            if int(wheretospend[0]) > points or int(wheretospend[0]) <= 0:
                continue
            elif len(wheretospend) != 2:
                continue
            elif wheretospend[1].lower() not in attributes:
                continue
            else:
                points -= int(wheretospend[0])
        except ValueError:
            continue

        amount = int(wheretospend[0])
        attribute = wheretospend[1].lower()

        if attribute == 'vitality':
            character['stats']['vitality'] += amount
        elif attribute == 'intelligence':
            character['stats']['intelligence'] += amount
        elif attribute == 'strength':
            character['stats']['strength'] += amount
        elif attribute == 'dexterity':
            character['stats']['dexterity'] += amount
        elif attribute == 'piety':
            character['stats']['piety'] += amount

    character['experience'] = 0
    character['level'] += 1
    character['stats']['health'] = math.floor(character['stats']['vitality'] * .85)
    announce('Here are your new stats, {name}..\n'.format(name=character['name']))
    for k, v in character['stats'].items():
        announce('\t{stat}: {value}'.format(stat=k, value=v))

def heal(character):
    if character['stats']['health'] < math.floor(character['stats']['vitality'] * .85) - 3:
        healamount = randint(1, 3)
        character['stats']['health'] += healamount
        announce(Fore.GREEN + '{name} has been healed for {amount} ({currenthealth})'.format(name=character['name'],
            amount=healamount, currenthealth=character['stats']['health']))


def announce(annoucement):
    print(f'\n\t {annoucement}')


if '__main__' in __name__:
    start()
