from abc import ABC, abstractmethod
from pygame import key


class Button(ABC):
    @abstractmethod
    def check_pressed(self):
        pass


# We'll have a general controller with only the buttons we need
# That can be checked uniformly across the code
class Controller:
    # Buttons that can be pressed (and checked)
    buttons_pressed = {}
    button_mappings = {}

    # Button_name (String) should specify our abstract buttons to bind to
    # button (Button) should be an object that implements the Button interface
    def register_button(self, button_name, button):
        if button_name in self.button_mappings.keys():
            self.button_mappings[button_name].add(button)
        else:
            self.button_mappings[button_name] = [button]

    # Takes in a button name and looks through all the actual hardware buttons mapped to it
    # Note that if the keyname doesn't exist, it returns a NoneType (as opposed to a bool)
    def check_button_pressed(self, button_name):
        button_pressed = False
        if button_name in self.button_mappings.keys():
            for button in self.button_mappings[button_name]:
                if button.check_pressed():
                    button_pressed = True

            return button_pressed


# Buttons from the keyboard (specifically)
class KeyboardButton(Button):
    whichKey = None

    def __init__(self, whichKey):
        self.whichKey= whichKey

    def check_pressed(self):
        if key.get_pressed()[self.whichKey]:
            return True
        else:
            return False
