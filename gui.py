from kivy.uix.popup import Popup
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

from character import Character


class MainScreen(Screen):
    pass

class ClassSelectScreen(Screen):
    pass

class CharacterNameScreen(Screen):
    pass

class CombatScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("kvs\main.kv")

class MainApp(App):
    def build(self):
        return presentation

    def classchosen(self, classtoplay):
        self.c = Character()
        self.character = dict()
        if classtoplay.lower() == 'warrior':
            self.character['stats'] = self.c.warrior()[0]
            self.character['combatstats'] = self.c.warrior()[1]
            self.character['abilities'] = self.c.warrior()[2]

        elif classtoplay.lower() == 'paladin':
            self.character['stats'] = self.c.paladin()[0]
            self.character['combatstats'] = self.c.paladin()[1]
            self.character['abilities'] = self.c.paladin()[2]

        elif classtoplay.lower() == 'fighter':
            self.character['stats'] = self.c.fighter()[0]
            self.character['combatstats'] = self.c.fighter()[1]
            self.character['abilities'] = self.c.fighter()[2]

        elif classtoplay.lower() == 'ranger':
            self.character['stats'] = self.c.ranger()[0]
            self.character['combatstats'] = self.c.ranger()[1]
            self.character['abilities'] = self.c.ranger()[2]

        elif classtoplay.lower() == 'cleric':
            self.character['stats'] = self.c.cleric()[0]
            self.character['combatstats'] = self.c.cleric()[1]
            self.character['abilities'] = self.c.cleric()[2]

        elif classtoplay.lower() == 'mage':
            self.character['stats'] = self.c.mage()[0]
            self.character['combatstats'] = self.c.mage()[1]
            self.character['abilities'] = self.c.mage()[2]


    def setupname(self, charactername):
        self.character['name'] = charactername

if __name__ == '__main__':
    MainApp().run()
