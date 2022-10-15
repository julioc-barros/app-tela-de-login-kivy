from kivymd.app import MDApp
from kivy.core.window import Window 

class Widgets(MDApp):

    Window.size = (300, 600)

    def build(self):
        pass

Widgets().run()