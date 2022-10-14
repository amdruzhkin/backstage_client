from kivy.uix.screenmanager import ScreenManager

from main_screen import MainScreen
from main_screen.widgets import AppBar, BottomNavigation


class AppManager:
    def __init__(self):
        self.app_bar = AppBar(self)
        self.bot_nav = BottomNavigation(self)

        self.screen_manager = ScreenManager()
        self.__initialize_screens()



    def __initialize_screens(self):
        self.screen_manager.add_widget(MainScreen(self))
        self.screen_manager.current = 'main_screen'
