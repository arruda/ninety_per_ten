# -*- coding: utf-8 -*-
from kivy.app import App


class NinetyPerTenApp(App):

    def on_pause(self):
        return True

    def on_resume(self):
        pass
