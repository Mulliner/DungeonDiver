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

if __name__ == '__main__':
    MainApp().run()
