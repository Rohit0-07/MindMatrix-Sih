from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.transition import MDFadeSlideTransition
from kivy.core.window import Window
from kivy.lang import Builder

from libs.screens.login import LoginScreen
from libs.screens.home import HomeScreen
from libs.screens.registeration import RegisterationScreen
from libs.screens.authentication import AuthenticationScreen
class MyScreenManager(MDScreenManager):
    def switch_to_login(self):
        self.remove_widget(self.get_screen('login'))
        # Builder.unload_file('libs/screens/login.kv')  # Force reload kv file
        # Builder.load_file('libs/screens/login.kv')  # Force reload kv file
        self.add_widget(LoginScreen(name = "login",
                                    md_bg_color= self.theme_cls.backgroundColor
                                    ))
        self.current = "login"

    def switch_to_home(self):
        self.remove_widget(self.get_screen('home'))
        # Builder.unload_file('libs/screens/home.kv')  # Force reload kv file
        # Builder.load_file('libs/screens/home.kv')  # Force reload kv file
        self.add_widget(HomeScreen(name= "home",
                                    md_bg_color= self.theme_cls.backgroundColor
                                   ))
        self.current = "home"

    def switch_to_register(self):
        self.remove_widget(self.get_screen('register'))
        # Builder.unload_file('libs/screens/registeration.kv')  # Force reload kv file
        # Builder.load_file('libs/screens/registeration.kv')  # Force reload kv file
        self.add_widget(RegisterationScreen(name= "register",
                                            md_bg_color= self.theme_cls.backgroundColor
                                            ))
        self.current = "register"

    def switch_to_authenticate(self, *args):
        self.remove_widget(self.get_screen('authenticate'))
        # Builder.unload_file('libs/screens/authentication.kv')  # Force reload kv file
        # Builder.load_file('libs/screens/authentication.kv')  # Force reload kv file
        self.add_widget(AuthenticationScreen(name = "authenticate",
                                            md_bg_color= self.theme_cls.backgroundColor
                                             ))
        self.current = "authenticate"
        
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
        Builder.load_file('libs/screens/registeration.kv')
        Builder.load_file('libs/screens/authentication.kv')

        # Create the screen instances
        login_screen = LoginScreen(name= "login")
        home_screen = HomeScreen(name= "home")
        authenticate_screen = AuthenticationScreen(name= "authenticate")
        registeration_screen = RegisterationScreen(name= "register")

        sm = MyScreenManager(transition=MDFadeSlideTransition(duration=0.1))
        sm.add_widget(login_screen)
        sm.add_widget(home_screen)
        sm.add_widget(registeration_screen)
        sm.add_widget(authenticate_screen)
        return sm

    def switch_theme(self):
        # self.root.screens.theme_cls.primary_palette = "Blue" if self.theme_cls.primary_palette == "Orange" else "Orange"
        # self.root.screens.theme_cls.theme_style = "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        self.theme_cls.primary_palette = "Blue" if self.theme_cls.primary_palette == "Orange" else "Orange"
        self.theme_cls.theme_style = "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        # Update background color for all screens
        for screen in self.root.screens:
            screen.md_bg_color = self.theme_cls.backgroundColor
if __name__ == '__main__':
    MainApp().run()