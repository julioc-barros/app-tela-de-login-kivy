from kivymd.app import MDApp
from kivy.core.window import Window 
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton, MDIconButton, MDFloatingActionButton, MDRectangleFlatButton, MDRaisedButton, MDRectangleFlatIconButton

class Buttons(MDApp):

    Window.size = (300, 600)

    def build(self):
        
        boxLayout = MDBoxLayout(
            orientation = 'horizontal',
            spacing = 15,
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        btn_Login = MDFlatButton(
            text = 'Login',
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        btn_Home = MDIconButton(
            icon = 'home',
            pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        )

        btn_Plus= MDFloatingActionButton(
            icon = 'plus',
            pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        )

        btn_Rectangle= MDRectangleFlatButton(
            text = 'Retangulo',
            pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        )
        
        btn_Raised= MDRaisedButton(
            text = 'Raised',
            pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        )

        btn_Misted= MDRectangleFlatIconButton(
            text = 'Raised',
            icon = 'home',
            pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        )

        boxLayout.add_widget(btn_Login)
        boxLayout.add_widget(btn_Home)
        boxLayout.add_widget(btn_Plus)
        boxLayout.add_widget(btn_Rectangle)
        boxLayout.add_widget(btn_Raised)
        boxLayout.add_widget(btn_Misted)
        

        return boxLayout
Buttons().run()