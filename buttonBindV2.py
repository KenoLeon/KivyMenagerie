#buttonBindV2.py...

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class buttonBindV2App(App):

    clickcounter = 0

    def build(self):
        layout = GridLayout(cols=2)
        button = Button(
            text='I\'ve been clicked ' +
            str(self.clickcounter) + ' times')
        layout.add_widget(button)
        button.bind(on_press=self.update)
        return layout

    def update(self, obj):
        self.clickcounter += 1
        obj.text = 'I\'ve been clicked ' + str(self.clickcounter) + ' times'


if __name__ == '__main__':
    buttonBindV2App().run()
