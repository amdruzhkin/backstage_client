
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout

from .widgets import AppBar, BottomNavigation

class MainScreen(MDScreen):
    def __init__(self, app_manager, **kwargs):
        super().__init__(**kwargs)

        self.name = 'main_screen'
        self.app_manager = app_manager

        box_layout = MDBoxLayout()
        box_layout.orientation = 'vertical'

        box_layout.add_widget(self.app_manager.app_bar)

        box_layout.add_widget(self.app_manager.bot_nav)

        self.add_widget(box_layout)

