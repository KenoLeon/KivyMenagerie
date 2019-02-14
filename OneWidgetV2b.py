#OneWidgetV2b.py...

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout

Builder.load_string('''
<GridLayout>:
    cols: 2
    Button:
        text: 'Widget 1'
        background_color : [0,1,0,1]
''')


class oneWidgetV2b(App):
    def build(self):
        return GridLayout()


if __name__ == '__main__':
    oneWidgetV2b().run()
