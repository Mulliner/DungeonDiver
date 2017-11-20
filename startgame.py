import math
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
    character['stats']['health'] = math.floor(character['stats']['vitality'] -
        .15 * character['stats']['vitality'])
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
        damagestat = character['stats']['intelligence']
    if character['type'] == 'fighter':
        damagestat = character['stats']['intelligence']
    if character['type'] == 'ranger':
        damagestat = character['stats']['intelligence']
    if character['type'] == 'paladin':
        damagestat = character['stats']['intelligence']
    if character['type'] == 'cleric':
        damagestat = character['stats']['intelligence']

    while mob['health'] > 0:
        announce('\nWhat action will you do? (basic or ability)')
        action = input('>>> ')

        if action.lower() == 'basic':
            damage = randint(0, int(damagestat / 2))

        whoattacks = randint(0, 1)
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

        announce('{charname} health remaining: {charhealth}({maxhealth}) | {mobname} health remaining: {mobhealth}'
            .format(charname=character['name'], charhealth=character['stats']['health'],
                    maxhealth=character['stats']['vitality'], mobname=mob['name'], mobhealth=mob['health']))

        if mob['health'] <= 0:
            announce('{mobname} has died!\n\n'.format(mobname=mob['name']) + '^' * 80)
            character['experience'] += mobexperiencevalue
            heal(character)
            announce('{name} has gained {exp} experience'.format(name=character['name'], exp=mobexperiencevalue))

        if character['experience'] >= character['level'] * 10:
            level(character)

        if character['stats']['health'] <= 0:
            announce('Game Over!')
            start()


def level(character):
    announce('!' * 40 + ' LEVEL UP ' + '!' * 40)
    character['experience'] = 0
    character['level'] += 1
    character['stats']['vitality'] += 5
    character['stats']['health'] = math.floor(character['stats']['vitality'] - .15 * character['stats']['vitality'])
    announce('Here are your new stats, {name}..\n'.format(name=character['name']))
    for k, v in character['stats'].items():
        announce('\t{stat}: {value}'.format(stat=k, value=v))

def heal(character):
    if character['stats']['health'] < math.floor(character['stats']['vitality'] - .15 * character['stats']['vitality']) - 3:
        healamount = randint(1, 3)
        character['stats']['health'] += healamount
        announce(Fore.GREEN + '{name} has been healed for {amount} ({currenthealth})'.format(name=character['name'],
            amount=healamount, currenthealth=character['stats']['health']))


def announce(annoucement):
    print('\n\t {annoucement} \n'.format(annoucement=annoucement))


if '__main__' in __name__:
    start()
