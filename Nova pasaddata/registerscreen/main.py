from kivymd.app import MDApp
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import Screen
from kivymd.uix.screen import MDScreen
from kivy.metrics import dp
import os
from kivymd.uix.screenmanager import MDScreenManager

class LoginScreen:
    def __init__(self):
        return Builder.load_file(os.path.join("loginscreen\loginscreen.kv")) 
        pass

class App(MDApp, App):
    def build(self):
        Window.size = (dp(360), dp(640))  
        Window.clearcolor = (1, 1, 1, 1)
        self.theme_cls.primary_palette = 'Teal'
        
        
if __name__ == "__main__":
    App().run()