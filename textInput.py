#textInput.py...

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class textInputApp(App):
    def build(self):
        return GridLayout()


if __name__ == '__main__':
    textInputApp().run()
