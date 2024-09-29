from kivymd.uix.screen import MDScreen
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivymd.uix.button import MDIconButton, MDButtonText, MDButton
from kivy.animation import Animation

class LoginScreen(MDScreen):
    current_user_type = StringProperty("User")  # Default to "User"
    show_register_button = BooleanProperty(False)
    
    def on_enter(self):
        # This method is called when the screen is entered
        self.update_register_button()
        
    def on_segment_change(self, user_type):
        self.current_user_type = user_type
        self.ids.user_choice_label.text = user_type
        self.update_register_button()

    def update_register_button(self):
        if self.current_user_type == "Dev" and not self.show_register_button:
            self.show_register_button = True
            reg_button = MDButton(
                MDButtonText(text='Register'),
                style='text',
                pos_hint={"x": 0.75, "top": 1},
                on_release=self.manager.switch_to_authenticate
            )
            self.ids.reg_button.add_widget(reg_button)
        elif self.current_user_type != "Dev" and self.show_register_button:
            self.show_register_button = False
            self.ids.reg_button.clear_widgets()

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
            if not self._once:
                self.ids.layout_hide_pass.add_widget(pass_hide_button)
                self.animate_card_size(dp(300), dp(420))
                self._once = True
        else:
            if self._once:
                self.ids.layout_hide_pass.clear_widgets()
                self.animate_card_size(dp(300), dp(380))
                self._once = False
        
    def animate_card_size(self, width, height):
        card = self.ids.login_card
        anim = Animation(size=(width, height), duration=0.3, t='out_quad')
        anim.start(card)
        
    def show_pass(self, instance):
        instance.icon = "eye" if instance.icon == "eye-off" else "eye-off"
        self.ids.password.password = False if instance.icon == "eye" else True
        
    def login(self, username, password, user_type):
        self.manager.switch_to_home()