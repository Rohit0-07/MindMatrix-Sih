from kivymd.uix.screen import MDScreen
import re

class RegisterationScreen(MDScreen):

    def update_helper_text(self, instance_textfield, field_type):
        if field_type == 'name':
            self.name_validator(instance_textfield)
        elif field_type == 'email':
            self.email_validator(instance_textfield)
        elif field_type == 'password':
            self.pass_validator(instance_textfield)
        elif field_type == "password_c":
            self.pass_c_validator(instance_textfield)
    
    _name_state = False
    def name_validator(self, textfield):
        name = textfield.text.strip()
        if len(name) >= 2 and name.isalpha():
            # textfield.children[2].text = "Valid name"
            RegisterationScreen._name_state = True
            textfield.error = False
        else:
            RegisterationScreen._name_state = False
            # textfield.children[2].text = "Invalid name."
            textfield.error = True

    _email_state = False
    def email_validator(self, textfield):
        email = textfield.text.strip()
        email_regex = r"[^@]+@[^@]+\.[^@]+"
        if re.match(email_regex, email):
            # textfield.children[2].text = "Valid email"
            textfield.error = False
            RegisterationScreen._email_state = True
            # If you want to add real-time email validation for existing emails, 
            # you would typically call an external API here.
        else:
            # textfield.children[2].text = "Invalid email"
            textfield.error = True
            RegisterationScreen._email_state = False

    _pass_state = False
    def pass_validator(self, textfield):
        password = textfield.text
        password_regex = r"^(?=.*[A-Z])(?=.*[0-9])(?=.*[@_])[A-Za-z0-9@_]{6,}$"
        if re.match(password_regex, password) and ' ' not in password:
            # textfield.children[2].text = "Strong password"
            textfield.error = False
            RegisterationScreen._pass_state = True
        else:
            # textfield.children[2].text = ("Password must be at least 6 characters, "
            #                          "include 1 capital letter, 1 digit, "
            #                          "no spaces, and only @ or _ symbols.")
            textfield.error = True
            RegisterationScreen._pass_state = False

    _pass_state_c = False
    def pass_c_validator(self, textfield):
        password = self.ids.password_registeraion.text
        password_c = textfield.text
        if password == password_c:
            # textfield.children[2].text = "Passwords match"
            textfield.error = False
            RegisterationScreen._pass_state_c = True
        else:
            # textfield.children[2].text = "Passwords do not match"
            textfield.error = True
            RegisterationScreen._pass_state_c = False
            
    def validate_all(self, instance):
        state = {
            RegisterationScreen._name_state,
            RegisterationScreen._email_state,
            RegisterationScreen._pass_state,
            RegisterationScreen._pass_state_c,
            }
        if False not in state:
            self.manager.current = "login"
        else:
            print(state)