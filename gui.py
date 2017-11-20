from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from character import Character

def WidgetScreen():
    layout = BoxLayout()
    btn = Button(text='Hello World')
    layout.add_widget(btn)
    return layout

class MyApp(App):

    def build(self):
        return WidgetScreen()


if __name__ == '__main__':
    MyApp().run()
