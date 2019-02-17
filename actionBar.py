#actionBar.py...

import kivy
from kivy.app import App
from kivy.uix.actionbar import ActionBar

class actionBarApp(App):
    def build(self):
        return ActionBar()


if __name__ == '__main__':
    actionBarApp().run()
