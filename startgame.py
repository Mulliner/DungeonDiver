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

    announce('Warrior, Paladin, Fighter, Ranger, Cleric or Mage?')
    classtoplay = input('>>> ')
    character = dict()

    if classtoplay.lower() == 'warrior':
        character['stats'] = c.warrior()[0]
        character['combatstats'] = c.warrior()[1]
        character['abilities'] = c.warrior()[2]

    elif classtoplay.lower() == 'paladin':
        character['stats'] = c.paladin()[0]
        character['combatstats'] = c.paladin()[1]
        character['abilities'] = c.paladin()[2]

    elif classtoplay.lower() == 'fighter':
        character['stats'] = c.fighter()[0]
        character['combatstats'] = c.fighter()[1]
        character['abilities'] = c.fighter()[2]

    elif classtoplay.lower() == 'ranger':
        character['stats'] = c.ranger()[0]
        character['combatstats'] = c.ranger()[1]
        character['abilities'] = c.ranger()[2]

    elif classtoplay.lower() == 'cleric':
        character['stats'] = c.cleric()[0]
        character['combatstats'] = c.cleric()[1]
        character['abilities'] = c.cleric()[2]

    elif classtoplay.lower() == 'mage':
        character['stats'] = c.mage()[0]
        character['combatstats'] = c.mage()[1]
        character['abilities'] = c.mage()[2]

    else:
        start()

    announce('Ah, a {classtoplay}. What shall we call you?'.format(classtoplay=classtoplay))
    character['name'] = input('>>> ')
    character['stats']['health'] = math.floor(character['stats']['vitality'] * .90)
    character['experience'] = 0
    character['level'] = 1
    character['type'] = classtoplay.lower()

    announce('Here are your stats, {name}..\n'.format(name=character['name']))
    for k, v in character['stats'].items():
        announce('\t{stat}: {value}'.format(stat=k, value=v))

    env = Environments(level=character['level'])
    environment = env.dungeon()
    announce("You've entered a {env}! You sense {enemycount} enemies!".format(env=environment['name'],
                                                                              enemycount=len(environment['mobs'])))

    shuffle(environment['mobs'])
    for mob in environment['mobs']:
        announce('Uh-oh! {mobname} attacks!'.format(mobname=mob['name']))
        fight(character, mob, environment, environment['mobs'].index(mob))

    announce("\nYou've cleared out all of the enemies, now its time for the boss!")
    if environment['boss']['name'] == 'Ogre':
        with open('art/ogre.txt', mode='r') as f:
            print(f.read())
    fight(character, environment['boss'])


def fight(character, mob, environment=None, mobindex=None):
    if mob['name'] == 'Bat':
        with open('art/bat.txt', mode='r') as f:
            print(f.read())
    elif mob['name'] == 'Skeleton':
        with open('art/skeleton.txt', mode='r') as f:
            print(f.read())

    higheststatvalue = 0
    mobexperiencevalue = mob['health']
    damagestat = character['combatstats']['basedamage']

    # if character['type'] == 'mage':
    #     damagestat = round(character['stats']['intelligence'] * 1.4)
    # if character['type'] == 'warrior':
    #     damagestat = round((character['stats']['vitality'] + character['stats']['strength']) * .75)
    # if character['type'] == 'fighter':
    #     damagestat = round(character['stats']['strength'] * 1.2)
    # if character['type'] == 'ranger':
    #     damagestat = round(character['stats']['dexterity'] * 1.3)
    # if character['type'] == 'paladin':
    #     damagestat = round((character['stats']['vitality'] + character['stats']['piety']) * .65)
    # if character['type'] == 'cleric':
    #     damagestat = round(character['stats']['piety'] * .9)


    while mob['health'] > 0:
        announce('\nWhat action will you do? (basic or ability)')
        whoattacks = randint(0, 1)
        action = prompt_fight_action()

        if action.lower() == 'basic':
            damage = randint(0, int(damagestat / 2))

        elif action.lower() == 'ability':
            announce('Which ability?')
            abilites = [k for (k, v) in character['abilities'].items()]
            announce(abilites)
            abilityinput = input('>>> ').lower()
            while abilityinput not in abilites:
                abilityinput = input('>>> ').lower()
            damage = randint(0, character['abilities'][abilityinput]['damage'])

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
            announce('{mobname} has died!\n'.format(mobname=mob['name']) + '^' * 80)
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
    print('\n\t {annoucement}'.format(annoucement=annoucement))


if '__main__' in __name__:
    start()
