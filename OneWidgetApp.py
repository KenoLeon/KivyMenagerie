import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class oneWidgetApp(App):
    def build(self):
        layout = GridLayout(cols=2)
        layout.add_widget(Button(text='Widget 1'))
        return layout

if __name__ == '__main__':
    oneWidgetApp().run()
