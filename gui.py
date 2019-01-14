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
    def classchosen(self, classtoplay):
        self.c = Character()
        self.character = dict()
        self.character['stats'] = getattr(self.c, classtoplay)()[0]
        self.character['combatstats'] = getattr(self.c, classtoplay)()[1]
        self.character['abilities'] = getattr(self.c, classtoplay)()[2]
        print(self.character)
        return self.character

class CombatScreen(Screen):
    app = App.get_running_app()

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("kvs\main.kv")


class MainApp(App):
    def build(self):
        return presentation

if __name__ == '__main__':
    MainApp().run()
