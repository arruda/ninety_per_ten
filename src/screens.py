# -*- coding: utf-8 -*-
from datetime import datetime

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.label import Label
from kivy.uix.button import Button
from npt_events import Event, EVALUATION_POSITIVE, EVALUATION_NEGATIVE


class BasicScreen(Screen):

    def __init__(self, **kwargs):
        super(BasicScreen, self).__init__(**kwargs)
        self.events = []

        self.add_widget(self._build_main_box())

    def _build_botton_grid(self):
        botton_grid = GridLayout(cols=2)

        positive_button = Button(text="Positive", font_size=30)
        positive_button.bind(on_release=self.handle_positive_button)

        negative_button = Button(text="Negative", font_size=30)
        negative_button.bind(on_release=self.handle_negative_button)

        botton_grid.add_widget(positive_button)
        botton_grid.add_widget(negative_button)
        return botton_grid

    def _build_top_box(self):
        top_box = BoxLayout(orientation='vertical')
        self.positive_label = Label(text="0%", font_size=50, color=[0, 0, 0, 1], size_hint=(1, 1))
        self.total_label = Label(font_size=30, color=[0, 0, 0, 1], size_hint=(1, 1))

        top_box.add_widget(self.positive_label)
        top_box.add_widget(self.total_label)
        return top_box

    def _build_main_box(self):
        main_box = BoxLayout(orientation='vertical')
        main_box.add_widget(self._build_top_box())
        main_box.add_widget(self._build_botton_grid())
        return main_box

    def update_positive_label(self):
        if not self.events:
            return
        positive_perc = Event.get_rate(self.events)[0]
        self.positive_label.text = "{}%".format(positive_perc)

    def update_total_label(self):
        self.total_label.text = "Total Entries: {}".format(len(self.events))

    def on_pre_enter(self):
        self.events = Event.get_events(self.manager.store)
        self.update_screen_values()

    def update_screen_values(self):
        self.update_positive_label()
        self.update_total_label()

    def handle_positive_button(self, button):
        self.add_new_event(EVALUATION_POSITIVE)
        self.update_screen_values()

    def handle_negative_button(self, button):
        self.add_new_event(EVALUATION_NEGATIVE)
        self.update_screen_values()

    def add_new_event(self, evaluation):
        new_event = Event(date=datetime.now(), evaluation=evaluation)
        new_event.save(self.manager.store)
        self.events.append(
            new_event
        )
