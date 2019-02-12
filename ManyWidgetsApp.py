import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

from kivy.uix.switch import Switch
from kivy.uix.button import Button
from kivy.uix.slider import Slider

class manyWidgetsApp(App):
    def build(self):
        layout = GridLayout(cols=2)
        layout.add_widget(Button(text='Widget 1'))
        layout.add_widget(Switch())
        layout.add_widget(Slider())
        layout.add_widget(Button(text='Widget 4'))
        return layout

if __name__ == '__main__':
    manyWidgetsApp().run()
