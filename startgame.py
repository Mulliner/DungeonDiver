import math
import random
import os
import sys
from random import shuffle
from random import randint
from random import choice
from colorama import init
from colorama import Fore, Back, Style


import configmanager
from character import Character
from environments import Environments


def start():
    init(autoreset=True)
    c = Character()
    charconfig = read_character_config()
    pu = 'n' # Default "promptuser to no"
    if charconfig['name'] != 'Default':
        announce('We found a previous character, would you like to continue? y/n')
        pu = input('>>> ')
        if pu.lower() == 'y':
            character = charconfig
        else:
            pu = 'n' # For pu to become no, regardless of what the user enters.

    if pu == 'n':
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
        character['inventory'] = dict()
        character['inventory']['gold'] = 0

        announce('Ah, a {classtoplay}. What shall we call you?'.format(classtoplay=classtoplay))
        character['name'] = input('>>> ')
        character['experience'] = 0
        character['level'] = 1
        character['type'] = classtoplay.lower()

        print_stats(character)
        write_character_config(character)

    # start_environment(character)
    enter_hub_world(character)


def write_character_config(character):
    charconf = configmanager.readconfig('charconfig.ini')
    charconf['character']['name'] = str(character['name'])
    charconf['character']['experience'] = str(character['experience'])
    charconf['character']['level'] = str(character['level'])
    charconf['character']['type'] = str(character['type'])
    for stat in character['stats']:
        charconf['stats'][stat] = str(character['stats'][stat])
    for stat in character['scalingstats']:
        charconf['scalingstats'][stat] = str(character['scalingstats'][stat])
    for stat in character['combatstats']:
        charconf['combatstats'][stat] = str(character['combatstats'][stat])
    for item in character['inventory']:
        charconf['inventory'][item] = str(character['inventory'][item])

    write_character = configmanager.writeconfig('charconfig.ini', charconf)


def reset_game():
    charconf = configmanager.readconfig('defaultcharconfig.ini')
    configmanager.writeconfig('charconfig.ini', charconf)

def read_character_config():
    c = Character()
    charconf = configmanager.readconfig('charconfig.ini')
    character = dict()
    character['name'] = charconf['character']['name']
    if character['name'] == 'Default':
        return character

    character['type'] = charconf['character']['type']
    characterobj = getattr(c, character['type'])()
    character['abilities'] = characterobj[2]
    character['level'] = int(charconf['character']['level'])
    character['experience'] = int(charconf['character']['experience'])
    character['stats'] = dict()
    character['scalingstats'] = dict()
    character['maxstats'] = dict()
    character['combatstats'] = dict()
    character['inventory'] = dict()

    for key in charconf['stats']:
        character['stats'][key] = int(charconf['stats'][key])
    for key in charconf['scalingstats']:
        character['scalingstats'][key] = int(charconf['scalingstats'][key])
        character['maxstats'][key] = int(charconf['scalingstats'][key])
    for key in charconf['combatstats']:
        character['combatstats'][key] = int(charconf['combatstats'][key])
    for key in charconf['inventory']:
        character['inventory'][key] = int(charconf['inventory'][key])
    return character


def enter_hub_world(character):
    announce("You're now in the hub. What would you like to do?")
    announce('Start a Dungeon (d) | Check your Stats (s) | Check your Inventory (i)')
    action = input('>>> ')
    if action == 'd':
        clear_command_line()
        start_environment(character)
    elif action == 's':
        clear_command_line()
        print_stats(character)
    elif action == 'i':
        clear_command_line()
        print_inventory(character)
    elif action.lower() == 'cls':
        clear_command_line()
    elif action.lower() == 'q':
        clear_command_line()
        write_character_config(character)
        announce('Saving Character, then exiting!')
        sys.exit()

    enter_hub_world(character)


def clear_command_line():
    os.system('cls')


def start_environment(character):
    env = Environments(level=character['level'])
    possible_environments = [func for func in dir(env) if callable(getattr(env, func)) and '_' not in func]
    chosenenv = random.choice(possible_environments)
    environment = getattr(env, chosenenv)()

    if chosenenv == 'dungeon':
        with open('art/dungeon.txt') as f:
            print(f.read())
    elif chosenenv == 'forest':
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
        enter_hub_world(character)


def print_stats(character):
    announce('Here are your stats, {name}..\n'.format(name=character['name']))
    for k, v in character['stats'].items():
        announce('\t{stat}: {value}'.format(stat=k, value=v))
    announce('-' * 50)
    for k, v in character['scalingstats'].items():
        announce('\t{stat}: {value}'.format(stat=k, value=v))


def print_inventory(character):
    announce('Here is your inventory, {name}..\n'.format(name=character['name']))
    for k, v in character['inventory'].items():
        announce('\t{item}: {value}'.format(item=k, value=v))
    announce('-' * 50)


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
    abilities.append('basic')

    while mob['health'] > 0:
        announce('You have health: {charhealth}, mana: {charmana}, stamina: {charstamina}. | {mobname} has {mobhealth}'\
                 ' health.'
                 .format(charhealth=character['scalingstats']['health'], charmana=character['scalingstats']['mana'],
                         charstamina=character['scalingstats']['stamina'], mobname=mob['name'], mobhealth=mob['health']))

        announce('\nWhat action will you do? ({abilities})'.format(abilities=abilities))
        action = prompt_fight_action()

        if action.lower() == 'basic':
            damage = randint(0, int(damagestat / 2))
        elif action.lower() == 'cls':
            clear_command_line()
            fight(character, mob, environment=environment, mobindex=mobindex)
            break
        elif action.lower() == 'h':
            clear_command_line()
            announce('Heading back to the hub..')
            write_character_config(character)
            enter_hub_world(character)
            break
        elif action.lower() == 'q':
            clear_command_line()
            write_character_config(character)
            announce('Saving Character, then exiting!')
            sys.exit()
        elif action.lower() in abilities:
            costtype = character['abilities'][action.lower()]['costtype']
            abilitytype = character['abilities'][action.lower()]['abilitytype']
            if character['scalingstats'][costtype] >= character['abilities'][action.lower()]['cost']:
                if abilitytype == 'damage':
                    damage = randint(0, character['abilities'][action.lower()][abilitytype])
                else:
                    damage = -1
                character['scalingstats'][costtype] -= character['abilities'][action.lower()]['cost']
            else:
                announce('Not enough {costtype} to use {ability}. Performing basic attack.'
                         .format(costtype=costtype, ability=action.lower()))
                damage = randint(0, int(damagestat / 2))
        else:
            announce(Back.CYAN + 'Action not available')
            damage = 0

        if damage > 0:
            announce(Fore.YELLOW + "{name} attacks {mobname} for {damage} damage!".format(mobname=mob['name'],
                name=character['name'], damage=damage))
            mob['health'] -= damage
        elif damage == 0:
            announce(Back.YELLOW + "{name} missed!".format(name=character['name']))
        else:
            pass

        mobdamage = randint(0, mob['damage'])
        if mobdamage != 0:
            announce(Fore.RED + '{mobname} attacks {name} for {damage} damage!'.format(mobname=mob['name'],
                name=character['name'], damage=mobdamage))
            character['scalingstats']['health'] -= mobdamage
        else:
            announce(Back.YELLOW + '{mobname} missed!'.format(mobname=mob['name']))

        if mob['health'] <= 0:
            os.system('cls')
            chancetogetitems = random.randint(1, 100)
            goldearned = None
            if chancetogetitems <= character['stats']['luck']:
                goldearned = random.randint(1, random.randint(2, character['stats']['luck'] * 10))
                character['inventory']['gold'] += goldearned
            announce('*' * 50 + '\n')
            announce('{mobname} has died to your {damage} damage!\n\t'.format(mobname=mob['name'], damage=damage))
            if goldearned:
                announce(Back.YELLOW + Fore.GREEN + '{mobname} has dropped {gold} gold.'.format(mobname=mob['name'], gold=str(goldearned)))
            announce('*' * 50)
            character['experience'] += mobexperiencevalue
            heal(character)
            announce('{name} has gained {earnedexp} experience | '\
                     'Total exp: {exp}'.format(name=character['name'], earnedexp=mobexperiencevalue,
                                               exp=character['experience']))

        if character['experience'] >= character['level'] * 10:
            character = level(character)

        if character['scalingstats']['health'] <= 0:
            os.system('cls')
            reset_game()
            announce('\tGame Over!\n\n\n')
            start()
        write_character_config(character)
    return character


def prompt_fight_action():
    return input('>>> ')


def level(character):
    announce('!' * 40 + ' LEVEL UP ' + '!' * 40)
    points = 3
    attributes = [k for (k, v) in character['stats'].items()]

    while points > 0:
        clear_command_line()
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

        character['stats'][attribute] += amount
        # if attribute == 'vitality':
        #     character['stats']['vitality'] += amount
        # elif attribute == 'intelligence':
        #     character['stats']['intelligence'] += amount
        # elif attribute == 'strength':
        #     character['stats']['strength'] += amount
        # elif attribute == 'dexterity':
        #     character['stats']['dexterity'] += amount
        # elif attribute == 'piety':
        #     character['stats']['piety'] += amount

    character['experience'] = 0
    character['level'] += 1
    # character = recalcstats(character['stats'], character['name'], character['level'], character['type'])

    # Reset health
    character['scalingstats']['health'] = character['maxstats']['health']
    # Reset stamina
    character['scalingstats']['stamina'] = character['maxstats']['stamina']
    #Reset mana
    character['scalingstats']['mana'] = character['maxstats']['mana']

    os.system('cls')
    print_stats(character)
    write_character_config(character)
    return character


# def recalcstats(stats, name, level, charactertype):
#     c = Character()
#     new_character = getattr(c, charactertype)(basestats=stats)
#     character = dict()
#     character['stats'] = new_character[0]
#     character['combatstats'] = new_character[1]
#     character['abilities'] = new_character[2]
#     character['scalingstats'] = new_character[3]
#     character['maxstats'] = new_character[4]
#     character['name'] = name
#     character['experience'] = 0
#     character['level'] = level
#     character['type'] = charactertype
#     return character

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
