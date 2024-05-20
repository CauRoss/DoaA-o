from kivymd.uix.banner.banner import MDFlatButton
from kivymd.app import MDApp
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivy.metrics import dp
from kivymd.uix.screenmanager import MDScreenManager
from kivy.clock import Clock
from kivymd.uix.dialog import MDDialog

class SplashScreen(MDScreen):
    pass

class LoginScreen(MDScreen):
    pass

class RegisterScreen(MDScreen):
    pass

class MenuScreen(MDScreen):
    pass

class EditarPerfil(MDScreen):
    pass

class CriacaoCampanha(MDScreen):
    pass

class MinhasCampanhas(MDScreen):
    pass

class MinhasDoacoes(MDScreen):
    pass

class Favoritos(MDScreen):
    pass

class Configuracoes(MDScreen):
    pass


class App(MDApp, App):
    dialog = None
    
    def build(self):
        Window.size = (dp(300), dp(600))  
        Window.clearcolor = (1, 1, 1, 1)
        self.theme_cls.primary_palette = 'Teal'
        Builder.load_file(("registerscreen.kv"))
        global sm
        sm = MDScreenManager()
        sm.add_widget(SplashScreen())
        sm.add_widget(LoginScreen())
        sm.add_widget(RegisterScreen())
        sm.add_widget(MenuScreen())
        sm.add_widget(EditarPerfil())
        sm.add_widget(MinhasCampanhas())
        sm.add_widget(MinhasDoacoes())
        sm.add_widget(Favoritos())
        sm.add_widget(Configuracoes())
        sm.add_widget(CriacaoCampanha())
        return sm
    
    def on_start(self):
        Clock.schedule_once(self.change_screen, 3)

    def change_screen(self, dt):
        sm.current = 'criar_login'
    
    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="Tem certeza que você quer sair da sua conta?",
                buttons=[
                    MDFlatButton(
                        text = "CANCELAR",
                        theme_text_color = "Custom",
                        text_color = '#008080',
                    ),
                    MDFlatButton(
                        text = "SAIR",
                        theme_text_color = "Custom",
                        text_color = '#008080',
                    ),
                ],
            )
        self.dialog.open()
         
if __name__ == "__main__":
    App().run()
