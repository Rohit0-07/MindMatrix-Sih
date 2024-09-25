from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.transition import MDFadeSlideTransition
from kivy.core.window import Window
from kivy.lang import Builder

from libs.screens.login import LoginScreen
from libs.screens.home import HomeScreen

class MyScreenManager(MDScreenManager):
    def switch_to_login(self):
        self.current = "login"

    def switch_to_home(self):
        self.current = "home"

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.2
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Light"
        Window.size = (340, 640)  # Common mobile phone size

        # Load the KV files directly in the build method
        Builder.load_file('libs/screens/login.kv')
        Builder.load_file('libs/screens/home.kv')

        # Create the screen instances
        login_screen = LoginScreen()
        home_screen = HomeScreen()

        sm = MyScreenManager(transition=MDFadeSlideTransition(duration=0.1))
        sm.add_widget(login_screen)
        sm.add_widget(home_screen)
        return sm

    def switch_theme(self):
        self.theme_cls.primary_palette = "Blue" if self.theme_cls.primary_palette == "Orange" else "Orange"
        self.theme_cls.theme_style = "Dark" if self.theme_cls.theme_style == "Light" else "Light"

if __name__ == '__main__':
    MainApp().run()