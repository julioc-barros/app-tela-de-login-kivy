from kivymd.uix.screen import MDScreen

class MenuScreen(MDScreen):
    def login(self):
        self.manager.current = 'login'
    pass

