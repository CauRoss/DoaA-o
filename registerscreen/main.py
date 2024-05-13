from kivymd.app import MDApp
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivy.metrics import dp
import os
from kivymd.uix.screenmanager import MDScreenManager

class LoginScreen(MDScreen):
    pass

class RegisterScreen(MDScreen):
    pass

class MenuScreen(MDScreen):
    pass


class App(MDApp, App):
    def build(self):
        Window.size = (dp(300), dp(600))  
        Window.clearcolor = (1, 1, 1, 1)
        self.theme_cls.primary_palette = 'Teal'
        Builder.load_file(os.path.join("registerscreen/registerscreen.kv"))
        sm = MDScreenManager()
        sm.add_widget(LoginScreen())
        sm.add_widget(RegisterScreen())
        sm.add_widget(MenuScreen())
        return sm
         
        
        
if __name__ == "__main__":
    App().run()
