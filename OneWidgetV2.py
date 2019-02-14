import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class oneWidgetV2(App):
    def build(self):
        return GridLayout()

if __name__ == '__main__':
    oneWidgetV2().run()
