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

    c = Character()

    def chooseclass(self, classtoplay):
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

if __name__ == '__main__':
    MainApp().run()
