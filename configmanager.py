from configparser import ConfigParser

def readconfig(file):
    config = ConfigParser()
    config.read(file)
    return config


def writeconfig(file, config):
    with open(file, 'w') as configfile:
        config.write(configfile)
