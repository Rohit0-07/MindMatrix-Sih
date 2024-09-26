from kivy.uix.accordion import FloatLayout
from kivymd.uix.screen import MDScreen
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivymd.uix.button import MDIconButton,MDButtonText,MDButton
from kivy.animation import Animation
class LoginScreen(MDScreen):
    current_user_type = StringProperty("User")  # Default to "User"
    _reg = False
        
    def on_segment_change(self, user_type):
        reg_hide_button= MDButton(
            MDButtonText(
                text='Register',
            ),
            style='text',
            pos_hint= {"x": 0.75, "top":1},
            # id= "reg_show",
            # icon= 'account',
            on_release = self.manager.switch_to_authenticate
        )
        self.current_user_type = user_type
        if user_type == "Dev":
            self.ids.user_choice_label.text = "Dev"
            if LoginScreen._reg==False:
                self.ids.reg_button.add_widget(reg_hide_button)
                LoginScreen._reg=True
                pass
        elif user_type == "User":
            self.ids.user_choice_label.text = "User"
            if LoginScreen._reg == True:
                self.ids.reg_button.remove_widget(self.ids.reg_button.children[0])
                LoginScreen._reg =False
                pass
        elif user_type == "Admin":
            self.ids.user_choice_label.text = "Admin"
            if LoginScreen._reg == True:
                self.ids.reg_button.remove_widget(self.ids.reg_button.children[0])
                LoginScreen._reg =False
                pass
    
    _once = False
    def show_password_widget_add(self, instance):
        if instance.text != '':
            pass_hide_button = MDIconButton(
                id="hide_show_pass",
                icon="eye-off",
                style="standard",
                pos_hint={"right": 1.0},
                on_press=self.show_pass,
            )
            if not LoginScreen._once:
                self.ids.layout_hide_pass.add_widget(pass_hide_button)
                self.animate_card_size(dp(300), dp(420))
                LoginScreen._once = True
        else:
            if LoginScreen._once:
                self.ids.layout_hide_pass.remove_widget(self.ids.layout_hide_pass.children[0])
                self.animate_card_size(dp(300), dp(380))
                LoginScreen._once = False
        
    def animate_card_size(self, width, height):
        card = self.ids.login_card
        anim = Animation(size=(width, height), duration=0.3, t='out_quad')
        anim.start(card)
        
    def show_pass(self, instance):
        instance.icon = "eye" if instance.icon == "eye-off" else "eye-off"
        self.ids.password.password = False if instance.icon == "eye" else True
        
    #yet to be implemented
    def login(self, username, password, user_type):
        self.manager.current = "home"
