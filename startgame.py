import math
import random
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

    print('#' * 80 + '\n#' + ' ' * 78 + '#' + '\n#\tWelcome to Command-Line Dungeon Diver! '\
    'Begin by selecting a class:     #\n' + '#' + ' ' * 78 + '#' + '\n' + '#' * 80)

    announce('Warrior, Paladin, Fighter, Ranger, Cleric or Mage?')
    classtoplay = input('>>> ')
    try:
        new_character = getattr(c, classtoplay.lower())()
    except AttributeError:
        start()

    character = dict()
    character['stats'] = new_character[0]
    character['combatstats'] = new_character[1]
    character['abilities'] = new_character[2]
    character['scalingstats'] = new_character[3]
    character['maxstats'] = new_character[4]

    announce('Ah, a {classtoplay}. What shall we call you?'.format(classtoplay=classtoplay))
    character['name'] = input('>>> ')
    character['experience'] = 0
    character['level'] = 1
    character['type'] = classtoplay.lower()

    print_stats(character)
    start_environment(character)

def start_environment(character):
    env = Environments(level=character['level'])
    randomenv = random.randint(0, 1)
    if randomenv == 0:
        environment = env.dungeon()
        with open('art/dungeon.txt') as f:
            print(f.read())
    elif randomenv == 1:
        environment = env.forest()
        with open('art/forest.txt') as f:
            print(f.read())

    announce("You've entered a {env}! You sense {enemycount} enemies!".format(env=environment['name'],
                                                                              enemycount=len(environment['mobs'])))

    shuffle(environment['mobs'])
    for mob in environment['mobs']:
        announce('Uh-oh! {mobname} attacks!\n\n'.format(mobname=mob['name']))
        character = fight(character, mob, environment, environment['mobs'].index(mob))

    announce("\nYou've cleared out all of the enemies, now its time for the boss!")
    if environment['boss']['name'] == 'Ogre':
        with open('art/ogre.txt', mode='r') as f:
            print(f.read())
    elif environment['boss']['name'] == 'Alpha Wolf':
        with open('art/alphawolf.txt', mode='r') as f:
            print(f.read())

    character = fight(character, environment['boss'])
    if character:
        announce('You have beaten the boss! Moving on..')
        start_environment(character)


def print_stats(character):
    announce('Here are your stats, {name}..\n'.format(name=character['name']))
    for k, v in character['stats'].items():
        announce('\t{stat}: {value}'.format(stat=k, value=v))
    announce('-' * 50)
    for k, v in character['scalingstats'].items():
        announce('\t{stat}: {value}'.format(stat=k, value=v))



def fight(character, mob, environment=None, mobindex=None):
    if mob['name'] == 'Bat':
        with open('art/bat.txt', mode='r') as f:
            print(f.read())
    elif mob['name'] == 'Skeleton':
        with open('art/skeleton.txt', mode='r') as f:
            print(f.read())
    elif mob['name'] == 'Wolf':
        with open('art/wolf.txt', mode='r') as f:
            print(f.read())
    elif mob['name'] == 'Rabid Squirrel':
        with open('art/squirrel.txt', mode='r') as f:
            print(f.read())
    elif mob['name'] == 'Cougar':
        with open('art/cougar.txt', mode='r') as f:
            print(f.read())

    higheststatvalue = 0
    mobexperiencevalue = mob['health']
    damagestat = character['combatstats']['basedamage']
    abilities = [k for (k, v) in character['abilities'].items()]

    while mob['health'] > 0:
        announce('\nWhat action will you do? (basic or ability | {abilities})'.format(abilities=abilities))
        whoattacks = randint(0, 1)
        action = prompt_fight_action()

        if action.lower() == 'basic':
            damage = randint(0, int(damagestat / 2))

        elif action.lower() == 'ability':
            announce('Which ability?')
            announce(abilities)
            abilityinput = input('>>> ').lower()
            while abilityinput not in abilities:
                abilityinput = input('>>> ').lower()
            damage = randint(0, character['abilities'][abilityinput]['damage'])
        elif action.lower() in abilities:
            damage = randint(0, character['abilities'][action.lower()]['damage'])
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
                character['scalingstats']['health'] -= mobdamage
            else:
                announce(Back.YELLOW + '{mobname} missed!'.format(mobname=mob['name']))

        announce('{charname} health remaining: {charhealth} | {mobname} health remaining: {mobhealth}'
            .format(charname=character['name'], charhealth=character['scalingstats']['health'],
                    mobname=mob['name'], mobhealth=mob['health']))

        if mob['health'] <= 0:
            os.system('cls')
            announce('{mobname} has died!\n'.format(mobname=mob['name']) + '^' * 80)
            character['experience'] += mobexperiencevalue
            heal(character)
            announce('{name} has gained {earnedexp} experience | '\
                     'Total exp: {exp}'.format(name=character['name'], earnedexp=mobexperiencevalue,
                                               exp=character['experience']))

        if character['experience'] >= character['level'] * 10:
            character = level(character)

        if character['scalingstats']['health'] <= 0:
            os.system('cls')
            announce('\tGame Over!\n\n\n')
            start()
    return character


def prompt_fight_action():
    return input('>>> ')


def level(character):
    announce('!' * 40 + ' LEVEL UP ' + '!' * 40)
    points = 3
    attributes = ['vitality', 'intelligence', 'strength', 'dexterity', 'piety']

    while points > 0:
        announce('You have {points} points to spend!'.format(points=points))
        announce('Where would you like them to go? Enter in format "Amount:Attribute"')
        print_stats(character)
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
    character = recalcstats(character['stats'], character['name'], character['level'], character['type'])
    print_stats(character)
    return character


def recalcstats(stats, name, level, charactertype):
    c = Character()
    new_character = getattr(c, charactertype)(basestats=stats)
    character = dict()
    character['stats'] = new_character[0]
    character['combatstats'] = new_character[1]
    character['abilities'] = new_character[2]
    character['scalingstats'] = new_character[3]
    character['maxstats'] = new_character[4]
    character['name'] = name
    character['experience'] = 0
    character['level'] = level
    character['type'] = charactertype
    return character

def heal(character):
    if character['scalingstats']['health'] < round(character['maxstats']['health'] * .7):
        healamount = randint(1, 3)
        character['scalingstats']['health'] += healamount
        announce(Fore.GREEN + '{name} has been healed for {amount} ({currenthealth})'.format(name=character['name'],
            amount=healamount, currenthealth=character['scalingstats']['health']))


def announce(annoucement):
    print('\n\t {annoucement}'.format(annoucement=annoucement))


if '__main__' in __name__:
    start()
