# -*- coding: utf-8 -*-
import os
from kivy.app import App
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore
from kivy.uix.screenmanager import ScreenManager

from screens import BasicScreen

Window.clearcolor = (1, 1, 1, 1)


class NinetyPerTenScreenManager(ScreenManager):
    """Screen manager
    """

    def __init__(self, store, **kwargs):
        self.store = store
        super(NinetyPerTenScreenManager, self).__init__(**kwargs)


class NinetyPerTenApp(App):

    def __init__(self, **kwargs):
        self.store = None
        super(NinetyPerTenApp, self).__init__(**kwargs)
        print "User data dir: %s" % self.user_data_dir

    def build(self):
        self.store = JsonStore(os.path.join(self.user_data_dir, 'ninetyperten.json'))
        sm = NinetyPerTenScreenManager(self.store)
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
