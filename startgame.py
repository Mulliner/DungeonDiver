import math
import random
import os
import sys
import json
import copy
from random import shuffle
from random import randint
from random import choice
from colorama import init
from colorama import Fore, Back, Style


import configmanager
from character import Character
from environments import Environments
from database import DungeonDiverDB


def start():
    # Init is for colorama, this will set auto-restart to true 
    # and fix colors after each announcement. 
    init(autoreset=True)

    database_connection = DungeonDiverDB()
    db_cc = database_connection.character_collection()
    charrestored = False
    # Load previous character?
    characters = database_connection.restore_character()
    if len(characters) > 0:
        announce(Back.CYAN + 'Character(s) found! Restore?')
        announce('Press enter to start a new character.')
        for character in characters:
            # database_connection.remove_character(character)
            if character['character']['scalingstats']['health'] > 0:
                announce(f"{characters.index(character)}) {character['name']}")
            else:
                characters.remove(character)
        
        charrestore = input('>>> ')
        try:
            if charrestore and int(charrestore) <= len(characters):
                announce(f"You've chosen to restore {characters[int(charrestore)]['name']}")
                charrestored = True
                character = characters[int(charrestore)]
                if 'inventory' not in character:
                    character['inventory'] = {}
                    database_connection.update_character(character['_id'], character)
                    
        except TypeError:
            announce("Invalid input, please restart the game or continue with a new character.")

    if not charrestored:
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
            character['character'] = c.mage()
        elif classtoplay.lower() == 'warrior':
            character['character'] = c.warrior()
        elif classtoplay.lower() == 'fighter':
            character['character'] = c.fighter()
        elif classtoplay.lower() == 'cleric':
            character['character'] = c.cleric()
        elif classtoplay.lower() == 'ranger':
            character['character'] = c.ranger()
        elif classtoplay.lower() == 'paladin':
            character['character'] = c.paladin()
        else:
            start()

        announce(f'Ah, a {classtoplay}. What shall we call you?')
        character['name'] = input('>>> ')
        character['character']['health'] = math.floor(character['character']['basestats']['vitality'] * .85)
        character['experience'] = 0
        character['inventory'] = {'gold': 0}
        character['level'] = 1
        character['type'] = classtoplay.lower()
        save_id = db_cc.insert_one(character).inserted_id
        print_stats(character)
        # write_character_config(character)

    enter_hub_world(character)


def calcmaxstats(stats):
    maxstats = {
        'health': math.floor(stats['vitality'] * .90),
        'stamina': round(stats['vitality'] / 3) +
                   round(stats['strength'] / 3) +
                   round(stats['dexterity'] / 3),
        'mana': round((stats['intelligence'] +  stats['piety']) * .90),
    }
    return maxstats


# def write_character_config(character):
#     charconf = configmanager.readconfig('charconfig.ini')
#     charconf['character']['name'] = str(character['character']['name'])
#     charconf['character']['experience'] = str(character['character']['experience'])
#     charconf['character']['level'] = str(character['character']['level'])
#     charconf['character']['type'] = str(character['character']['type'])
#     for stat in character['character']:
#         charconf['stats'][stat] = str(character['character'][stat])
#     for stat in character['character']['scalingstats']:
#         charconf['scalingstats'][stat] = str(character['character']['scalingstats'][stat])
#     for stat in character['character']['combatstats']:
#         charconf['combatstats'][stat] = str(character['character']['combatstats'][stat])
#     try:
#         for item in character['inventory']:
#             charconf['inventory'][item] = str(character['inventory'][item])
#     except:
#         pass
#
#     configmanager.writeconfig('charconfig.ini', charconf)


def reset_game():
    charconf = configmanager.readconfig('defaultcharconfig.ini')
    configmanager.writeconfig('charconfig.ini', charconf)


def read_character_config(basestats=None):
    c = Character()
    charconf = configmanager.readconfig('charconfig.ini')
    character = dict()
    character['name'] = charconf['character']['name']
    if character['name'] == 'Default':
        return character

    character['type'] = charconf['character']['type']
    if basestats:
        characterobj = getattr(c, character['type'])(basestats=basestats)
    else:
        characterobj = getattr(c, character['type'])()
    character['abilities'] = characterobj[2]
    character['level'] = int(charconf['character']['level'])
    character['experience'] = int(charconf['character']['experience'])
    character['character'] = dict()
    character['scalingstats'] = dict()
    character['maxstats'] = dict()
    character['combatstats'] = dict()
    character['inventory'] = dict()

    for key in charconf['stats']:
        character['character'][key] = int(charconf['stats'][key])
    for key in charconf['scalingstats']:
        character['character']['scalingstats'][key] = int(charconf['scalingstats'][key])
        character['character']['maxstats'][key] = int(charconf['scalingstats'][key])
    for key in charconf['combatstats']:
        character['character']['combatstats'][key] = int(charconf['combatstats'][key])
    for key in charconf['inventory']:
        character['character']['inventory'][key] = int(charconf['inventory'][key])
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
        # write_character_config(character)
        announce('Character Saved!')
        sys.exit()

    enter_hub_world(character)


def clear_command_line():
    try:
        os.system('cls')
    except:
        os.system('clear')


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
    announce(f'Here are your stats, {character["name"]}..\n')
    char_copy = copy.deepcopy(character)
    char_copy['character'].pop('abilities')
    for k, v in char_copy['character'].items():
        if type(v) is not str and type(v) is not int:
            build_print = str()
            for sub_k, sub_v in v.items():
                build_print += f'\n\t\t\t{sub_k}: {sub_v}'
            v = build_print
        announce('\t{stat}: {value}'.format(stat=k, value=v))
    announce('-' * 50)
    for k, v in char_copy['character']['scalingstats'].items():
        announce('\t{stat}: {value}'.format(stat=k, value=v))


def print_inventory(character):
    announce('Here is your inventory, {name}..\n'.format(name=character['name']))
    for k, v in character['inventory'].items():
        announce('\t{item}: {value}'.format(item=k, value=v))
    announce('-' * 50)


def fight(character, mob, environment=None, mobindex=None):
    database_connection = DungeonDiverDB()
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
    damagestat = character['character']['combatstats']['basedamage']
    print(character['character'])
    abilities = [k for (k, v) in character['character']['abilities'].items()]
    abilities.append('basic')

    while mob['health'] > 0:
        announce('You have health: {charhealth}, mana: {charmana}, stamina: {charstamina}. | {mobname} has {mobhealth}'\
                 ' health.'
                 .format(charhealth=character['character']['scalingstats']['health'], charmana=character['character']['scalingstats']['mana'],
                         charstamina=character['character']['scalingstats']['stamina'], mobname=mob['name'], mobhealth=mob['health']))

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
            # write_character_config(character)
            enter_hub_world(character)
            break
        elif action.lower() == 'q':
            clear_command_line()
            # write_character_config(character)
            announce('Saving Character, then exiting!')
            sys.exit()
        elif action.lower() in abilities:
            costtype = character['character']['abilities'][action.lower()]['costtype']
            abilitytype = character['character']['abilities'][action.lower()]['abilitytype']
            if character['character']['scalingstats'][costtype] >= character['character']['abilities'][action.lower()]['cost']:
                if abilitytype == 'damage':
                    damage = randint(0, character['character']['abilities'][action.lower()][abilitytype])
                else:
                    damage = -1
                character['character']['scalingstats'][costtype] -= character['character']['abilities'][action.lower()]['cost']
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
        elif damage == -1:
            announce(Back.BLUE + Fore.GREEN +
                     "{name} used a buff! This will last until your next level up, or ".format(name=character['name']) +
                     "until your stats fall below the buff amount.")
            if character['character']['abilities'][action.lower()]['stattobuff'] == 'health':
                character['character']['scalingstats']['health'] += int(character['character']['abilities'][action.lower()]['buff'])
                announce(Back.BLUE + Fore.GREEN + "{name} now has temporary buff of {amount} to your health!"
                         .format(name=character['name'], amount=int(character['character']['abilities'][action.lower()]['buff'])))
        elif damage == 0:
            announce(Back.YELLOW + "{name} missed!".format(name=character['name']))
        else:
            pass

        mobdamage = randint(0, mob['damage'])
        if mobdamage != 0:
            announce(Fore.RED + '{mobname} attacks {name} for {damage} damage!'.format(mobname=mob['name'],
                name=character['name'], damage=mobdamage))
            character['character']['scalingstats']['health'] -= mobdamage
        else:
            announce(Back.YELLOW + '{mobname} missed!'.format(mobname=mob['name']))

        if mob['health'] <= 0:
            try:
                os.system('cls')
            except:
                os.system('clear')
            announce('{mobname} has died!\n\n'.format(mobname=mob['name']) + '^' * 80)
            chancetogetitems = random.randint(1, 100)
            goldearned = None
            if chancetogetitems <= character['character']['basestats']['luck']:
                goldearned = random.randint(1, random.randint(2, character['character']['basestats']['luck'] * 10))
                if not 'gold' in character['inventory']:
                    character['inventory']['gold'] = 0
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
                                            
        database_connection.update_character(character['_id'], character)
            
        if character['character']['scalingstats']['health'] <= 0:
            os.system('cls')
            reset_game()
            announce('\tGame Over!\n\n\n')
            start()

        if character['experience'] >= character['level'] * 10:
            character = level(character)

        # write_character_config(character)
    return character


def prompt_fight_action():
    return input('>>> ')


def level(character):
    database_connection = DungeonDiverDB()
    announce('!' * 40 + ' LEVEL UP ' + '!' * 40)
    points = 3
    attributes = [k for (k, v) in character['character']['basestats'].items()]

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

        character['character']['basestats'][attribute] += amount

    character['experience'] = character['experience'] - character['level'] * 10
    character['level'] += 1
    character['character']['health'] = math.floor(character['character']['basestats']['vitality'] * .85)
    announce('Here are your new stats, {name}..\n'.format(name=character['name']))
    database_connection.update_character(character['_id'], character)
    for k, v in character['character'].items():
        announce('\t{stat}: {value}'.format(stat=k, value=v))
    return character


def heal(character):
    database_connection = DungeonDiverDB()
    if character['character']['health'] < math.floor(character['character']['basestats']['vitality'] * .85) - 3:
        healamount = randint(1, 3)
        character['character']['health'] += healamount
        database_connection.update_character(character['_id'], character)

    character['maxstats'] = calcmaxstats(character['character']['basestats'])

    # Reset health
    character['character']['scalingstats']['health'] = character['maxstats']['health']
    # Reset stamina
    character['character']['scalingstats']['stamina'] = character['maxstats']['stamina']
    #Reset mana
    character['character']['scalingstats']['mana'] = character['maxstats']['mana']

    os.system('cls')
    print_stats(character)
    # write_character_config(character)
    return character


def announce(annoucement):
    print(f'\n\t {annoucement}')


if '__main__' in __name__:
    start()
