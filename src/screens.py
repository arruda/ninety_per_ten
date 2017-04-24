# -*- coding: utf-8 -*-
from datetime import datetime

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout


from kivy.uix.label import Label
from kivy.uix.button import Button
from npt_events import Event, EVALUATION_POSITIVE, EVALUATION_NEGATIVE, FILTERS


class BasicScreen(Screen):

    def __init__(self, **kwargs):
        super(BasicScreen, self).__init__(**kwargs)
        self.events = []
        self.reset_count = 0

        self.add_widget(self._build_main_box())

    def _build_evaluation_box(self):
        evaluation_box = BoxLayout(orientation='horizontal')
        positive_button = Button(
            text="Positive",
            font_size=30,
            size_hint=(.5, .5),
            background_normal='',
            background_color=(0 / 255.0, 102 / 255.0, 0 / 255.0, 1)
        )
        positive_button.bind(on_release=self.handle_positive_button)

        negative_button = Button(
            text="Negative",
            font_size=30,
            size_hint=(.5, .5),
            background_normal='',
            background_color=(255 / 255.0, 0 / 255.0, 0 / 255.0, 1)
        )
        negative_button.bind(on_release=self.handle_negative_button)

        evaluation_box.add_widget(positive_button)
        evaluation_box.add_widget(negative_button)
        return evaluation_box

    def _build_botton_box(self):
        botton_box = BoxLayout(orientation='vertical', spacing=10)
        self.total_label = Label(font_size=30, color=[0, 0, 0, 1], size_hint=(1, 1))

        botton_box.add_widget(self.total_label)
        botton_box.add_widget(self._build_evaluation_box())
        return botton_box

    def _filter_layout(self):
        filter_box = BoxLayout(orientation='vertical', spacing=50)
        reset_button = Button(
            text="Reset",
            font_size=30,
            size_hint=(1, 1),
        )
        reset_button.bind(on_release=self.handle_reset_button)
        filter_box.add_widget(reset_button)

        for filter_type in FILTERS.keys():
            filter_button = Button(
                text=filter_type,
                font_size=30,
                size_hint=(1, 1),
                background_normal='',
                background_color=(239/255.0, 93/255.0, 5/255.0, 1)
            )
            filter_button.bind(on_release=self.handle_filter_button)
            filter_box.add_widget(filter_button)

        return filter_box

    def _menu_layout(self):
        menu_layout = RelativeLayout(
            size_hint=(None, None),
            size=(300, 600),
            pos_hint={'right': 1, 'top': 1},
        )
        menu_layout.add_widget(self._filter_layout())
        return menu_layout

    def _build_top_box(self):
        top_box = BoxLayout(orientation='vertical')

        self.positive_label = Label(text="0%", font_size=150, color=[239/255.0, 93/255.0, 5/255.0, 1], size_hint=(1, 1))

        top_box.add_widget(self._menu_layout())
        top_box.add_widget(self.positive_label)
        return top_box

    def _build_main_box(self):
        main_box = BoxLayout(orientation='vertical')
        main_box.add_widget(self._build_top_box())
        main_box.add_widget(self._build_botton_box())
        return main_box

    def update_positive_label(self):
        if not self.events:
            positive_perc = 100
        else:
            positive_perc = Event.get_rate(self.events)[0]
        self.positive_label.text = "{:.2f}%".format(positive_perc)

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

    def handle_reset_button(self, button):
        if self.reset_count < 7:
            self.reset_count += 1
        else:
            self.reset_count = 0
            self.events = Event.reset_store(self.manager.store)
        self.update_screen_values()

    def handle_filter_button(self, button):
        filter_by = button.text
        filtered_events = Event.filter(self.manager.store, filter_by)
        self.events = filtered_events
        self.update_screen_values()
