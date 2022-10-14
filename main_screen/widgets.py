from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar
from kivy.lang import Builder

class AppBar(MDTopAppBar):
    def __init__(self, app_manager, **kwargs):
        super().__init__(**kwargs)

        self.app_manager = app_manager
        self.title = 'Backstage'
        self.elevation = 10
        self.pos_hint = {'top': 1}
        # self.left_action_items = [["menu", lambda x: None]]
        self.right_action_items = [["magnify", lambda x: print('search')]]

    def change_title(self, title):
        self.title = title

class BottomNavigation(MDBottomNavigation):
    def __init__(self, app_manager, **kwargs):
        super().__init__(**kwargs)
        self.app_manager = app_manager

        # region Home
        home_tab = MDBottomNavigationItem()
        home_tab.icon = "home"
        home_tab.name = 'home'
        # home_tab.text = 'Главная'

        home_tab.bind(on_tab_release=lambda x: self.app_manager.app_bar.change_title('Backstage'))


        home_body = MDLabel(text='Home', halign='center')
        home_tab.add_widget(home_body)

        self.add_widget(home_tab)
        # endregion

        # region Search
        search_tab = MDBottomNavigationItem()
        search_tab.icon = "magnify"
        search_tab.name = 'search'
        # search_tab.text = 'Поиск'

        search_tab.bind(on_tab_release=lambda x: self.app_manager.app_bar.change_title('Search'))

        search_body = MDLabel(text='Search', halign='center')
        search_tab.add_widget(search_body)

        self.add_widget(search_tab)
        # endregion

        # region Account
        account_tab = MDBottomNavigationItem()
        account_tab.icon = "account"
        account_tab.name = 'account'
        # account_tab.text = 'Профиль'

        account_tab.bind(on_tab_release=lambda x: self.app_manager.app_bar.change_title('Profile'))


        account_body = MDLabel(text='Account', halign='center')
        account_tab.add_widget(account_body)

        self.add_widget(account_tab)
        # endregion
