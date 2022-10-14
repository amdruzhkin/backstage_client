from kivy.core.window import Window
from kivymd.app import MDApp
from app_manager import AppManager

Window.size = (360, 748)

class Backstage(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.app_manager = AppManager()


    def build(self):
        return self.app_manager.screen_manager

if __name__ == "__main__":
    Backstage().run()