#buttonBindV3.py...

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty


class buttonBindV3App(App):

    clickCounterProperty = NumericProperty(0)

    def build(self):
        return GridLayout()

    def update(self):
        self.clickCounterProperty += 1


if __name__ == '__main__':
    buttonBindV3App().run()
