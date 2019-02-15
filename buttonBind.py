#buttonBind.py...

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class buttonBindApp(App):

    clickcounter = 0

    def build(self):
        layout = GridLayout(cols=2)
        layout.add_widget(
            Button(
                text='I\'ve been clicked ' +
                str(self.clickcounter) + ' times',
                on_press=self.update))
        return layout

    def update(self, obj):
        self.clickcounter += 1
        obj.text = 'I\'ve been clicked ' + str(self.clickcounter) + ' times'


if __name__ == '__main__':
    buttonBindApp().run()
