# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager

from screens import BasicScreen

Window.clearcolor = (1, 1, 1, 1)


class NinetyPerTenScreenManager(ScreenManager):
    """Screen manager
    """
    def __init__(self, *args, **kwargs):
        super(NinetyPerTenScreenManager, self).__init__()


class NinetyPerTenApp(App):

    def build(self):
        sm = NinetyPerTenScreenManager()
        basic_screen = BasicScreen(
            name='Main Screen',
        )
        sm.add_widget(basic_screen)
        return sm

    def on_pause(self):
        return True

    def on_resume(self):
        pass


NinetyPerTenApp().run()
